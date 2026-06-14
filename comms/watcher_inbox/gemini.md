# Watcher Inbox — Gemini CLI

Messages from **Gemini CLI** to the Watcher (Stan). Only Gemini CLI writes here.

Post review outcomes, task completions, and blockers using `comms/message_template.md`.
Message IDs are agent-scoped: `MSG-YYYYMMDD-GEMINI-NN`. Append only; do not overwrite.
The Watcher reads this file and mirrors state into Watcher-owned files — do not write Watcher
state directly. See `comms/watcher_inbox/README.md`.
