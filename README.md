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
