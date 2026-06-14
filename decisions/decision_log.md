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

## DECISION-20260613-001

Date: 2026-06-13
Owner: Thomas / Quill
Related Task: TASK-015
Status: Accepted

### Decision

The AgentBus Watcher shall initially be implemented as a **role, not a software service**. Phase 1: the Watcher role is performed by an agent (Claude CLI, Local Agent, or a future Director Agent) and is **activated on request** ("Run Watcher pass", "Process Watcher inbox"). It does not run continuously and requires no daemon, scheduler, or background process. Phase 2 (local Watcher service) and Phase 3 (Director Agent) are deferred future enhancements.

### Reasoning

Resolves REVIEW-008 blocking finding B1. A role-based Watcher lets AgentBus validate the governance model before introducing infrastructure complexity. Note: Phase 1 does not yet deliver the original spec's goal of removing manual "check for updates" intervention — that benefit lands in Phase 2.

### Alternatives Considered

- Implement the Watcher immediately as a polling service / daemon.
- Implement an autonomous Director Agent from the start.

### Impact

TASK-015 implements a manually triggered, role-based Watcher. Automation is deferred to a later governance version.

## DECISION-20260613-002

Date: 2026-06-13
Owner: Thomas / Quill
Related Task: TASK-015
Status: Accepted

### Decision

All AgentBus state files have a single defined owner and purpose (File Authority Matrix): `sprint.md` = strategic planning, **not** operational state; `state/sprint_board.md` = operational source of truth (Watcher); `watcher/event_log.md` = state-transition history (Watcher); `state/state_snapshot.md` = machine-readable summary (Watcher); `state/sync_log.md` = repository sync history; `decisions/decision_log.md` = permanent decisions; `tasks/*` = work execution records (owners); `reviews/*` = review artifacts (reviewers).

### Reasoning

Resolves REVIEW-008 blocking finding B2. Each file gets a single responsibility, eliminating overlapping state surfaces and clarifying precedence among `event_log`, `sync_log`, and `decision_log`.

### Alternatives Considered

- Keep `sprint.md` as the combined planning+operational surface.
- Let any agent write operational state to any file.

### Impact

`state/sprint_board.md` becomes the operational board, maintained by the Watcher. TASK-015 must define `sprint_board.md` as a derived/reflective aggregate of `tasks/*` (per REVIEW-009 condition 1) so the two surfaces cannot diverge.

## DECISION-20260613-003

Date: 2026-06-13
Owner: Thomas / Quill
Related Task: TASK-015
Status: Accepted

### Decision

Watcher Governance Model v1 is **additive**. Existing AgentBus workflows remain operational and no existing procedures are retired. Agents continue managing `tasks/*`, `reviews/*`, `logs/*`, and deliverables, and may send questions to agent inboxes and status updates to the Watcher inbox. The Watcher manages `sprint_board.md`, `dispatch_queue.md`, `event_log.md`, `state_snapshot.md`, and status-change broadcasts. Current procedures (`task_claiming.md`, `review_response.md`, `check_for_updates.md`) remain valid; Watcher procedures are introduced in parallel.

### Reasoning

Resolves REVIEW-008 blocking finding B3. An additive model avoids breaking existing workflows while introducing coordination improvements, rather than inverting the current task-management procedures.

### Alternatives Considered

- Retire `task_claiming.md` / `review_response.md` and force agents to stop maintaining task state immediately (original spec Rule 4).
- Defer all Watcher work until a full procedure migration is designed.

### Impact

TASK-015 introduces Watcher files and procedures in parallel with existing governance. Future governance versions may centralize authority further. Broadcast ownership must be clarified per REVIEW-009 condition 2 (agents retain announcement broadcasts; Watcher owns status-change broadcasts).

## DECISION-20260613-004

Date: 2026-06-13
Owner: Thomas
Related Task: EPIC-002 (TASK-016, TASK-021)
Status: Accepted

### Decision

Product Owner sign-off on the two EPIC-002 scope questions raised in REVIEW-011:

