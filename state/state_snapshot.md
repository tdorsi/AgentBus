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
