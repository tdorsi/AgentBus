# Procedure: Check for Updates

`origin/main` is the source of truth. Reading local files before checking repository state is not considered a complete update check.

When instructed to "check for updates", agents must:

1. Run `git status -sb`.
2. Run `git fetch origin`.
3. Determine whether the local branch is synced, ahead, behind, or diverged.
4. If tracked files are clean and local is behind, run `git pull --ff-only origin main`.
5. If tracked local modifications exist, do not overwrite them. Summarize the local changes and message Quill if guidance is needed.
6. If branches diverged, do not merge or rebase without human or Quill guidance.
7. Read:
   - `sprint.md`
   - `state/agent_status.md`
   - your agent inbox
   - `comms/broadcast.md`
   - `tasks/active.md`
   - `tasks/blocked.md`
   - `tasks/review.md`
   - `reviews/`
   - `decisions/decision_log.md`
8. Review synchronization behavior:
   - Confirm `reviews/README.md` and `reviews/review_template.md` are present when review workflow questions arise.
   - Read new or changed `reviews/REVIEW-*.md` files.
   - Revalidate review findings that claim missing files, missing directories, or stale state after fetch/pull.
   - Do not create follow-up tasks from stale-state findings until synced `origin/main` confirms the issue.
9. Append a concise entry to `state/sync_log.md` when the update check changes working context or pulls commits.
10. Summarize:
   - commits pulled
   - new messages
   - new reviews
   - task state changes
   - sync state
   - actions required
11. If no action is required, report standing by.