1. **TASK-016 overwrite protection** — fail-by-default is required (non-destructive: stop with a clear message on collision risk). Additionally ship a `--force` override that is explicit and logged. `--force` must NOT interfere with legitimate `--from-stage` resume; resuming into an existing output directory is permitted and is not a collision.
2. **TASK-021 dry-run flag name** — use `--dry-run`, matching `text_to_audio.py` for cross-tool consistency.

### Reasoning

Thomas runs the Voice_Gen pipeline iteratively (resume via `--from-stage`), so a logged escape hatch is worth the small added scope while keeping the safe default. Matching `text_to_audio.py`'s `--dry-run` continues EPIC-001's goal of reducing divergence between the two tools.

### Alternatives Considered

- Fail-by-default only, no `--force` (rejected: too rigid for iterative runs).
- Flag names `--scan-only` / `--plan-only` (rejected: inconsistent with `text_to_audio.py`).

### Impact

Releases Stan's hold on TASK-016. Stan may create the adjusted EPIC-002 board tasks per REVIEW-011 / MSG-20260613-W005, with TASK-016 including the logged `--force` criterion and the `--from-stage` resume carve-out, and TASK-021 using `--dry-run`.

## DECISION-20260614-001

Date: 2026-06-14
Owner: Thomas
Related Task: TASK-026
Related: RCA-20260613-001 (`RCA.md`), `reviews/Agent_Bus_Action_Plan_draft.md`; extends DECISION-20260613-002 (File Authority Matrix) and DECISION-20260613-003 (additive Watcher model)
Status: Accepted

### Decision

Adopt the AgentBus **Communication Isolation / Single-Writer model** to eliminate the
concurrent-writer race in RCA-20260613-001. Specifically:

1. **Core rule:** no two agents write to the same working tree or the same communication file.
2. **Single Watcher writer.** Only the Watcher writes Watcher-owned state:
   `state/sprint_board.md`, `state/state_snapshot.md`, `watcher/event_log.md`,
   `watcher/dispatch_queue.md`, **`tasks/done.md`**, and status-change broadcasts in
   `comms/broadcast.md`. `tasks/done.md` is hereby moved to Watcher ownership in the File
   Authority Matrix (extends DECISION-20260613-002).
3. **Per-agent Watcher inboxes.** `comms/watcher_inbox/<agent>.md` (`codex`, `claude`, `gemini`,
   `quill`) replace the shared `comms/inbox_watcher.md` (retired, history-only). Each agent writes
   only its own file, using agent-scoped message IDs `MSG-YYYYMMDD-<AGENT>-NN` (collision-proof by
   construction).
4. **Reviewer boundary.** Reviewers (Claude CLI) record outcomes in `tasks/review.md` + `reviews/`
   and route them to their Watcher inbox; they do **not** write Watcher-owned state. The Watcher
   mirrors the board, logs the event, records done, and broadcasts.
5. **Project-repo isolation.** Each agent uses its own working tree/clone for git write actions on
   project repos (e.g., Voice_Gen); a reviewer must not commit from a developer's working tree.
6. **One Watcher writer at a time.** The autonomous Watcher loop is not run concurrently with a
   manual Watcher pass or with any agent that self-mirrors. The loop stays paused until the
   TASK-026 cutover completes (interim operating decision, action plan §7).

### Reasoning

During the 2026-06-13 EPIC-002/003 burst, multiple actors wrote Watcher-owned state concurrently
against one shared working tree, producing duplicate message IDs (`W011`/`W012`/`MSG-015`) and a
transiently stale board. The trigger was the Claude reviewer performing a full Watcher pass in
commit `392f5a1` while the autonomous loop was also active. Enforcing a single writer per file and
per-agent, collision-proof message IDs removes the race at its root while preserving the additive
Watcher Governance Model v1.

### Alternatives Considered

- **Keep the shared inbox, add advisory locking** — rejected for v1 as heavier and still
  race-prone on ID allocation; a lock file (RCA P5) remains a possible add-on.
- **Watcher-as-service (single process owns state)** — deferred (RCA P8); larger architectural
  change than needed now.
- **Do nothing / rely on append-only recovery** — rejected; collisions recur under concurrency and
  waste reconciliation effort.

