# Backlog

Use this file for known work that is not currently claimed. Append new tasks using `task_template.md`.

## TASK-001: Validate AgentBus workflow

Status: Active — claimed by Claude CLI 2026-05-31
Owner: Claude CLI
Priority: High
Created: 2026-05-31
Updated: 2026-05-31
Related Files: `sprint.md`, `agent_rules.md`, `tasks/active.md`, `tasks/review.md`, `tasks/done.md`, `comms/`, `logs/`

### Goal

Validate that agents can coordinate through AgentBus using the expected task, message, log, review, and decision flow.

### Context

AgentBus has been bootstrapped as a markdown-only coordination workspace.

### Acceptance Criteria

- One agent claims this task in `tasks/active.md`.
- The agent appends at least one log entry.
- Any cross-agent or human request uses a message ID.
- The task reaches `tasks/review.md`, then `tasks/done.md` after review.

### Work Notes

### Blockers

### Review Notes

### Completion Summary

## TASK-007: Align Review Workflow Documentation

Status: Review
Owner: Codex CLI
Priority: Medium
Created: 2026-06-01
Updated: 2026-06-01
Related Files: `README.md`, `procedures/README.md`, `procedures/review_response.md`, `procedures/check_for_updates.md`, `reviews/`

### Goal

Align AgentBus documentation and procedures with the implemented review workflow.

### Context

During TASK-006 review, Claude reported a possible missing `reviews/` directory. Subsequent investigation confirmed `reviews/README.md`, `reviews/review_template.md`, and review artifacts exist. The follow-up is to make review discovery and review workflow behavior explicit.

### Acceptance Criteria

- `README.md` references the `reviews/` directory.
- `procedures/README.md` references the review workflow.
- `procedures/review_response.md` aligns with the actual reviews structure.
- `procedures/check_for_updates.md` explicitly includes review synchronization behavior.
- Review artifacts are discoverable by all agents.
- Stale-state assumptions are documented as governance guidance.

### Work Notes

- 2026-06-01: Codex CLI aligned review workflow documentation and stale-state guidance.

### Blockers

- None.

### Review Notes

- Submitted for Claude review.

### Completion Summary

## TASK-006: Establish AgentBus Rules of Engagement and State Monitoring

Status: Review
Owner: Codex CLI
Priority: High
Created: 2026-06-01
Updated: 2026-06-01
Related Files: `README.md`, `sprint.md`, `comms/broadcast.md`, `procedures/`, `state/`

### Goal

Establish clear rules of engagement and state monitoring for AgentBus agents.

### Context

Thomas requested governance procedures and state files so agents consistently treat GitHub `origin/main` as source of truth, standardize update checks, and have clear startup, task claiming, review response, and state monitoring processes.

### Acceptance Criteria

- `procedures/agent_startup.md` exists.
- `procedures/task_claiming.md` exists.
- `procedures/review_response.md` exists.
- `state/sync_log.md` exists.
- `state/state_snapshot.md` exists.
- `README.md`, `sprint.md`, and `comms/broadcast.md` are updated.
- `procedures/check_for_updates.md` is standardized around `origin/main`.
- TASK-006 is submitted for Claude review.

### Work Notes

- 2026-06-01: Codex CLI created governance procedures and state monitoring files.

### Blockers

- None.

### Review Notes

- Submitted to Claude CLI for review.

### Completion Summary

## TASK-002: Establish AgentBus POC Team Structure

Status: Review
Owner: Codex CLI
Priority: High
Created: 2026-05-31
Updated: 2026-05-31
Related Files: `roles.md`, `sprint.md`, `tasks/backlog.md`, `decisions/decision_log.md`, `comms/broadcast.md`

### Goal

Establish the planning structure for the AgentBus Health Check CLI proof of concept.

### Context

Quill requested this task in `MSG-20260531-004` after Thomas approved the next AgentBus POC. `roles.md` defines Thomas as Product Owner, Quill as Senior Analyst / PM, and Claude CLI plus Codex CLI as the Development Team.

### Acceptance Criteria

- `roles.md` exists and is referenced.
- `sprint.md` reflects the Health Check CLI POC sprint.
- `tasks/backlog.md` includes TASK-002 through TASK-005.
- `decisions/decision_log.md` records the approved role model and POC direction.
- `comms/broadcast.md` announces the POC and next steps to all agents.
- Changes are committed and pushed to `main`.

### Work Notes

- 2026-05-31: Codex CLI established the POC sprint structure and task breakdown.

### Blockers

- None.

### Review Notes

- Ready for Quill review after commit and push.

### Completion Summary

- POC planning structure created and announced.

## TASK-003: Build AgentBus Health Check CLI

Status: Review
Owner: Codex CLI
Priority: High
Created: 2026-05-31
Updated: 2026-05-31
Related Files: `sprint.md`, `roles.md`, `tasks/`, `comms/`, `decisions/`

### Goal

Build a CLI that reads the AgentBus workspace and reports coordination health.

### Context

The CLI should support the Health Check POC by summarizing active tasks, blocked tasks, messages needing response, recent decisions, and last update timing.

### Acceptance Criteria

- CLI can run locally from the AgentBus repository.
- CLI reports active tasks and blocked tasks.
- CLI reports messages that appear to need response.
- CLI reports recent decisions.
- CLI reports last update timing for key coordination files.
- CLI avoids reading ignored runtime output as primary input.

### Work Notes

- 2026-05-31: Codex CLI claimed this task after completing TASK-002.
- 2026-05-31: Codex CLI implemented `agentbus_health.py`; runtime and compile checks pass.

### Blockers

### Review Notes

- Ready for TASK-005 review by Thomas / Quill.

### Completion Summary

## TASK-004: Build README Usage Instructions for Health Check CLI

Status: Active — claimed by Claude CLI 2026-05-31
Owner: Claude CLI
Priority: Medium
Created: 2026-05-31
Updated: 2026-05-31
Related Files: `README.md`, `git_notes.md`, Health Check CLI files

### Goal

Document how to run and interpret the AgentBus Health Check CLI.

### Context

Claude CLI owns usage documentation after Codex CLI establishes the CLI behavior.

### Acceptance Criteria

- README or appropriate documentation includes CLI usage.
- Instructions explain expected output and basic troubleshooting.
- Documentation does not expose secrets or local-only runtime details.

### Work Notes

### Blockers

### Review Notes

### Completion Summary

## TASK-005: Review and Test Health Check CLI

Status: Backlog
Owner: Thomas / Quill
Priority: High
Created: 2026-05-31
Updated: 2026-05-31
Related Files: Health Check CLI files, `README.md`, `sprint.md`

### Goal

Review and test the Health Check CLI against the approved POC goals.

### Context

Thomas owns final acceptance. Quill coordinates review and synthesizes findings.

### Acceptance Criteria

- CLI output is useful for Product Owner and PM review.
- CLI handles current AgentBus files without errors.
- CLI does not require GitHub or remote access to run.
- Follow-up issues are recorded as tasks or review notes.

### Work Notes

### Blockers

### Review Notes

### Completion Summary
