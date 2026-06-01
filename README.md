# AgentBus

AgentBus is a markdown-based shared coordination layer for independent AI agents.
Codex CLI, Claude CLI, and local custom agents can work independently while communicating through files.

The system is intentionally simple, append-friendly, and human-readable. It is not a replacement for Git, issue tracking, source control, or project documentation.

## Directory Overview

- `sprint.md` - current sprint goals, priorities, assignments, blockers, and review checklist.
- `agent_rules.md` - operating rules for all agents.
- `tasks/` - backlog, active work, blocked work, review queue, completed tasks, and a reusable task template.
- `comms/` - shared broadcasts, agent inboxes, and a reusable message template.
- `logs/` - append-only work logs per agent.
- `decisions/` - decision log and reusable decision template.
- `reviews/` - formal review artifacts, review templates, and review findings.
- `procedures/` - standard operating procedures for update checks, startup, task claiming, and review response.
- `state/` - lightweight shared state trackers and sync snapshots.
- `artifacts/` - generated summaries, handoffs, notes, and supporting materials.

## Basic Workflow

1. Read `sprint.md`, `tasks/active.md`, `tasks/blocked.md`, and your inbox.
2. Claim one task by adding your name as owner and moving or referencing it in `tasks/active.md`.
3. Append progress to your agent log in `logs/`.
4. Communicate through inbox files or `comms/broadcast.md`.
5. Record durable decisions in `decisions/decision_log.md`.
6. Move finished work to review, then done after human or assigned review.

## Source of Truth

GitHub `origin/main` is the source of truth for tracked AgentBus coordination files. Before acting, agents must run the update-check or startup procedure and fast-forward when safe. Local ignored logs may remain local, but tracked task, comms, procedure, review, and state files should be committed and pushed when they change.

## Governance Procedures

- `procedures/check_for_updates.md` - required refresh behavior before reading local files as current.
- `procedures/agent_startup.md` - startup sequence for agents beginning a work session.
- `procedures/task_claiming.md` - rules for claiming assigned work.
- `procedures/review_response.md` - process for submitting work to review and responding to feedback.

## Review Workflow

`tasks/review.md` is the review queue. Formal review artifacts live in `reviews/` and should use `reviews/review_template.md` when possible. Review files should be committed and pushed when they are part of shared task acceptance, follow-up planning, or governance history.

Review findings that appear to be based on stale local state must be revalidated after syncing with `origin/main` before creating follow-up tasks or changing shared procedures.

## State Monitoring

- `state/agent_status.md` - current task/status summary for each participant.
- `state/sync_log.md` - append-only sync and push events.
- `state/state_snapshot.md` - concise point-in-time operating snapshots.

State monitoring process:

1. Update `state/agent_status.md` when claiming, submitting, blocking, or completing a task.
2. Append to `state/sync_log.md` after meaningful fetch, pull, commit, or push events.
3. Add a `state/state_snapshot.md` entry when governance, sprint direction, or review state changes.
4. Keep entries concise and avoid secrets, local credentials, or private runtime output.

## Status Meanings

- `Backlog` - known work not currently claimed.
- `Active` - claimed and in progress.
- `Blocked` - cannot proceed without input, dependency, or decision.
- `Review` - implementation or notes are ready for review.
- `Done` - accepted and complete.

## Safety Rules

- Do not delete history.
- Do not overwrite another agent's log or inbox entries.
- Use task IDs and message IDs.
- Keep updates concise and factual.
- Ask for human review when blocked, uncertain, or making a durable decision.

## Human Operator Role

The human operator resolves conflicts, approves important decisions, assigns priorities, reviews completed work, and decides when AgentBus structure or rules should change.

## Health Check CLI

`agentbus_health.py` is a local Python CLI that reads the AgentBus workspace and reports coordination status. It requires no external dependencies — only Python 3.7 or later from the standard library.

### Requirements

- Python 3.7+
- No packages to install

### Usage

Run from the root of the AgentBus workspace:

```
python agentbus_health.py
```

To point at a different workspace directory:

```
python agentbus_health.py --root /path/to/agentbus
```

To control how many recent decisions are shown (default is 5):

```
python agentbus_health.py --recent-decisions 3
```

### Output

```
AgentBus Health Check
Workspace: /path/to/agentbus
Tasks: 5 | Active: 1 | Blocked: 0
Messages: 4 | Need Response: 1
Decisions: 2

Active Tasks
  TASK-003: Build AgentBus Health Check CLI
    Status: Active | Owner: Codex CLI | Source: tasks/active.md

Blocked Tasks
  None

Messages Needing Response
  MSG-20260531-005: Review Needed from Codex CLI to All Agents
    Related Task: TASK-002 | Source: comms/broadcast.md

Recent Decisions
  DECISION-20260531-001: Accepted
    Date: 2026-05-31 | Owner: Thomas / Quill | Task: TASK-002

Last Update Timing
  sprint.md: 2026-05-31 12:05
  roles.md: 2026-05-31 11:45
  tasks/backlog.md: 2026-05-31 12:10
  ...
```

**Active Tasks** — tasks whose most authoritative status is Active (deduplicated across all task files).

**Blocked Tasks** — tasks whose most authoritative status is Blocked.

**Messages Needing Response** — messages with status `Request`, `Blocker`, or `Review Needed` where the `### Response` section is empty.

**Recent Decisions** — the N most recent entries from `decisions/decision_log.md`.

**Last Update Timing** — last-modified timestamps for key coordination files. Useful for spotting files that have gone stale.

### Exit Codes

| Code | Meaning |
|------|---------|
| `0` | Workspace is healthy — no blocked tasks, no messages awaiting response |
| `1` | Attention needed — blocked tasks or messages need response |
| `2` | Not a valid AgentBus workspace (missing `agent_rules.md` or `tasks/`) |

The exit code makes the CLI scriptable:

```
python agentbus_health.py && echo "All clear" || echo "Action needed"
```

### Troubleshooting

**"Not an AgentBus workspace"** — run the script from the AgentBus root directory, or pass `--root` pointing to the correct location.

**Task shown in wrong status** — the CLI resolves duplicates by file priority: `done` beats `review` beats `blocked` beats `active` beats `backlog`. If a task appears in an unexpected state, check whether it has been moved to the correct file.

**Message not flagged as needing response** — only messages with status `Request`, `Blocker`, or `Review Needed` and an empty `### Response` section are flagged. If a response has been written inline, the message is considered resolved.