### Impact

- Governance/doc portion implemented by the Watcher (commit `b6859a2`, EVENT-20260614-001):
  per-agent inboxes, `watcher_rules.md` single-writer model + boundaries, `routing_table.md`,
  `procedures/review_response.md`, `README.md`, and the File Authority Matrix change.
- **TASK-026** (Codex, reviewer Claude; DISPATCH-20260614-001) covers the residual code/infra:
  `agentbus_health.py` duplicate-ID + board-divergence detection, per-agent project working trees,
  and inbox cutover verification.
- Agents acknowledged the new rules in their 2026-06-14 session handoffs
  (`comms/watcher_inbox/{codex,claude,gemini}.md`).

## DECISION-20260614-002

Date: 2026-06-14
Owner: Thomas D'Orsi
Recommendation: Quill
Status: **Accepted** (approved by Thomas, 2026-06-14)
Related: RCA-20260613-001, REVIEW-017, TASK-027; extends DECISION-20260614-001 (Communication Isolation)

> Watcher note: recorded at Thomas's direction and **approved by Thomas 2026-06-14** (Quill recommended Approve Option A). The source draft was headed "DECISION-20260614-001"; that ID was already taken (Communication Isolation), so this decision is assigned **-002**. Approval authorizes: pause EPIC-002/EPIC-003, dispatch TASK-027, and complete the Watcher → `AgentBus_stan` cutover after TASK-027 is complete.

### Summary

Adopt **per-agent AgentBus clones** to eliminate working-tree and staging-area contention between agents. Follows RCA-20260613-001, REVIEW-017, and TASK-027. The current single-checkout model risks one agent committing, rebasing, stashing, or otherwise interacting with another agent's uncommitted work. Goal: preserve the AgentBus governance model while isolating each agent's git workspace.

### Decision

AgentBus uses dedicated per-agent clones under `D:\Development\Sandbox`:

```text
D:\Development\Sandbox\
├── AgentBus_stan
├── AgentBus_codex
├── AgentBus_claude
├── AgentBus_gemini
└── AgentBus_quill
```

Each agent operates exclusively within its assigned AgentBus clone.

### Canonical Repository

`D:\Development\AgentBus` becomes the **human-operated reference checkout** — manual review, administration, Product Owner / PM activities, repository inspection. No autonomous agent performs routine work from this checkout.

### Operating Model

Each agent, from its own clone: `git pull --rebase` → make changes → commit → push. Agents must never commit, stage, or run cleanup commands against another agent's clone.

### Governance (unchanged)

Does not change Watcher governance, routing model, sprint-board ownership, review process, or dispatch process. The Watcher remains sole owner of `state/sprint_board.md`, `state/state_snapshot.md`, `watcher/event_log.md`, `watcher/dispatch_queue.md`, `tasks/done.md`.

### Rationale

Mirrors the isolation model already adopted for Voice_Gen workspaces under `D:\Development\Sandbox` (`Voice_Gen_codex/_claude/_gemini`). Benefits: independent working tree / staging area / local git state per agent; consistency with existing structure; prevents accidental commits of another agent's work, shared staging-area contamination, rebase conflicts from unrelated local edits, and cross-agent git operations. No changes to the task model, Watcher architecture, or review process — workspace isolation only.

### Implementation Guidance (TASK-027)

1. Per-agent AgentBus clone creation. 2. Startup documentation updates. 3. `AGENTS.md` updates. 4. Branching-strategy updates. 5. Agent startup-procedure updates. 6. Validate every active agent can pull / commit / push / receive messages / process dispatches from its isolated clone.

### Expected End State

Per-agent project workspaces (`Voice_Gen_*`) and per-agent AgentBus clones (`AgentBus_stan/_codex/_claude/_gemini/_quill`) all sync to the shared remote `origin/main`. Preserves AgentBus as the coordination layer while eliminating local working-tree contention.

### Approval Recommendation

Approve Option A; proceed with TASK-027; implement per-agent AgentBus clones under `D:\Development\Sandbox` before resuming normal multi-agent execution.
