# REVIEW-017

Reviewer: Claude CLI
Date: 2026-06-14
Related Task: TASK-026 (Implement AgentBus Communication Isolation — residual code + infra)
Artifact: AgentBus commit `207e2e9 [agentbus][TASK-026] Add communication isolation health checks` (submission `8fb32f5`)
Status: Accepted with Follow-ups

## Summary

TASK-026 completes the code + infrastructure + cutover for the communication-isolation model (RCA-20260613-001 / DECISION-20260614-001). The health-check detection, per-agent worktree isolation, and agent-facing doc cutover are all implemented correctly and verified by running the tool and inspecting the worktrees. One live residual remains — an active dispatch still routes an agent to the retired shared inbox — but it lives in a Watcher-owned file outside Codex's writable scope, so it is routed to the Watcher as a follow-up rather than bounced to Codex.

## Verified (exercised, not just claimed)

**Duplicate-ID detection** ✓ — `MSG_RE` widened to agent-scoped IDs (`MSG-\d{8}-(?:[A-Z]+-)?[A-Z]?\d+`, matches `MSG-20260614-CLAUDE-01` and legacy `…-W011`); added `EVENT_RE`/`DISPATCH_RE`. `parse_ids()` scans `comms/*`, `comms/watcher_inbox/*`, and `watcher/*`; `duplicate_ids()` groups occurrences. Running `agentbus_health.py` surfaced **5 duplicate IDs** (legacy cross-file collisions) with file:line — works as intended.

**Board-divergence detection** ✓ — `parse_board()` reads the `sprint_board.md` summary table; `board_divergences()` compares status/owner/presence against the merged `tasks/*` state with sensible `normalize_status()` bucketing. Run surfaced **7 divergences** (legacy). Works.

**Exit code** ✓ — `agentbus_health.py` returns **exit 1** when issues are present (verified directly), so it is usable as a pre-pass gate per RCA P7.

**Worktree isolation** ✓ — `git worktree list` on Voice_Gen confirms four separate trees: canonical `D:/Development/Voice_Gen`, plus `Sandbox/Voice_Gen_claude` (detached, reviewer), `Sandbox/Voice_Gen_codex` (on `vg_e002_voice_gen_hardening__codex__TASK-020`), and `Sandbox/Voice_Gen_gemini` (on `vg_e003_…__gemini__TASK-022`). Per-agent + per-task-branch convention from AGENTS.md is in place; no shared checkout for git writes.

**Cutover (agent-facing)** ✓ — `watcher/watcher_rules.md` Responsibilities now monitors `comms/watcher_inbox/*.md`; `watcher/watcher_seed_prompt.md` reads per-agent inboxes; README updated; `agentbus_health.py` key-files list includes the per-agent inboxes. Codex startup pointer `C:\Users\thoma\.codex\AGENTS.md` added (outside repo; claimed). `py_compile` clean.

## Follow-up (Watcher-owned — not Codex's to fix)

**FU1 — One active dispatch still routes to the retired inbox.** `DISPATCH-20260613-005` in `watcher/dispatch_queue.md` (Status: **Dispatched**, live) instructs Gemini: *"Submit each task to Claude CLI for review; route outcomes to `comms/inbox_watcher.md`."* That is the retired shared inbox, which technically violates criterion #3 ("no agent is instructed to append to the retired shared `comms/inbox_watcher.md`"). The fix is a one-word path change to `comms/watcher_inbox/gemini.md`, but `dispatch_queue.md` is Watcher-owned state, so the **Watcher** must make it — Codex (and the reviewer) may not write that file under the boundary. Routed to the Watcher.

All other `inbox_watcher.md` references are correctly historical: `watcher/event_log.md` `Source:` lines (append-only history) and descriptive "replaced/retired" mentions in `watcher_rules.md` / `watcher_inbox/README.md`.

## Observations (non-blocking)

- Codex's verification ("cutover scan … shows only retired/history references") missed the live `DISPATCH-20260613-005` routing line — its scan covered instruction docs but not active Watcher dispatches. Minor process gap.
- **Optional enhancement:** extend the new `agentbus_health.py` cutover awareness to flag *active* (non-history) references to `comms/inbox_watcher.md` in `watcher/dispatch_queue.md` / routing instructions. That would have caught FU1 automatically and closes the detection gap RCA P7 targets.

## Acceptance Recommendation

**Accepted with Follow-ups.** Codex's owned deliverables (duplicate-ID + board-divergence health checks with exit-1 gating, per-agent worktree isolation, agent-facing doc/seed/README cutover, Codex startup pointer) meet the acceptance criteria and are verified working. The single residual (FU1) is in Watcher-owned state and is routed to the Watcher to correct on its next pass. With FU1 fixed, the cutover is fully consistent. The communication-isolation model is functionally in effect.
