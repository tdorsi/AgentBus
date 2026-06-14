# GEMINI.md

This file provides foundational mandates and operational guidance for Gemini CLI when working within the **AgentBus** workspace. It bridges the gap between general agent behavior and the project-specific coordination rules.

## Core Mandates

1. **Source of Truth:** `origin/main` is the absolute source of truth. Always perform the [Startup Sequence](#startup-sequence) at the beginning of a session.
2. **Coordination Model:** Operate as a member of the **Development Team** (or as **Quill/Stan** if explicitly assigned). All status changes must be reflected in AgentBus files.
3. **Commit Integrity:** Strictly follow the [Commit Message Policy](#commit-message-policy). Never commit without including Release, Epic, and Task IDs.
4. **Non-Destructive Operations:** Never delete log history or overwrite other agents' inbox/log entries. Append only.

## Startup Sequence

Before acting, you MUST:
1. Synchronize with the repository: `git status -sb && git fetch origin`.
2. Fast-forward if safe: `git pull --ff-only origin main`.
3. Read the authoritative state files in order:
    - `D:\Development\AGENTS.md` — CLI-agnostic workspace grounding (replaces `CLAUDE.md` as the cross-agent anchor).
    - `agent_rules.md`
    - `roles.md`
    - `sprint.md`
    - `state/agent_status.md`
    - `tasks/active.md`
    - Your Watcher inbox `comms/watcher_inbox/gemini.md` and your direct inbox `comms/inbox_gemini.md`.
    - `comms/broadcast.md`

## Memory & Session Snapshots

This project uses a structured memory system to maintain context across sessions.

- **Storage Root:** `D:\Memory\Gemini\` — your platform's own area under `D:\Memory\`. Do not write into another platform's memory (e.g. `D:\Memory\Claude\`).
- **Session Snapshots:** At the end of every significant work session, you must save a context snapshot to `D:\Memory\Gemini\Snapshots\`.
- **Naming Convention:** `YYYYMMDD_<topic>.md` (e.g., `20260613_Watcher_Implementation.md`).
- **Snapshot Content:** Summarize what was built, key decisions made (with IDs), and the current operational state/next steps.

## Commit Message Policy

All commits must follow the standard format:
`[Release][Epic/Branch][TASK-###] Short description`

**Examples:**
- `[v0.3.0][vg_e002][TASK-016] Add overwrite protection`
- `[agentbus][TASK-015] Implement Watcher Governance Model v1`

## Referenced Grounding

For detailed procedures and architecture, refer to:
- `D:\Development\AGENTS.md` - CLI-agnostic workspace grounding: coding behavior, environment notes (CUDA, TTS), and per-project guidance. Supersedes `CLAUDE.md` as the cross-agent reference (`CLAUDE.md` remains Claude Code's own platform file).
- `README.md` - Overall AgentBus architecture and directory map.
- `procedures/` - Detailed SOPs for task claiming, updates, and reviews.
- `roles.md` - Authoritative role assignments.
- `watcher/watcher_rules.md` - Rules for the Watcher/Stan role.

## Communication Protocols

- **Single-writer isolation (DECISION-20260614-001):** Write only your own files. Do **not** write Watcher-owned state — `state/sprint_board.md`, `state/state_snapshot.md`, `watcher/event_log.md`, `watcher/dispatch_queue.md`, `tasks/done.md`, or status-change broadcasts — or any other agent's files. Use your own Voice_Gen working tree/clone for project-repo git writes.
- **Status Changes:** Route review outcomes, task completions, and blockers to **your own** `comms/watcher_inbox/gemini.md` for **Stan** to process, using agent-scoped IDs `MSG-YYYYMMDD-GEMINI-NN`. The shared `comms/inbox_watcher.md` is retired (history only).
- **Peer Comm:** Use `comms/inbox_codex.md` for Codex CLI, `comms/inbox_claude.md` for Claude CLI, and `comms/broadcast.md` for team-wide announcements.
- **Escalation:** Send questions for Thomas or Quill to `comms/watcher_inbox/quill.md` or use `broadcast.md` for high-visibility blockers.
