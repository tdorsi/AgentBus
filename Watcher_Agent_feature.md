You are working in the AgentBus repository.

Objective:
Implement the AgentBus Watcher architecture and supporting governance documents.

## Background

AgentBus currently supports:

* Thomas (Product Owner)
* Quill (Senior Analyst / PM)
* Codex CLI (Developer)
* Claude CLI (Developer / Reviewer)

The current workflow requires manual intervention to tell agents to check for updates and determine what work should begin next.

We want to introduce a dedicated Watcher role that acts as the coordination hub.

The Watcher is NOT a developer.

The Watcher is responsible for:

* Monitoring AgentBus communications
* Maintaining sprint state
* Routing messages
* Dispatching work
* Updating task status
* Detecting completed reviews
* Activating dependent tasks

The Watcher becomes the authoritative state-transition engine.

## Architecture

Implement the following model:

```
                Thomas / Quill
                     │
                     ▼
                  Watcher
        ┌────────────┼────────────┐
        ▼            ▼            ▼
   Codex Inbox   Claude Inbox   Broadcast

        ▲                        ▲
        └────── Watcher Inbox ───┘
```

## Rules

1. Codex and Claude report outcomes to the Watcher.

2. The Watcher updates:

   * Sprint board
   * Task status
   * Dispatch queue
   * State snapshot

3. Codex and Claude may:

   * Write logs
   * Write deliverables
   * Send direct questions to another agent inbox
   * Send status updates to Watcher inbox

4. Codex and Claude should NOT directly maintain sprint state.

5. The repository remains the source of truth.

## Required Repository Changes

Create:

watcher/
watcher_rules.md
routing_table.md
dispatch_queue.md
event_log.md

comms/
inbox_watcher.md

state/
sprint_board.md

## Required Documents

1. watcher_rules.md

Define:

* Watcher responsibilities
* Watcher authority
* Allowed actions
* Forbidden actions
* State ownership

Include examples for:

* Accepted review
* Blocked task
* New task activation
* Broadcast creation

2. routing_table.md

Document message routing.

Examples:

Review outcome
→ Watcher inbox

Task completion
→ Watcher inbox

Question for Codex
→ inbox_codex.md

Question for Claude
→ inbox_claude.md

Team-wide announcement
→ broadcast.md

3. dispatch_queue.md

Create template structure.

Purpose:

Queue work waiting for dispatch.

Include:

* Dispatch ID
* Trigger
* Assigned Agent
* Action
* Status

4. event_log.md

Create event ledger.

Purpose:

Record significant state transitions.

Examples:

TASK accepted
TASK blocked
TASK completed
EPIC activated
Review completed

5. sprint_board.md

Create a single sprint status board.

Suggested sections:

Backlog
Ready
In Progress
Review
Blocked
Done

Include ownership and status columns.

## Watcher Operating Procedures

Document the following workflow:

Review Accepted

Trigger:
Review outcome = Accepted

Watcher Actions:

1. Update task state.
2. Move task to Done.
3. Update sprint board.
4. Check dependent tasks.
5. Dispatch newly available work.
6. Broadcast state change.

Blocked Task

Trigger:
Task status = Blocked

Watcher Actions:

1. Update sprint board.
2. Record blocker in event log.
3. Notify Thomas / Quill if decision required.

EPIC Completion

Trigger:
All Epic tasks complete.

Watcher Actions:

1. Record Epic completion.
2. Activate dependent Epic.
3. Dispatch next work items.
4. Broadcast transition.

## README Updates

Update README to describe:

* Watcher role
* Message routing model
* Sprint board ownership
* Dispatch workflow

## Acceptance Criteria

* All files created.
* Documentation is internally consistent.
* Roles and responsibilities are clearly defined.
* Message routing is unambiguous.
* Sprint ownership is assigned to Watcher.
* Watcher can be used by Claude, Codex, or a future local Director agent.
* Existing AgentBus governance remains compatible.

## Commit Format

Use AgentBus commit policy:

[v0.3.0][agentbus][TASK-015] Implement watcher governance model

Post completion summary to:
comms/broadcast.md

Post any review requests to:
comms/inbox_watcher.md