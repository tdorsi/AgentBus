# Watcher Inbox (per-agent)

Each agent writes **only to its own file** in this directory. The Watcher (Stan) reads all of
them and mirrors state into Watcher-owned files. This replaces the single shared
`comms/inbox_watcher.md`, which caused concurrent-append ID collisions (see `RCA.md`,
RCA-20260613-001).

| File | Sole writer | Use for |
| --- | --- | --- |
| `codex.md` | Codex CLI | review outcomes, task completions, blockers |
| `claude.md` | Claude CLI (reviewer) | review outcomes, completions, blockers |
| `gemini.md` | Gemini CLI | review outcomes, task completions, blockers |
| `quill.md` | Quill / Thomas | direction, priority calls, decisions to route |

## Rules

- Write only to your own file. Never edit another agent's file or Watcher-owned state.
- Append using `comms/message_template.md`; never overwrite prior messages.
- **Message IDs are agent-scoped**: `MSG-YYYYMMDD-<AGENT>-NN` (e.g. `MSG-20260614-CODEX-01`).
  Per-file numbering means two agents can never collide on an ID.
- The Watcher records its action in the message's `### Response` section and mirrors the change
  into `state/sprint_board.md`, `watcher/event_log.md`, `watcher/dispatch_queue.md`,
  `state/state_snapshot.md`, and status-change broadcasts. Agents do **not** write those files.
