# Root Cause Analysis — Concurrent-Writer Race on Watcher-Owned State

| Field | Value |
| --- | --- |
| RCA ID | RCA-20260613-001 |
| Status | **Draft for Thomas's analysis** (Watcher-authored; adoption of measures is Thomas / Quill's call) |
| Author | Watcher (Stan) |
| Date | 2026-06-13 |
| Severity | Medium — coordination integrity (no code/data loss; duplicate IDs + transiently stale board) |
| Component | AgentBus coordination layer (Watcher Governance Model v1) |
| Related | `watcher/watcher_rules.md`, DECISION-20260613-002 (File Authority Matrix), `watcher/event_log.md` EVENT-20260613-027 |

---

## 1. Summary

During the EPIC-002 / EPIC-003 burst on 2026-06-13 (~19:23–21:47), more than one actor wrote
**Watcher-owned state files** concurrently against a shared working tree. Because AgentBus is a
markdown-only model with no locking and message IDs are allocated by "read the latest, add one,"
the concurrency produced **duplicate message IDs** and a **transiently stale sprint board**.

No work was lost and no review outcome was altered. The artifacts are recoverable and were
reconciled. The incident is a **process/ownership-boundary failure**, not a data-integrity
failure.

---

## 2. Impact

- **Duplicate message IDs** (two distinct messages sharing one ID):
  - `MSG-20260613-W011` — Codex (TASK-019 submission) **and** Gemini (EPIC-003 claim).
  - `MSG-20260613-W012` — Claude (TASK-019 accepted) **and** Gemini (EPIC-003 breakdown accepted).
  - `MSG-20260613-015` — Watcher welcome in `comms/inbox_gemini.md` **and** a Watcher TASK-019
    broadcast in `comms/broadcast.md` (cross-file).
- **Transiently stale board** — `state/sprint_board.md` lagged or was double-written for TASK-019
  and TASK-020 until reconciled.
- **Wasted/duplicated Watcher effort** — at least one autonomous loop pass found work "already
  done" by another actor and had to hold.
- **No impact to:** task acceptance decisions, review artifacts (`reviews/REVIEW-0NN.md`),
  decision log, or Voice_Gen code commits. Append-only history was preserved throughout.

---

## 3. Timeline (2026-06-13, local time; all commits authored by the shared git user `tdorsi`)

| Time | Commit | Actor (per message) | Note |
| --- | --- | --- | --- |
| 19:23 | a36887c | Watcher | TASK-016 submitted → Review (EVENT-013, MSG-010) |
| 19:30 | 401a8f4 | Claude reviewer | TASK-016 accepted — touched **only** `inbox_watcher.md` ✅ |
| 19:37 | e507d4d | Watcher | TASK-016 → Done (EVENT-014, MSG-011) |
| 19:49 | d201cf2 | Claude reviewer | TASK-018 accepted — **only** `inbox_watcher.md` ✅ |
| 19:52 | 9f7baa4 | Watcher | TASK-018 → Done (EVENT-016, MSG-013) |
| 20:42 | 0ef2937 | Watcher | EPIC-003 activated, Gemini onboarded (DISPATCH-004) |
| 20:46 | 19bf0e0 | Watcher | roles/roadmap amended (EVENT-020) |
| 20:50 | **392f5a1** | **Claude reviewer** | **TASK-019 accepted — also wrote `sprint_board.md`, `event_log.md`, `dispatch_queue.md`, `state_snapshot.md`, `broadcast.md` ❌ (boundary crossing)** |
| 20:53 | e40b8f3 | Codex | TASK-020 submitted |
| 21:01 | fd1e7dc | Claude reviewer | EPIC-003 breakdown accepted-with-changes — only `inbox_watcher.md` ✅ |
| 21:24 | 4be52cf | Claude reviewer | TASK-020 changes-requested — only `inbox_watcher.md` ✅ |
| (within window) | — | concurrent pass | Inbox duplicates renumbered (W011/W012 → W015/W016) |
| 21:47 | aec29c0 | Watcher | Single-threaded catch-up reconciliation (EVENT-024..027, DISPATCH-005) |

