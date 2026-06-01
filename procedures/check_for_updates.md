# Procedure: Check for Updates

When instructed to 'check for updates', agents must:

1. Run `git status -sb`.
2. Run `git fetch origin`.
3. Determine whether the local branch is ahead, behind, or diverged.
4. If clean and behind, fast-forward pull.
5. If local modifications exist, do not overwrite them.
6. Read:
   - sprint.md
   - agent inbox
   - comms/broadcast.md
   - tasks/active.md
   - tasks/review.md
   - reviews/
   - decisions/decision_log.md
7. Summarize:
   - commits pulled
   - new messages
   - new reviews
   - task state changes
   - actions required
8. If no action is required, report standing by.

Reading local files without first checking repository state is not considered a complete update check.
