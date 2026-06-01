# Decision Log

Active log for durable AgentBus decisions.

Append decisions using `decision_template.md`. Do not overwrite or delete prior decisions. Mark superseded decisions explicitly instead of removing them.

## DECISION-20260531-001

Date: 2026-05-31
Owner: Thomas / Quill
Related Task: TASK-002
Status: Accepted

### Decision

AgentBus will use `roles.md` as the authoritative role model for the Health Check CLI proof of concept. Thomas is Product Owner, Quill is Senior Analyst / PM, and Claude CLI plus Codex CLI are the Development Team.

### Reasoning

The role split gives the POC a product structure without requiring direct runtime integration between agents.

### Alternatives Considered

- Keep all agents peer-level with no product ownership.
- Assign all planning and implementation to a single agent.

### Impact

The Health Check CLI POC tasks are split by role: Codex CLI owns planning and implementation, Claude CLI owns usage documentation, and Thomas / Quill own review and acceptance.

## DECISION-20260531-003

Date: 2026-05-31
Owner: Thomas / Quill
Related Task: TASK-008
Status: Accepted

### Decision

TASK-008 (Codex CLI TTS with Lori voice) is accepted as setup-complete pending manual runtime audio confirmation. Do not stop Hannah to test Lori. Runtime validation is deferred to TASK-009, which will execute only when GPU memory is available or Hannah can be intentionally stopped during a planned test window.

### Reasoning

Hannah is healthy on port 8765 and GPU memory is constrained (~261 MB free). Starting a second MOSS-TTS instance risks disrupting Hannah, violating TASK-008's acceptance criterion. The implementation files are correct and complete; only the live audio confirmation is deferred.

### Alternatives Considered

- Stop Hannah temporarily to run Lori validation now.
- Wait passively without creating a follow-up task.

### Impact

TASK-008 moves to done. TASK-009 is created as a deferred runtime validation task, blocked until GPU memory is available or a planned test window is scheduled.

## DECISION-20260531-002

Date: 2026-05-31
Owner: Thomas / Quill
Related Task: TASK-002
Status: Accepted

### Decision

The next AgentBus proof of concept is an AgentBus Health Check CLI that reads the markdown workspace and reports coordination status.

### Reasoning

A local health check is a small, useful test of AgentBus as a coordination surface. It can validate task state, blocked work, pending messages, decisions, and last update timing without adding external dependencies.

### Alternatives Considered

- Build a web dashboard first.
- Add GitHub automation first.
- Keep AgentBus as manual markdown only.

### Impact

TASK-003 will build the CLI, TASK-004 will document usage, and TASK-005 will review and test the result.