The autonomous 15-minute Watcher loop (cron `af03d40d`, created earlier in the session) was
firing throughout this window and was **paused** once the contention was identified.

---

## 4. Root Cause

**Primary root cause:** Watcher-owned state was written by more than one actor at the same time,
with no mechanism to serialize writers or allocate IDs without collision.

Two concurrent writers were active:
1. The **autonomous Watcher loop** (`af03d40d`) running every 15 minutes in one session.
2. The **Claude reviewer instance**, which in commit `392f5a1` performed a *full Watcher pass*
   (board mirror + event log + dispatch + snapshot + status broadcast) instead of only recording
   its review outcome and routing it to the Watcher inbox.

### 5-Whys

1. *Why duplicate IDs / stale board?* Two actors wrote Watcher-owned files against the same base
   without seeing each other's edits.
2. *Why two actors?* The reviewer performed Watcher duties (392f5a1) **and** an autonomous Watcher
   loop was also running.
3. *Why did the reviewer do Watcher duties?* The reviewer's operating instructions don't restate
   the ownership boundary, and **nothing technically prevents** any agent from editing
   Watcher-owned files — the File Authority Matrix is documentation, not enforcement.
4. *Why did concurrency cause collisions rather than a clean conflict?* IDs are allocated by
   "read latest sequential ID, increment." Two readers at the same base pick the same next ID.
   Appends to different regions of a file don't even produce a git conflict.
5. *Why no detection until IDs collided?* There is no automated consistency check for duplicate
   IDs or board/`tasks/*` divergence; detection was manual (a Watcher pass noticing the dupes).

### Contributing factors

- **Shared working tree** across multiple CLI instances (single directory, single git user).
- **No advisory lock** for a Watcher pass.
- **Global, monotonic, manually-assigned IDs** (`MSG-YYYYMMDD-NNN`, `W0NN`, `EVENT-…`, etc.) — a
  contention hot spot under concurrency.
- **Ownership is advisory** — `watcher_rules.md` names owners but the toolchain allows any writer.
- **High burst rate** — six task/review transitions plus a new-agent onboarding inside ~2.5 hours.

---

## 5. What Went Well / Detection

- **Append-only discipline held** — no history was deleted; collisions were additive and fully
  recoverable.
- **Routing mostly worked** — 5 of 6 reviewer commits correctly touched only `inbox_watcher.md`.
- **Self-healing** — a concurrent pass renumbered the inbox duplicates (W011/W012 → W015/W016);
  the Watcher catch-up pass annotated the residual collision (EVENT-027) and reconciled the board.
- **Gap:** detection was entirely manual and after-the-fact.

---

## 6. Resolution (actions already taken)

1. Paused the autonomous Watcher loop (`CronDelete af03d40d`) to cut one concurrent writer.
2. Ran a single-threaded catch-up reconciliation (commit `aec29c0`): TASK-020 → changes-requested
   + fix routed to Codex; EPIC-003 TASK-022–025 created and dispatched (DISPATCH-005).
3. Documented the ID collisions and disambiguation in `watcher/event_log.md` EVENT-20260613-027
   (originals left intact per append-only policy).

---

## 7. Recommended Preventative Measures

Prioritized; each maps to a cause above. **Adoption is Thomas / Quill's decision** — items that
touch `procedures/*` or `watcher_rules.md` are governance changes.

### Immediate (process; no tooling)

- **P1 — One Watcher writer at a time.** Never run the autonomous Watcher loop concurrently with a
  manual Watcher pass or with agents that self-mirror. Designate a single Watcher writer per work
  session. *(Addresses: primary cause, factor "shared tree".)*
