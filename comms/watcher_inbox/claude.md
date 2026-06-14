# Watcher Inbox — Claude CLI

Messages from **Claude CLI** (reviewer) to the Watcher (Stan). Only Claude CLI writes here.

Post review outcomes (Accepted / Accepted with Changes / Changes Requested), completions, and
blockers using `comms/message_template.md`. Message IDs are agent-scoped:
`MSG-YYYYMMDD-CLAUDE-NN`. Append only; do not overwrite.

As reviewer, record the outcome in `tasks/review.md` + `reviews/REVIEW-NNN.md` and post it here.
Do **not** write `state/sprint_board.md`, `watcher/event_log.md`, `watcher/dispatch_queue.md`,
`state/state_snapshot.md`, `tasks/done.md`, or status broadcasts — the Watcher owns those.
See `comms/watcher_inbox/README.md`.
