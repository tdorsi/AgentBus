# Watcher Rules

The Watcher is a coordination role for AgentBus. It is not a developer, reviewer, or product owner. Any capable agent may perform a Watcher pass when asked by Thomas, Quill, or a future Director agent.

Watcher v1 is manual and additive. It does not run as a service, scheduler, or daemon, and it does not retire existing AgentBus procedures.

## Responsibilities

- Monitor `comms/watcher_inbox/*.md`, `comms/broadcast.md`, `tasks/*`, and `reviews/*` for state changes.
- Maintain aggregate operational state in `state/sprint_board.md`.
- Maintain Watcher-owned transition records in `watcher/event_log.md`.
- Maintain pending dispatches in `watcher/dispatch_queue.md`.
- Update `state/state_snapshot.md` when a Watcher pass changes the operating state.
- Create status-change broadcasts in `comms/broadcast.md`.
- Route work or questions to the correct inbox according to `watcher/routing_table.md`.

## Authority

The Watcher may:

- Mirror task state from `tasks/*` into `state/sprint_board.md`.
- Record state transitions in `watcher/event_log.md`.
- Add dispatch items to `watcher/dispatch_queue.md`.
- Send status-change broadcasts.
- Notify Thomas or Quill when a decision, priority call, or override is needed.
- Mark a dispatch as corrected or cancelled when the correction procedure below is followed.

The Watcher may not:

- Approve product direction.
- Accept its own implementation work.
- Change review outcomes.
- Delete task, review, decision, event, dispatch, or log history.
- Rewrite another agent's log or inbox entries.
- Move a task to done unless an accepted review, explicit Product Owner approval, or recorded decision supports the move.
- Retire or contradict existing procedures without Thomas / Quill approval.

## State Ownership

| File | Owner | Purpose |
| --- | --- | --- |
| `sprint.md` | Thomas / Quill | Strategic sprint goals and priorities, not operational task state. |
| `tasks/active.md`, `tasks/backlog.md`, `tasks/review.md` | Task owners and reviewers | Authoritative individual task records. |
| `tasks/done.md` | Watcher | Completed-task ledger; the Watcher records a task here only when an accepted review, recorded decision, or Product Owner approval supports it. |
| `reviews/*` | Reviewers | Formal review artifacts and findings. |
| `state/sprint_board.md` | Watcher | Derived aggregate board view mirrored from `tasks/*`. |
| `watcher/dispatch_queue.md` | Watcher | Pending and completed dispatch instructions. |
| `watcher/event_log.md` | Watcher | Append-only state-transition ledger. |
| `state/state_snapshot.md` | Watcher | Concise operating summaries after meaningful state changes. |
| `state/sync_log.md` | Syncing agent | Repository sync history. |
| `decisions/decision_log.md` | Thomas / Quill | Durable governance and product decisions. |
| `comms/broadcast.md` | Agents for announcements; **Watcher for status-change broadcasts** | Team announcements/review notices (agents) and Watcher operational status changes. |
| `comms/watcher_inbox/<agent>.md` | One sole writer per file (the named agent) | Inputs to the Watcher needing routing, board updates, dispatch, or state-transition processing. The Watcher reads all of them. |
| `comms/inbox_watcher.md` | Legacy (retired) | Historical shared inbox, read-only; replaced by `comms/watcher_inbox/<agent>.md`. |

`state/sprint_board.md` is derived from `tasks/*`. If the board and task files disagree, treat the relevant task entry under `tasks/*` as authoritative and correct the board in the next Watcher pass.

## Single-Writer Serialization Model

The Watcher is the **single writer** of Watcher-owned state. This prevents the concurrent-append
races and duplicate message IDs documented in `RCA.md` (RCA-20260613-001).

Core rule: **no two agents write to the same working tree or the same communication file.**

- **Watcher-owned files** (only the Watcher writes these): `state/sprint_board.md`,
  `state/state_snapshot.md`, `watcher/event_log.md`, `watcher/dispatch_queue.md`,
  `tasks/done.md`, and status-change broadcasts in `comms/broadcast.md`.
- **Agents write only to their own files**: their `tasks/active.md` task entries, `reviews/*`
  (reviewers), `logs/<agent>.md`, and their own `comms/watcher_inbox/<agent>.md`. Agents do
  **not** write Watcher-owned state directly; they route the change to the Watcher, which mirrors
  it.
- **One Watcher writer at a time.** Do not run the autonomous Watcher loop concurrently with a
  manual Watcher pass or with any agent that self-mirrors. A Watcher pass is performed by a single
  instance from a single working tree.
- **Per-agent Watcher inboxes** replace the shared `comms/inbox_watcher.md`. Each agent appends
  only to `comms/watcher_inbox/<agent>.md`, using agent-scoped message IDs
  `MSG-YYYYMMDD-<AGENT>-NN` so two agents can never collide on an ID.
- **Project repositories** (e.g., Voice_Gen): each agent uses its own working tree/clone for git
  write actions; a reviewer agent must not commit from a developer agent's working tree.

### Reviewer Boundary