- **P2 — Reinforce the reviewer boundary in instructions.** Reviewer's lane = record outcome in
  `tasks/review.md` + `reviews/`, post to `comms/inbox_watcher.md`, **stop**. Do not write
  `sprint_board.md`, `event_log.md`, `dispatch_queue.md`, `state_snapshot.md`, or status
  broadcasts. *(Addresses: why-3, the 392f5a1 crossing.)*

### Near-term (lightweight tooling / docs)

- **P3 — Codify P2 in `procedures/review_response.md`** so the boundary is durable for any
  reviewer, not just a prompt. (Draft available on request.)
- **P4 — Collision-resistant IDs.** Replace the global "read-latest+1" scheme with IDs that don't
  require a shared counter — e.g., agent-scoped suffix (`MSG-20260613-claude-03`) or a short
  timestamp/hash component. At minimum, keep per-inbox W-series strictly per-recipient and have
  each agent prefix broadcast IDs with its own initials. *(Addresses: why-4.)*
- **P5 — Advisory lock for Watcher passes.** A `watcher/.watcher.lock` file (claim → pass →
  release, with a stale-lock timeout) gives single-writer semantics in the markdown model without
  a runtime. *(Addresses: primary cause.)*
- **P6 — Pull-before-write + commit-immediately.** Each actor pulls (`--rebase`) immediately
  before editing shared state and commits/pushes in one tight unit; avoid long-lived uncommitted
  edits in the shared tree. *(Addresses: factors "shared tree", burst rate.)*

### Detection

- **P7 — Extend `agentbus_health.py`** to flag (a) duplicate message/event/dispatch IDs across
  `comms/*` and `watcher/*`, and (b) `sprint_board.md` rows that disagree with `tasks/*`. Run it
  at the start of every Watcher pass. *(Addresses: why-5.)*

### Longer-term (architecture)

- **P8 — Watcher-as-service (Phase 2).** The original governance proposal deferred a single-process
  Watcher. A single writer process that owns all Watcher state structurally eliminates this class
  of race. Revisit if burst concurrency becomes routine. *(Addresses: primary cause at the root.)*
- **P9 — Per-agent working directories or a serialized merge path** (e.g., agents push to their own
  branches; one integrator merges) instead of all instances sharing one working tree on `main`.

### Recommended minimum set

P1 + P2 immediately; P3, P4, and P7 near-term. These remove both concurrent Watcher writers and
make the remaining ID scheme collision-resistant and self-checking, at low cost.

---

## 8. Open Questions for Thomas / Quill

1. Is the standalone Watcher loop still wanted, given agents/reviewers have been self-mirroring? If
   yes, enforce single-writer (P1/P5); if no, retire the loop and have the Watcher run on-demand.
2. Should the reviewer boundary (P2) be enforced via instruction only, or codified in
   `procedures/review_response.md` (P3)?
3. Appetite for changing the ID scheme (P4) — it touches every agent's message-writing habit.

---

## Appendix A — Watcher-owned files (per `watcher_rules.md` / DECISION-20260613-002)

`state/sprint_board.md`, `watcher/event_log.md`, `watcher/dispatch_queue.md`,
`state/state_snapshot.md`, and **status-change** broadcasts in `comms/broadcast.md`. Agents own
`tasks/*`, `reviews/*`, `logs/*`, their own `comms/inbox_<agent>.md` sends, and announcement
broadcasts. `comms/inbox_watcher.md` is the routing target for review outcomes / completions /
blockers.

## Appendix B — Evidence command

```
git log --oneline -20 --format="%h %s" | grep -i "Claude CLI.*review" \
  | while read h _; do git show --stat --format="" $h \
      | grep -E "sprint_board|event_log|dispatch_queue|state_snapshot|broadcast"; done
```

Result: only `392f5a1` wrote Watcher-owned state; the other reviewer commits touched only
`comms/inbox_watcher.md`.
