# Blocked Tasks

Use this file for tasks that cannot proceed without human input, dependency resolution, or another agent's response.

Include the task ID, owner, blocker, requested action, and date blocked.

## TASK-008: Set Up Codex CLI TTS with Lori Voice

Status: Done — resolved 2026-05-31 per DECISION-20260531-003
Owner: Codex CLI

### Resolution

Thomas / Quill accepted TASK-008 as setup-complete. Runtime audio confirmation deferred to TASK-009. Do not start Lori on port 8766 while Hannah is active and GPU memory is constrained.

## TASK-009: Perform Lori Runtime Audio Validation

Status: Done - resolved 2026-06-01
Owner: Thomas / Codex CLI
Blocked: 2026-05-31

### Blocker

GPU memory is constrained while Hannah is running on port 8765 (~261 MB free). Starting a second MOSS-TTS instance for Lori on port 8766 risks disrupting Hannah.

### Requested Action

Thomas: schedule a test window when Hannah can be intentionally stopped, or when a session ends and GPU memory is available. Codex CLI will start the Lori server on port 8766, confirm audio output, and close TASK-009.

### Resolution

2026-06-01: Lori server started on port 8766. Codex confirmed `/health` returned ready, direct synthesis queued and drained, and Thomas confirmed the Lori voice test passed. Moved to `tasks/done.md`.
