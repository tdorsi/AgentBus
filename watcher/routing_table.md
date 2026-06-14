# Watcher Routing Table

Use this table when deciding where a message belongs. The Watcher routes operational state changes; direct collaboration can still use agent inboxes.

Operational inputs to the Watcher go to the sender's **own** per-agent file in
`comms/watcher_inbox/` (`codex.md`, `claude.md`, `gemini.md`, `quill.md`) using agent-scoped IDs
`MSG-YYYYMMDD-<AGENT>-NN`. The Watcher reads all of them. The legacy shared
`comms/inbox_watcher.md` is retired (history only). See `comms/watcher_inbox/README.md`.

| Input | Destination | Owner | Notes |
| --- | --- | --- | --- |
| Review outcome | `comms/watcher_inbox/<reviewer>.md` | Reviewer | Watcher mirrors accepted, blocked, or changes-requested state. Reviewer does not write Watcher state. |
| Task completion notice | `comms/watcher_inbox/<owner>.md` | Task owner | Watcher updates aggregate board and dispatches follow-up work. |
| Task blocker | `comms/watcher_inbox/<owner>.md` | Task owner | Watcher records blocker and routes decision needs. |
| Question for Codex CLI | `comms/inbox_codex.md` | Sender | Use for implementation-specific questions. |
| Question for Claude CLI | `comms/inbox_claude.md` | Sender | Use for review or Claude-owned work questions. |
| Question for Gemini CLI | `comms/inbox_gemini.md` | Sender | Use for EPIC-003 / Gemini-owned implementation questions. |
| Question for Thomas / Quill | `comms/broadcast.md` or directed human channel | Sender or Watcher | Use broadcast only when the whole team needs visibility. |
| Team announcement | `comms/broadcast.md` | Any agent | Includes review-ready notices and broad coordination updates. |
| Watcher status change | `comms/broadcast.md` | Watcher | Includes dispatches, blocker state, accepted-review transitions, and epic completion. |
| Durable decision | `decisions/decision_log.md` | Thomas / Quill | Watcher may reference decisions but does not create them without authority. |
| Sync event | `state/sync_log.md` | Syncing agent | Not a Watcher routing concern unless sync changes operating state. |

## Routing Examples

### Review Outcome

Claude accepts `TASK-015`.

Route to `comms/watcher_inbox/claude.md` with the review artifact path. The Watcher updates `state/sprint_board.md`, appends `watcher/event_log.md`, checks dependent work, and broadcasts the state change. Claude does not write the board, event log, or broadcast itself.

### Task Completion

Codex finishes implementation for `TASK-015`.

Route to `comms/watcher_inbox/codex.md` and `tasks/review.md`. The Watcher keeps the board and dispatch queue current; Claude reviews from the review queue.

### Blocker

Codex cannot proceed because a decision is missing.

Route to `comms/watcher_inbox/codex.md`. The Watcher records the blocked state and sends the decision request to Thomas / Quill.

### Direct Agent Question

Codex needs Claude to clarify a review comment.

Route to `comms/inbox_claude.md`. The Watcher does not need to process direct implementation discussion unless task state changes.

### Team Announcement

Codex submits work for review.

Route to `comms/broadcast.md` or the assigned reviewer inbox. The Watcher owns only the follow-up status-change broadcast after the operational state changes.
