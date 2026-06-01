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
4. If the review says `Accepted`, move or mark the task as done only if you are assigned to do so.
5. If the review says `Accepted with Follow-ups`, do not expand scope silently. Create or request follow-up tasks.
6. If changes are requested, claim only the assigned follow-up work.
7. If feedback is unclear or conflicts with ownership, message Quill.

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
