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
