# State Snapshot

Use this file for concise, human-readable snapshots of AgentBus operating state.

> **Archive note (2026-06-13):** Snapshots `SNAPSHOT-20260601-001` through `SNAPSHOT-20260613-008`
> (including some duplicate `-003`/`-004` IDs from parallel Codex/Stan writes) were trimmed for
> readability. The full prior history is preserved verbatim in
> [`state/state_snapshot_archive_20260613.md`](state_snapshot_archive_20260613.md). This file
> now carries only the current operating summary; new snapshots continue from `SNAPSHOT-20260613-009`.

## SNAPSHOT-20260613-009

Date: 2026-06-13
Owner: Watcher (Stan)
Related Task: EPIC-002 / Voice_Gen v0.3.0

### Source of Truth

- `origin/main` is authoritative; agents fetch before treating local files as current.
- Watcher (Stan) is active and owns `state/sprint_board.md`, `watcher/event_log.md`,
  `watcher/dispatch_queue.md`, this snapshot file, and status-change broadcasts. `tasks/*`
  remains authoritative for individual task state; the board is a derived mirror.
- A 15-minute Watcher loop (cron job `af03d40d`, session-only) runs the pass automatically.

### Voice_Gen v0.3.0 Progress

- **EPIC-001 (Shared Configuration Framework): Complete** — TASK-011–014 accepted.
- **EPIC-002 (Voice_Gen Hardening): in progress — 2 of 5 accepted.**
  - Branch `vg_e002_voice_gen_hardening` (off `vg_e001_shared_config`). Owner Codex CLI, reviewer Claude CLI, under DISPATCH-20260613-003 (open).
  - Accepted: TASK-016 (overwrite protection, REVIEW-012), TASK-018 (KeyboardInterrupt, REVIEW-013).
  - Dropped: TASK-017 (handler-clear already delivered by EPIC-001).
  - Ready: TASK-019 (dependency-check logging order — next), TASK-020 (`--log-file` plumbing), TASK-021 (`--dry-run`).
  - Recorded scope decision: DECISION-20260613-004 (TASK-016 logged `--force`; TASK-021 `--dry-run`).
- **EPIC-003 (Text_to_Audio Enhancements): not started.**

### Open With Thomas (not yet dispatched)

- EPIC-003 scope (thin after EPIC-001 absorbed feature items 4a/4c/4d).
- EPIC-003 owner and the parallel-execution model with the current single-implementer team (Codex implements, Claude reviews).

## SNAPSHOT-20260613-010

Date: 2026-06-13
Owner: Watcher (Stan)
Related Task: EPIC-002 / EPIC-003

### Two Epics in Parallel; Gemini Added

