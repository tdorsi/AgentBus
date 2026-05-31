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
- `artifacts/` - generated summaries, handoffs, notes, and supporting materials.

## Basic Workflow

1. Read `sprint.md`, `tasks/active.md`, `tasks/blocked.md`, and your inbox.
2. Claim one task by adding your name as owner and moving or referencing it in `tasks/active.md`.
3. Append progress to your agent log in `logs/`.
4. Communicate through inbox files or `comms/broadcast.md`.
5. Record durable decisions in `decisions/decision_log.md`.
6. Move finished work to review, then done after human or assigned review.

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
