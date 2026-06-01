# Blocked Tasks

Use this file for tasks that cannot proceed without human input, dependency resolution, or another agent's response.

Include the task ID, owner, blocker, requested action, and date blocked.

## TASK-008: Set Up Codex CLI TTS with Lori Voice

Status: Blocked
Owner: Codex CLI
Blocked: 2026-06-01

### Blocker

Implementation files are in place, but live Lori audio confirmation requires starting a second MOSS-TTS server on port 8766. Hannah is currently healthy on port 8765 and GPU memory is nearly full with only about 261 MB free.

Starting Lori now may fail or disrupt Hannah, which violates the acceptance criterion that Claude CLI's Hannah server remains unaffected.

### Requested Action

Quill / Thomas: confirm whether to stop Hannah temporarily for Lori testing, test Lori later after freeing GPU memory, or accept setup completion pending manual runtime confirmation.