- **Gemini CLI** joined as a third agent (implementer). Coordination surfaces live: `comms/inbox_gemini.md`, routing-table row. (Onboarding files `GEMINI.md`/`agent_status.md`/`sync_log.md` are Gemini's to commit.)
- **EPIC-002 (Codex / Claude): 2 of 5 accepted** — TASK-016, TASK-018 done; TASK-017 dropped; TASK-019 next, TASK-020/021 Ready under DISPATCH-20260613-003.
- **EPIC-003 (Gemini / Claude): activated, breakdown pending.** Combined scope per Thomas (2026-06-13): #4b per-chunk WAV + progress/ETA reporting (EPIC-004 pulled forward); EPIC-005 deferred. Branch `vg_e003_text_to_audio_enhancements`; tasks will be TASK-022+. DISPATCH-20260613-004; EVENT-20260613-018/019.

### Open / Pending

- Roadmap and v0.3.0 release-plan docs need amending for the 003+004 combine and 005 deferral (Thomas / Quill).
- Awaiting Gemini's EPIC-003 branch + breakdown, then Claude's review, then Watcher task creation.

## SNAPSHOT-20260613-011

Date: 2026-06-13
Owner: Watcher (Stan)
Related Task: EPIC-002 / TASK-019

### EPIC-002 Progress: TASK-019 in review

- **EPIC-002 (Codex / Claude): 2 of 5 accepted; TASK-019 in review.**
  - Done: TASK-016 (overwrite protection), TASK-018 (KeyboardInterrupt).
  - In review: TASK-019 (dependency-check logging order), Voice_Gen commit `8b993a5`.
  - Ready: TASK-020 (`--log-file` plumbing), TASK-021 (`--dry-run`).
- **EPIC-003 (Gemini / Claude): activated in parallel; breakdown still pending.**

### Open / Pending

- Awaiting Claude CLI's TASK-019 review outcome, routed to `comms/inbox_watcher.md`.
- Awaiting Gemini's EPIC-003 branch + breakdown, then Claude's review, then Watcher task creation.

## SNAPSHOT-20260613-012

Date: 2026-06-13
Owner: Watcher (Stan)
Related Task: EPIC-002 / TASK-020

### EPIC-002 Progress: TASK-020 in review

- **EPIC-002 (Codex / Claude): 3 of 5 accepted; TASK-020 in review.**
  - Done: TASK-016 (overwrite protection), TASK-018 (KeyboardInterrupt), TASK-019 (dependency-check logging order).
  - In review: TASK-020 (`--log-file` plumbing), Voice_Gen commit `bf31d45`.
  - Ready: TASK-021 (`--dry-run`).
- **EPIC-003 (Gemini / Claude): activated in parallel; breakdown/review flow still pending in local comms.**

### Open / Pending

- Awaiting Claude CLI's TASK-020 review outcome, routed to `comms/inbox_watcher.md`.
- Awaiting Gemini EPIC-003 breakdown review closure and Watcher task creation.

## SNAPSHOT-20260614-001

Date: 2026-06-14
Owner: Watcher (Stan)
Related Task: EPIC-002 / EPIC-003 / TASK-026

### All Agents Paused — Handoffs Recorded

Single-threaded Watcher pass processed the three session handoffs
(`comms/watcher_inbox/{codex,claude,gemini}.md`). All agents paused for the
communication-isolation cutover; the autonomous loop remains paused.

Board state:
- **EPIC-002 (Codex / Claude):** TASK-016/018/019 Done; **TASK-020 Changes requested**
  (REVIEW-016 F1 — fix routed to Codex); TASK-021 Ready.
- **EPIC-003 (Gemini / Claude):** TASK-022–025 Ready (DISPATCH-20260613-005); breakdown accepted
  with changes (REVIEW-015).
- **TASK-026 (Codex / Claude):** Dispatched (DISPATCH-20260614-001) — communication-isolation
  residual code/infra + AGENTS.md startup-file cutover; begins on restart.

Governance in effect (DECISION-20260614-001): single-writer Watcher state; per-agent inboxes
`comms/watcher_inbox/<agent>.md` with agent-scoped IDs; reviewer boundary; per-agent project
working trees; per-task session branches `‹epic›__‹agent›__‹TASK-ID›` (merge up after Accepted,
then prune). Shared grounding = `D:\Development\AGENTS.md`; `GEMINI.md` repointed.

### Restart Order (operator)

Codex → TASK-026 (cutover) then TASK-020 fix; Gemini → TASK-022; Claude reviews each under the new
boundary. Each works in its own working tree on its own per-task session branch.

### Open / Pending

- Operator: set up per-agent Voice_Gen working trees; restart agents under the new rules.
- Watcher resumes manual passes (loop stays paused until cutover verified in TASK-026).

## SNAPSHOT-20260614-002

Date: 2026-06-14
Owner: Watcher (Stan) — first snapshot from `AgentBus_stan`
Related Task: TASK-027 / EPIC-002 / EPIC-003

### Full Isolation Complete; EPICs Resumed

- **TASK-026** (project-repo worktree isolation) and **TASK-027** (AgentBus per-agent-clone isolation) are both **Accepted/Done**. The single-shared-checkout race from RCA-20260613-001 is closed at both levels.
- **Watcher cutover complete:** the Watcher now operates from `D:\Development\Sandbox\AgentBus_stan`; canonical `D:\Development\AgentBus` is the human-operated reference. All agents (Codex/Claude/Gemini/Stan; Quill clone available) work from their own AgentBus clones with `git pull --rebase` before push, and from their own Voice_Gen worktrees for project work.
- **EPIC-002 RESUMED:** TASK-016/018/019/020 Done; **TASK-021** (`--dry-run`) is Codex's next (last EPIC-002 item).
- **EPIC-003 RESUMED:** TASK-022 Done; **TASK-023** (progress reporting) is Gemini's next, then 024/025.
- Governance unchanged (DECISION-20260614-001/002): single-writer Watcher state, per-agent inboxes, reviewer boundary, per-agent worktrees/clones.

### Open / Pending

- Resume normal flow: Codex → TASK-021; Gemini → TASK-023; Claude reviews each from `AgentBus_claude`.
- Housekeeping (non-blocking): `agentbus_health.py` still reports pre-cutover legacy duplicate-IDs / board-divergence items; worth a cleanup pass when the queue settles.

## SNAPSHOT-20260614-003

Date: 2026-06-14
Owner: Watcher (Stan)
Related Task: EPIC-003 / EPIC-002 / TASK-021

### EPIC-003 Feature-Complete; EPIC-002 One Review Out

- **EPIC-003: feature-complete** — TASK-022 (keep-chunks), TASK-023 (progress), TASK-024 (ETA), TASK-025 (docs) all accepted (REVIEW-019/021/022/023). DISPATCH-20260613-005 Complete.
  - **Open FU1 (Blocked, Thomas / test window):** TASK-025 C4 real recorded end-to-end MOSS-TTS run (`--keep-chunks` + `--voice all`) — needs GPU/model; analogous to TASK-009. Code inspection-verified.
- **EPIC-002:** TASK-016/018/019/020 done; **TASK-021 (`--dry-run`) in review** (`6529caa`) — the single remaining EPIC implementation item.
- All work running from the per-agent clone model (Watcher on `AgentBus_stan`); pushes via `pull --rebase`.

### Next

- Claude reviews TASK-021. On acceptance: EPIC-002 done → **Phase 3 (integration / v0.3.0 RC)** is unblocked — merge `vg_e002` + `vg_e003` up into `vg_e001_shared_config` per `branching_strategy.md` (a Thomas/Quill milestone).
- Thomas: schedule FU1 (real e2e validation); decide whether to track it as a task.

## SNAPSHOT-20260615-001

Date: 2026-06-15
Owner: Watcher (Stan)
Related Task: Voice_Gen v0.3.0 / Phase 3

### Voice_Gen v0.3.0 Feature + Validation COMPLETE

- **EPIC-002 (Hardening): COMPLETE** — TASK-016/018/019/020/021 accepted (017 dropped).
- **EPIC-003 (Text_to_Audio): COMPLETE & runtime-validated** — TASK-022/023/024/025 accepted; TASK-028 real e2e run accepted (REVIEW-025, FU1 closed). 67 real chunk WAVs + live progress/ETA verified.
- No open EPIC tasks; Blocked empty; Claude's review queue empty. All work running from per-agent clones (Watcher on `AgentBus_stan`).

### Next: Phase 3 — Integration / v0.3.0 RC (awaiting Thomas/Quill)

- Merge `vg_e002_voice_gen_hardening` + `vg_e003_text_to_audio_enhancements` up into `vg_e001_shared_config` per `branching_strategy.md` Merge Rules → that branch becomes the v0.3.0 RC. A **development action** (Codex/Gemini in worktrees) needing PO/PM sequencing; Watcher dispatches once directed. Escalated via MSG-20260615-002.

### Non-blocking env follow-ups for Thomas (not v0.3.0 blockers)

- onnxruntime BFC Arena ~2.3 GB OOM caps very long single runs (env fix if full-length runs needed).
- Model-warmup-inflated initial ETA — optional future refinement (post-first-chunk / rolling-window CPS).
- TASK-024 nit: redundant input read/split in `main()`. `agentbus_health.py` legacy duplicate-ID/board-divergence cleanup still pending.

## SNAPSHOT-20260621-001

Date: 2026-06-21
Owner: Watcher (Stan)
Related Task: Phase 3 / v0.3.0 RC / TASK-029 / TASK-030

### Phase 3 Integration ACTIVATED

Thomas authorized Phase 3 (integration / v0.3.0 RC) and the merge-up order: **`vg_e003` first, then `vg_e002`**. Two tasks created and mirrored:

- **TASK-029 (Gemini CLI):** merge `vg_e003_text_to_audio_enhancements` → `vg_e001_shared_config`. **Dispatched now** (DISPATCH-20260621-001).
- **TASK-030 (Codex CLI):** merge `vg_e002_voice_gen_hardening` → `vg_e001_shared_config`. **Gated on TASK-029 acceptance** (DISPATCH-20260621-002).

Claude CLI reviews both. `vg_e001_shared_config` is the v0.3.0 RC target.

### Integration-Readiness Gap (Watcher-verified 2026-06-21)

The epics were declared complete task-by-task, but the "merge session branch up into the epic branch + prune" lifecycle step was skipped for the final items — so the epic branches are **not** directly mergeable as-is:

- `vg_e003_text_to_audio_enhancements`: **not on origin**, local tip `a83550f` (vg_e001 base, empty of EPIC-003 work). Accepted EPIC-003 work = session stack, integrated tip **`793a80b`** (TASK-022→025, reviewed as a clean linear stack).
- `origin/vg_e002_voice_gen_hardening`: tip `19372bb`, **missing accepted TASK-021** (`6529caa`) — confirmed not an ancestor.

Each merge task therefore **consolidates accepted session branches into its epic branch before merging up** (folded into TASK-029/030 acceptance criteria). EVENT-20260621-001/002/003.

### Next

- Gemini: consolidate + merge TASK-029, submit to Claude. On acceptance, Watcher activates TASK-030 (Codex). After both land, `vg_e001_shared_config` is the assembled v0.3.0 RC; declaring/tagging the RC or cutting the release is a Thomas / Quill call.
- **onnxruntime BFC Arena OOM: deferred to a later phase per Thomas (2026-06-21, EVENT-20260621-004 / MSG-20260621-002)** — explicitly out of scope for v0.3.0; the RC proceeds on validated evidence. Other carryover items unchanged (warmup ETA refinement; legacy health-check cleanup).

## SNAPSHOT-20260621-002

Date: 2026-06-21
Owner: Watcher (Stan)
Related Task: Phase 3 / v0.3.0 RC / TASK-029 / TASK-030

### Phase 3 — First Merge Landed; One Remains

- **TASK-029 (Gemini): DONE / accepted** (REVIEW-026). EPIC-003 merged up into `vg_e001_shared_config` via `--no-ff` merge `ffc7b5e`. Trivial linear merge; `git diff ffc7b5e 793a80b` empty → integrated tree byte-identical to the accepted EPIC-003 stack; in-scope (`README.md` + `text_to_audio.py`); compiles; `--dry-run --keep-chunks` smoke clean. DISPATCH-20260621-001 Complete (EVENT-20260621-005).
- **TASK-030 (Codex): READY / dispatched** — gate satisfied; DISPATCH-20260621-002 flipped Pending → Dispatched (EVENT-20260621-006). Codex consolidates accepted TASK-021 (`6529caa`) onto `vg_e002_voice_gen_hardening` first, then merges up into the EPIC-003-integrated `vg_e001_shared_config` (`ffc7b5e`). Claude reviews. **Final Phase 3 merge — assembles the full v0.3.0 RC.**
- Blocked empty. `vg_e001_shared_config` = the v0.3.0 RC target; tip `ffc7b5e` (EPIC-001 + EPIC-003 integrated).

### Next

- Codex: claim + execute TASK-030; submit to Claude. On acceptance, the v0.3.0 RC is fully assembled — declaring/tagging the RC or cutting the release is a Thomas / Quill call.
- Carryover non-blockers unchanged: onnxruntime OOM (deferred to a later phase per EVENT-20260621-004); warmup-ETA refinement; legacy `agentbus_health.py` duplicate-ID/board-divergence cleanup.
