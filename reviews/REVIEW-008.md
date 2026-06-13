# REVIEW-008

Reviewer: Claude CLI
Date: 2026-06-13
Related Task: N/A — design review of proposed feature (no task created yet)
Artifact: `Watcher_Agent_feature.md` — AgentBus Watcher architecture and governance specification
Status: Changes Requested

## Summary

`Watcher_Agent_feature.md` proposes a dedicated **Watcher** coordination role that becomes the authoritative state-transition engine for AgentBus: monitoring communications, maintaining sprint state, routing messages, dispatching work, and activating dependent tasks when reviews complete. It defines a routing model, five required documents (`watcher_rules.md`, `routing_table.md`, `dispatch_queue.md`, `event_log.md`, `sprint_board.md`), a Watcher inbox, and three operating procedures (Review Accepted, Blocked Task, EPIC Completion).

The concept is **sound and worth doing** — a single-writer Watcher for sprint state is the correct pattern to eliminate the concurrent-edit risk inherent in running two CLI agents against the same markdown workspace. However, the spec is **not ready to implement as written**. It leaves the execution model undefined and creates three overlapping state surfaces that, without explicit reconciliation, would produce divergence rather than a single source of truth. Recommendation: **Changes Requested** — one revision pass resolving the three blocking items below.

## Strengths

- **Solves a real problem.** Sprint state is currently edited by whichever agent acts. With two concurrent CLI instances, that is a live merge-conflict risk. Centralizing sprint-state writes in the Watcher is the right fix.
- **Routing table is unambiguous.** Review outcomes / task completions → Watcher inbox; directed questions → agent inboxes; announcements → broadcast. Clean and complete.
- **The three operating procedures formalize existing behavior** (Review Accepted, Blocked, EPIC Completion) rather than inventing new flows — they map directly onto cycles AgentBus already runs manually.

## Blocking Findings

### B1 — Execution model is undefined

The spec calls the Watcher "the authoritative state-transition engine" (implying automation) but also states it "can be used by Claude, Codex, or a future local Director agent" (implying a role an agent adopts). AgentBus is markdown-only with no runtime. The spec never states **what runs the Watcher, or when.** As written, a human must still tell an agent to run a Watcher pass — which is the exact manual-intervention problem the document opens by trying to eliminate.

**Required:** Decide and document the trigger model. Options: (a) a scheduled/looped agent session, (b) a hat an agent explicitly dons on request, or (c) a hybrid. This decision shapes every other document, so it must be settled first.

### B2 — Three overlapping state surfaces

The spec adds `state/sprint_board.md` and `watcher/event_log.md`, but the workspace already has:
- `sprint.md` (root) — its own status / assignments / decisions sections
- `state/state_snapshot.md`, `state/agent_status.md`, `state/sync_log.md`
- `decisions/decision_log.md`, `logs/`

Without an explicit precedence statement, agents will not know which file is authoritative, defeating the goal.

**Required:** State which file supersedes which — e.g. "`sprint_board.md` becomes the authoritative board and `sprint.md` status sections are retired" — and delineate `event_log.md` (state transitions) vs `sync_log.md` (sync records) vs `decision_log.md` (durable decisions).

### B3 — "Existing governance remains compatible" is contradicted by the spec

Rule 4 states Claude/Codex "should NOT directly maintain sprint state." But `procedures/task_claiming.md` and `procedures/review_response.md` currently have agents writing directly to `tasks/active.md`, `tasks/review.md`, and `sprint.md`. This is an **inversion** of existing procedure, not an addition — so the acceptance criterion "Existing AgentBus governance remains compatible" cannot be met unless those procedures are revised in the same change.

**Required:** The spec must own the procedure migration: enumerate which existing procedures change, and how task claiming / review response behave once the Watcher owns sprint state.

## Non-Blocking Findings

### N1 — Ambiguous file layout

The required-changes block indents `watcher_rules.md`, `routing_table.md`, `dispatch_queue.md`, `event_log.md` under `watcher/` but it is not explicit whether they live inside `watcher/` or at root. Write them as full paths (`watcher/watcher_rules.md`, etc.).

### N2 — Wrong version tag

The commit format is `[v0.3.0][agentbus][TASK-015]`. v0.3.0 is the **Voice_Gen** product release. This is AgentBus coordination tooling, not the product — tagging it under the Voice_Gen release conflates two independent things. Recommend AgentBus infra be untagged or versioned on its own track.

### N3 — TASK-015 does not exist

The commit format references TASK-015, but no such task exists in `tasks/backlog.md` and no acceptance criteria have been scoped. This document reads as a direct implementation brief that bypasses the normal flow (Thomas approves → Quill scopes a task with acceptance criteria → agent implements → reviewer accepts). It should become a real backlog task before implementation.

### N4 — No end-to-end validation criterion

Acceptance is mostly "files created" and "documentation consistent" — necessary but subjective. Add a behavioral criterion: simulate one full cycle (a Review = Accepted event flows from the Watcher inbox → task moved to Done → dependent task dispatched → broadcast posted) to prove the model works, not just that the files exist.

### N5 — No correction / rollback procedure

The spec defines forward transitions but no recovery path for when the Watcher mis-detects an outcome or dispatches the wrong work. Add a correction procedure and state who has authority to override a Watcher action.

## Acceptance Recommendation

**Changes Requested.** The Watcher concept is endorsed and the routing/procedure design is largely sound. Before implementation proceeds, the spec needs one revision pass resolving the three blocking items:

- **B1** — define the Watcher execution/trigger model.
- **B2** — reconcile the new state files against existing ones and declare precedence.
- **B3** — own the migration of `task_claiming.md` / `review_response.md` so agents stop writing sprint state directly.

Once B1–B3 are answered (N1–N5 are quick cleanups), this is an implementable governance upgrade. Suggested next step: convert it to a scoped backlog task (TASK-015) under AgentBus governance, with Codex as implementer and Claude CLI as reviewer, consistent with the established split.
