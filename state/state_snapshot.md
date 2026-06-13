# State Snapshot

Use this file for concise, human-readable snapshots of AgentBus operating state.

## SNAPSHOT-20260601-001

Date: 2026-06-01
Owner: Codex CLI
Related Task: TASK-006

### Source of Truth

`origin/main` is the source of truth. Local agents must fetch before reading local files as authoritative.

### Current Governance State

- Startup, task claiming, review response, and update-check procedures are tracked under `procedures/`.
- Agent task visibility is tracked in `state/agent_status.md`.
- Sync events are tracked in `state/sync_log.md`.
- Point-in-time state summaries are tracked in this file.

### Current Review State

- TASK-003 has Quill review: accepted with follow-ups.
- TASK-004 is submitted for review by Claude CLI.
- TASK-006 is submitted to Claude CLI for review after implementation.

## SNAPSHOT-20260601-002

Date: 2026-06-01
Owner: Codex CLI
Related Task: TASK-007

### Review Workflow State

- `reviews/README.md` exists.
- `reviews/review_template.md` exists.
- `reviews/REVIEW-001.md` exists.
- `reviews/REVIEW-002.md` exists locally and is being added to shared history.
- `tasks/review.md` is the review queue.
- Procedures now require stale-state findings to be revalidated after syncing with `origin/main`.

## SNAPSHOT-20260601-003

Date: 2026-06-01
Owner: Codex CLI
Related Task: TASK-008

### TTS Setup State

- Claude CLI Hannah server remains assigned to port 8765.
- Codex CLI Lori server is being configured for port 8766.
- MOSS-TTS server defaults must continue to load Hannah unless CLI args override them.
- Runtime acceptance depends on hook trust/reload and Thomas confirming Lori audio.

## SNAPSHOT-20260601-004

Date: 2026-06-01
Owner: Codex CLI
Related Task: EPIC-001 / TASK-011 through TASK-014

### Voice_Gen v0.3.0 Planning State

- Voice_Gen v0.3.0 planning documents are tracked under `artifacts/Planning/`.
- `procedures/branching_strategy.md` defines Epic branches and the `vg_e001_shared_config` branch for EPIC-001.
- EPIC-001 has been split into TASK-011 through TASK-014.
- TASK-011 is active with Codex CLI implementing and Claude CLI assigned to architecture review.

### Attention Items

- Thomas / Quill should confirm the TASK-011 through TASK-014 breakdown matches intended EPIC-001 scope.
- Claude CLI should review TASK-011 architecture notes once Codex posts them.

## SNAPSHOT-20260613-001

Date: 2026-06-13
Owner: Codex CLI
Related Task: TASK-015

### Watcher Governance State

- Thomas approved the Watcher Governance Proposal v1 and authorized TASK-015.
- The Watcher is a manually activated role, not a service.
- Watcher v1 is additive; existing task, review, and update procedures remain valid.
- Codex CLI owns implementation and Claude CLI owns review.
- `state/sprint_board.md` is Watcher-owned aggregate state derived from `tasks/*`.
- `watcher/dispatch_queue.md` and `watcher/event_log.md` are Watcher-owned operational state.

### Current Validation Cycle

- TASK-014 accepted review is used as the Review Accepted trigger.
- TASK-015 is dispatched to Codex CLI through `DISPATCH-20260613-001`.
- Events are recorded in `watcher/event_log.md`.
- The status-change broadcast is recorded as `MSG-20260613-003`.

## SNAPSHOT-20260613-002

Date: 2026-06-13
Owner: Watcher pass performed by Codex CLI
Related Task: TASK-015

### Watcher Review Closure State

- Claude CLI accepted TASK-015 in `reviews/REVIEW-010.md`.
- TASK-015 is done and recorded in `tasks/done.md`.
- `state/sprint_board.md` mirrors TASK-015 as Done.
- `watcher/event_log.md` records the accepted-review closure as EVENT-20260613-006.
- `comms/broadcast.md` records the completion status change as MSG-20260613-005.
- No dependent work was dispatched.

## SNAPSHOT-20260613-003

Date: 2026-06-13
Owner: Watcher (Stan)
Related Task: EPIC-002

### Voice_Gen Development Resumed

- EPIC-001 (Shared Configuration Framework) is complete; v0.3.0 development has resumed.
- Thomas authorized EPIC-002 (Voice_Gen Hardening, Phase 2) with Codex CLI as owner and Claude CLI as reviewer.
- Branch `vg_e002_voice_gen_hardening` is to be created from `vg_e001_shared_config`.
- DISPATCH-20260613-002 assigns the claim/branch/breakdown work to Codex CLI; EVENT-20260613-007/008 record the activation and dispatch.

### Workflow Gates (EPIC-002)

1. Codex proposes the task breakdown when claiming.
2. Claude reviews the breakdown and posts notable concerns.
3. Watcher creates the resulting tasks (TASK-016+) on `state/sprint_board.md` after Claude's review.
4. Codex begins implementation once the tasks exist.

### Open With Thomas (not yet dispatched)

- EPIC-003 scope (thin after EPIC-001 absorbed items 4a/4c/4d).
- Parallel-execution model with one implementer (Codex) and one reviewer (Claude).
- Overall epic-scoping ownership.