A reviewer (Claude CLI) **may write**: `reviews/*`, the review outcome in `tasks/review.md`,
`logs/claude.md`, `comms/watcher_inbox/claude.md`, and `comms/inbox_codex.md` (to ask the
developer a direct question).

A reviewer **may not write**: `state/sprint_board.md`, `watcher/event_log.md`,
`watcher/dispatch_queue.md`, `state/state_snapshot.md`, `tasks/done.md`, or status-change
broadcasts. The reviewer records its outcome and routes it to the Watcher inbox; the Watcher
mirrors the board, logs the event, and broadcasts.

### Watcher Boundary

The Watcher **may write** the Watcher-owned files above. The Watcher **may not**: review code
quality, approve its own work, modify review outcomes, or perform project implementation.

## Broadcast Ownership

Agents continue using `comms/broadcast.md` for team announcements, review-ready notices, and broad coordination messages.

The Watcher owns broadcasts that announce operational status changes, such as a task moving to done, a task becoming blocked, a dependent task becoming ready, a dispatch being created, or an epic completing.

## Correction Procedure

Watcher history is append-only. Do not delete incorrect events or dispatches.

To correct a bad dispatch:

1. Mark the dispatch status as `Corrected` or `Cancelled` in `watcher/dispatch_queue.md`.
2. Add a correction note under the dispatch explaining the original mistake and the replacement action.
3. Add a correction event to `watcher/event_log.md` that references the dispatch ID.
4. If the bad dispatch was broadcast, append a follow-up status-change broadcast with the corrected instruction.
5. Escalate to Thomas / Quill when the correction changes ownership, priority, or task acceptance.

To correct a bad event-log entry:

1. Leave the original event in place.
2. Add a new event with type `Correction`.
3. Reference the incorrect event ID and explain the corrected state.
4. Update `state/sprint_board.md` if the aggregate board was affected.
5. Broadcast the correction only if another agent may act on the wrong state.

Thomas / Quill may override any Watcher action. Record overrides in `watcher/event_log.md` and, when durable, in `decisions/decision_log.md`.

## Operating Procedures

### Review Accepted

Trigger: a review artifact or message records `Result: Accepted`.

Watcher actions:

1. Confirm the accepted review maps to the correct task.
2. Confirm the task owner and reviewer are recorded in `tasks/*`.
3. Mirror the task state to `Done` or `Review complete - accepted` in `state/sprint_board.md`.
4. Record the transition in `watcher/event_log.md`.
5. Check whether the accepted task unlocks dependent work.
6. Add any newly available work to `watcher/dispatch_queue.md`.
7. Append a status-change broadcast if team action is needed.

### Blocked Task

Trigger: a task status changes to `Blocked` or an agent reports a blocker to the Watcher inbox.

Watcher actions:

1. Mirror the blocked state in `state/sprint_board.md`.
2. Record the blocker in `watcher/event_log.md`.
3. Route decision-needed blockers to Thomas / Quill.
4. Route agent-specific questions to the appropriate inbox.
5. Broadcast only when the blocker changes team state or affects another agent.

### New Task Activation

Trigger: Thomas / Quill authorizes work, a dependency is accepted, or a dispatch creates a ready task.

Watcher actions:

1. Confirm the task exists in `tasks/backlog.md` or create a dispatch requesting task creation by the assigned owner.
2. Mirror the task under `Ready` or `In Progress` in `state/sprint_board.md`.
3. Add a dispatch entry for the assigned agent.
4. Record the activation in `watcher/event_log.md`.
5. Broadcast the status change if the assigned agent or reviewer needs to act.

### Broadcast Creation

Trigger: a Watcher-owned status change occurs.

Watcher actions:

1. Use the next available message ID.
2. Set `From: Watcher`.
3. Reference the related task, epic, event, or dispatch.
4. State the operational change and requested action.
5. Avoid duplicating developer review notes or implementation details unless they are needed for routing.

### EPIC Completion

Trigger: all tasks in an epic are accepted or done.

Watcher actions:

1. Record the epic completion in `watcher/event_log.md`.
2. Mirror completed epic state in `state/sprint_board.md`.
3. Check for dependent epics or planning tasks.
4. Add dispatches for newly available work.
5. Broadcast the transition.

## Worked Examples

### Accepted Review

Input: Claude writes `Result: Accepted` for `TASK-014`.

Watcher output: update `state/sprint_board.md` to show `TASK-014` done, append an event for the accepted review, add a dispatch for the next ready task, and broadcast the status change.

### Blocked Task

Input: Codex reports `TASK-020` is blocked by missing approval.

Watcher output: mirror `TASK-020` under `Blocked`, add a blocker event, route a decision request to Thomas / Quill, and broadcast only if another agent is waiting on the decision.

### New Task Activation

Input: Thomas authorizes `TASK-015`.

Watcher output: mirror `TASK-015` under `Ready`, add a dispatch assigning Codex CLI, record the activation event, and broadcast that TASK-015 is ready for Codex.

### Broadcast Creation

Input: A dispatch assigns Codex to implement TASK-015.

Watcher output: append a `Watcher` broadcast that references the dispatch ID, states Codex is assigned, and names Claude CLI as reviewer.
