# Done Tasks

Use this file for tasks that have been reviewed and accepted.

Include the task ID, owner, completion date, and concise completion summary.

## TASK-015: Implement Watcher Governance Model v1

Status: Done
Owner: Codex CLI
Completed: 2026-06-13
Approved by: Claude CLI (`reviews/REVIEW-010.md`)

### Completion Summary

Implemented the additive, role-based AgentBus Watcher Governance Model v1. Added Watcher rules, routing table, dispatch queue, event log, Watcher inbox, and sprint board; updated README and AgentBus state records; documented correction procedure, broadcast ownership, and state ownership; recorded and reviewed the required end-to-end validation cycle. Claude CLI accepted all acceptance criteria and REVIEW-009 conditions C1-C5.

## TASK-009: Perform Lori Runtime Audio Validation

Status: Done
Owner: Thomas / Codex CLI
Completed: 2026-06-01
Approved by: Thomas

### Completion Summary

Lori MOSS-TTS server started successfully on port 8766. Codex verified the health endpoint returned ready, queued a direct synthesis request, confirmed the queue drained, and Thomas confirmed the Lori voice test passed. Runtime validation for TASK-008 is complete.

## TASK-008: Set Up Codex CLI TTS with Lori Voice

Status: Done
Owner: Codex CLI
Completed: 2026-05-31
Approved by: Thomas / Quill (DECISION-20260531-003)

### Completion Summary

All implementation files in place: `tts_server_win.py` updated to accept `--config`, `--reference`, and `--port` CLI args; `lori.yaml` created; Lori server launcher created; Codex CLI TTS hook script created and registered. Live audio confirmation deferred to TASK-009 — runtime validation blocked pending available GPU memory or a planned test window. Hannah server on port 8765 unaffected.

## TASK-001: Validate AgentBus workflow

Status: Done
Owner: Claude CLI
Completed: 2026-05-31
Approved by: Human operator

### Completion Summary

Full AgentBus task lifecycle validated end-to-end. Claude CLI claimed the task, broadcast to all agents, executed a cross-agent message round-trip with Codex CLI, logged all work, and submitted for review. All acceptance criteria met. Both agents followed message ID, log, and inbox conventions correctly on first run.
