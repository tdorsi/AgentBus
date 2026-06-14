# Watcher Inbox — Codex CLI

Messages from **Codex CLI** to the Watcher (Stan). Only Codex CLI writes here.

Post review outcomes, task completions, and blockers using `comms/message_template.md`.
Message IDs are agent-scoped: `MSG-YYYYMMDD-CODEX-NN`. Append only; do not overwrite.
The Watcher reads this file and mirrors state into Watcher-owned files — do not write Watcher
state directly. See `comms/watcher_inbox/README.md`.
