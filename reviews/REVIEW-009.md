# REVIEW-009

Reviewer: Claude CLI
Date: 2026-06-13
Related Task: N/A — design review of governance proposal (precursor to TASK-015)
Artifact: `AgentBus Watcher Governance Proposal v1` (Quill, 2026-06-13) — response to REVIEW-008
Status: Accepted with Conditions

## Summary

Quill's *Watcher Governance Proposal v1* responds directly to the three blocking findings in REVIEW-008 and resolves all of them. It establishes three decisions (DECISION-20260613-001/002/003), a File Authority Matrix, a Watcher Authority Matrix, and a scoped TASK-015 with an end-to-end validation scenario. Thomas approved all three decisions and authorized TASK-015 on 2026-06-13.

Recommendation: **Accepted with Conditions.** The proposal is sound and conservative. Five residual items (carried from REVIEW-008 plus two new minor ambiguities) are folded into the TASK-015 acceptance criteria to be resolved during implementation — none block approval.

## Resolution of REVIEW-008 blocking findings

**B1 — Execution model undefined → RESOLVED.**
DECISION-20260613-001 defines the Watcher as a **role, not a software service**. Phase 1 is activated on request ("Run Watcher pass"); no daemon, scheduler, or background process. Phase 2 (local service) and Phase 3 (Director agent) are explicitly deferred. This is a clean, low-risk answer that lets the governance model be validated before any infrastructure is built.

**B2 — Overlapping state surfaces → RESOLVED.**
DECISION-20260613-002 provides a File Authority Matrix assigning each file a single owner and purpose: `sprint.md` = strategic planning (explicitly *not* operational state); `state/sprint_board.md` = operational source of truth (Watcher); `watcher/event_log.md` = state-transition history (Watcher); `state/state_snapshot.md` = machine-readable summary (Watcher); `state/sync_log.md` = repo sync history; `decisions/decision_log.md` = permanent decisions; `tasks/*` = work execution (owners); `reviews/*` = review artifacts (reviewers). This delineates the three ledgers REVIEW-008 flagged (`event_log` vs `sync_log` vs `decision_log`).

**B3 — Governance-compatibility contradiction → RESOLVED.**
DECISION-20260613-003 makes Watcher v1 **additive**: no existing procedures are retired, agents continue managing `tasks/*`, and Watcher procedures run in parallel. This sidesteps the original spec's Rule-4 inversion rather than forcing a procedure migration — a safer resolution than the migration path REVIEW-008 had proposed.

## Resolution of REVIEW-008 non-blocking findings

- **N3 (TASK-015 did not exist) → RESOLVED.** Now formally scoped with owner (Codex CLI), reviewer (Claude CLI), priority, and acceptance criteria.
- **N4 (no end-to-end validation) → RESOLVED.** TASK-015 includes an explicit Validation Scenario: Review Accepted → Watcher update → sprint board updated → event logged → dispatch generated → broadcast generated, recorded and reviewed.

## Conditions (folded into TASK-015 acceptance criteria)

These do not block approval; they are carried forward so implementation closes them.

1. **`sprint_board.md` vs `tasks/*` reconciliation.** Define `sprint_board.md` as a derived/reflective aggregate of `tasks/*` — the Watcher mirrors task state into the board; `tasks/*` remains authoritative for individual task state, `sprint_board.md` authoritative for the aggregate board view. Without this the two operational surfaces can diverge.
2. **Broadcast ownership.** Clarify that agents retain `broadcast.md` for announcements and review notices; the Watcher owns *status-change* broadcasts only. (DECISION-003 lists "broadcasts" flatly under Watcher, but the Authority Matrix scopes it to "Broadcast status change.")
3. **Version tag (REVIEW-008 N2, still open).** AgentBus infrastructure must not use the Voice_Gen `[v0.3.0]` release tag. Set the TASK-015 commit convention to an AgentBus track or untagged.
4. **Correction procedure (REVIEW-008 N5, partial).** The Authority Matrix adds "Override Watcher action → Thomas/Quill," but `watcher_rules.md` must also document how to undo a bad dispatch or revert an event-log entry.
5. **`dispatch_queue.md` completeness.** Owned by the Watcher per DECISION-003 and TASK-015 but missing from the DECISION-002 File Authority Matrix — add it for completeness.

## Note on phasing

Phase 1 keeps the Watcher manually triggered, so it does **not yet** deliver the original feature spec's headline goal of removing manual "check for updates" intervention — that benefit lands in Phase 2 (local service). This is a deliberate, reasonable phasing choice approved with eyes open.

## Acceptance Recommendation

**Accepted with Conditions.** DECISION-20260613-001/002/003 are approved by Thomas and resolve all REVIEW-008 blocking findings. TASK-015 (Implement Watcher Governance Model v1) is authorized with Codex CLI as implementer and Claude CLI as reviewer. Conditions 1–5 above are incorporated into the TASK-015 acceptance criteria and will be verified at review, including the required end-to-end workflow simulation.
