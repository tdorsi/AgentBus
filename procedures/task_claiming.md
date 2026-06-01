# Procedure: Task Claiming

Use this process when starting a task.

## Rules

- Claim only tasks assigned to your role.
- Claim only one active task at a time unless Thomas or Quill explicitly approves otherwise.
- Do not claim tasks assigned to another agent.
- If assignment is unclear, message Quill before making changes.
- Use task IDs in every related update.

## Claim Sequence

1. Complete the agent startup procedure.
2. Confirm the task is assigned to you in `sprint.md`, `tasks/backlog.md`, or an inbox message.
3. Add or update the task entry in `tasks/active.md`.
4. Update the task status in `tasks/backlog.md` if the task appears there.
5. Update your section in `state/agent_status.md`.
6. Broadcast only if other agents need to know immediately.
7. Commit and push claim-state changes when they affect tracked coordination files.

## Blocked Claim

If the task appears assigned to multiple owners or conflicts with current sprint direction:

- Do not start implementation.
- Add a blocker note to `tasks/blocked.md`.
- Send Quill a message with the conflicting task IDs and proposed next action.
