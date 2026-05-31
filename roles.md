# AgentBus Roles

AgentBus uses clear role separation so local and remote agents can coordinate without direct integration.

## Product Owner

**Owner:** Thomas

Thomas owns product direction, priorities, approvals, and final acceptance. The Product Owner decides what should be built and whether delivered work meets the intended goal.

## Senior Analyst / PM

**Owner:** Quill

Quill owns scope framing, task breakdown, acceptance criteria, review coordination, cross-agent synthesis, and recommendations. Quill does not directly execute local code unless explicitly asked; Quill coordinates and reviews work through AgentBus and repository context.

## Development Team

**Members:** Claude CLI and Codex CLI

The development team executes assigned implementation, documentation, testing, and review tasks. Each agent should work independently, communicate through AgentBus files, and preserve task/message/log history.

## Working Agreement

- Thomas approves direction before development begins.
- Quill converts approved direction into tasks and review criteria.
- Claude CLI and Codex CLI claim assigned work, make changes, and push updates.
- Agents use inbox messages for directed requests and `comms/broadcast.md` for shared announcements.
- Completed work moves to review before being marked done.
- Durable process or architecture decisions are recorded in `decisions/decision_log.md`.
