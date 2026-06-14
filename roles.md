# AgentBus Roles

AgentBus uses clear role separation so local and remote agents can coordinate without direct integration.

## Product Owner

**Owner:** Thomas

Thomas owns product direction, priorities, approvals, and final acceptance. The Product Owner decides what should be built and whether delivered work meets the intended goal.

## Senior Analyst / PM

**Owner:** Quill

Quill owns scope framing, task breakdown, acceptance criteria, review coordination, cross-agent synthesis, and recommendations. Quill does not directly execute local code unless explicitly asked; Quill coordinates and reviews work through AgentBus and repository context.

## Development Team

**Members:** Claude CLI, Codex CLI, and Gemini CLI

The development team executes assigned implementation, documentation, testing, and review tasks. Each agent should work independently, communicate through AgentBus files, and preserve task/message/log history.

Current focus (Voice_Gen v0.3.0):
- **Codex CLI** — implementer, EPIC-002 (Voice_Gen Hardening).
- **Gemini CLI** — implementer, EPIC-003 (Text_to_Audio Enhancements, combined with Progress Reporting); joined 2026-06-13.
- **Claude CLI** — reviewer for EPIC-002 and EPIC-003.

## Coordination (Watcher)

**Role:** Watcher — nickname **Stan**

The Watcher is a manual, additive coordination role (not a fifth agent; any capable agent may perform a Watcher pass). It maintains aggregate operational state — `state/sprint_board.md`, `watcher/event_log.md`, `watcher/dispatch_queue.md`, `state/state_snapshot.md` — and status-change broadcasts, routing state changes per `watcher/routing_table.md`. The Watcher does not write code, review work, accept its own work, or approve product direction. Authority and procedures are defined in `watcher/watcher_rules.md` (DECISION-20260613-001/002/003).

## Working Agreement

- Thomas approves direction before development begins.
- Quill converts approved direction into tasks and review criteria.
- Claude CLI, Codex CLI, and Gemini CLI claim assigned work, make changes, and push updates.
- Agents use inbox messages (`comms/inbox_<agent>.md`) for directed requests and `comms/broadcast.md` for shared announcements; operational state changes route to `comms/inbox_watcher.md`.
- Completed work moves to review before being marked done.
- Durable process or architecture decisions are recorded in `decisions/decision_log.md`.
