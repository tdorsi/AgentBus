# Procedure: Review Response

Use this process when work is ready for review or when review feedback is received.

## Submitting for Review

1. Confirm the task acceptance criteria are satisfied.
2. Run relevant local checks.
3. Update the task status to `Review`.
4. Add a concise entry to `tasks/review.md`.
5. If a formal review artifact is expected, direct reviewers to `reviews/README.md` and `reviews/review_template.md`.
6. Send a message to the assigned reviewer inbox or `comms/broadcast.md`.
7. Commit and push the tracked review submission files to `origin/main`.

## Responding to Review

1. Synchronize with `origin/main` before treating review state as authoritative.
2. Read `tasks/review.md`, review artifacts in `reviews/`, and any related inbox messages.
3. If a review claims a file or directory is missing, verify after sync before creating a follow-up task.
4. The reviewer records the outcome in `tasks/review.md` + `reviews/REVIEW-NNN.md` and routes it to the Watcher (see Reviewer Boundary). The **Watcher** moves the task to done and mirrors the board — the reviewer does not.
5. If the review says `Accepted with Follow-ups`, do not expand scope silently. Create or request follow-up tasks.
6. If changes are requested, claim only the assigned follow-up work.
7. If feedback is unclear or conflicts with ownership, message Quill.

## Reviewer Boundary

To preserve single-writer Watcher state (see `watcher/watcher_rules.md` and `RCA.md`,
RCA-20260613-001), a reviewer records and **routes** the outcome but does not write Watcher-owned
state.

A reviewer **may write**: `reviews/*`, the review outcome in `tasks/review.md`, `logs/claude.md`,
its own `comms/watcher_inbox/<reviewer>.md`, and `comms/inbox_<developer>.md` for a direct
question.

A reviewer **may not write**: `state/sprint_board.md`, `watcher/event_log.md`,
`watcher/dispatch_queue.md`, `state/state_snapshot.md`, `tasks/done.md`, or status-change
broadcasts in `comms/broadcast.md`. Post the outcome to `comms/watcher_inbox/<reviewer>.md`
(agent-scoped ID `MSG-YYYYMMDD-<AGENT>-NN`); the Watcher mirrors the board, logs the event,
records done, and broadcasts.

## Review Artifact Discovery

- Review queue: `tasks/review.md`
- Review directory overview: `reviews/README.md`
- Review template: `reviews/review_template.md`
- Review artifact naming: `reviews/REVIEW-###.md`
- Shared review artifacts should be committed and pushed to `origin/main`.

## Review Status Meanings

- `Accepted` - task can move to done.
- `Accepted with Follow-ups` - current scope is accepted; new work should become new tasks.
- `Changes Requested` - assigned owner should revise.
- `Blocked` - reviewer cannot complete review without more input.
