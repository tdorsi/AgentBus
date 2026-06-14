# REVIEW-020

Reviewer: Claude CLI
Date: 2026-06-14
Related Task: TASK-027 (AgentBus Working-Tree Isolation — per-agent clones)
Artifact: AgentBus commit `602e6b5 [agentbus][TASK-027] Add AgentBus clone isolation` (submission `ea880bb`)
Status: Accepted

## Summary

TASK-027 closes the residual shared-checkout race on the AgentBus repo itself (the gap behind the unintended consolidated push in REVIEW-017). It implements DECISION-20260614-002 Approach A: per-agent AgentBus clones under `D:\Development\Sandbox\AgentBus_<agent>`, with the canonical `D:\Development\AgentBus` as the human-operated reference checkout. All acceptance criteria are met, verified by direct inspection (clones exist with correct remotes; the new health check runs). Codex respected the no-impersonation boundary throughout. Accepted — this review is itself recorded from `AgentBus_claude`, the first use of the new model.

## Verification Against Acceptance Criteria

**Per-agent clones exist with `origin` configured** ✓ — verified all five (`AgentBus_stan`, `_codex`, `_claude`, `_gemini`, `_quill`) exist under `D:\Development\Sandbox` and each has `origin = https://github.com/tdorsi/AgentBus.git`. Canonical `D:\Development\AgentBus` documented as the human-operated reference checkout post-cutover.

**No shared working tree/index; pushes serialize via `pull --rebase`** ✓ — each clone has its own tree/index/stash/rebase state; the `git pull --rebase origin main` → commit → push discipline is documented in `agent_startup.md`, `branching_strategy.md`, and `AGENTS.md`. (I exercised it: this clone pulled --rebase cleanly to `7892d7b` before writing.)

**Structural validation, no impersonation** ✓ — the submission documents `git remote -v` / `fetch` / `pull --rebase` / `status --branch` for `stan`/`claude`/`gemini`/`quill` (the clones Codex does not own) and a real sync→commit→rebase→push only from `AgentBus_codex`. Boundary notes explicitly confirm Codex did not commit, push, or post as any other agent. Correct.

**First-startup self-validation documented** ✓ — `agent_startup.md` adds a "First Startup Self-Validation" section: validate only from your own clone (path check, fetch, `pull --rebase`, trivial change → commit → push → inbox/dispatch read), with an explicit instruction not to validate by acting as another agent.

**Docs updated** ✓ — `procedures/agent_startup.md` (clone table + `pull --rebase` + self-validation), `procedures/branching_strategy.md` ("AgentBus Coordination Clones": no shared tree/index/stash/rebase, clone layout, canonical-checkout rule), and `D:\Development\AGENTS.md` (clone list, `pull --rebase` before push, human-operated canonical checkout). Consistent across all three.

**(Optional, REVIEW-017 FU) Active retired-inbox detection** ✓ — `agentbus_health.py` adds `RETIRED_WATCHER_INBOX_RE` + a `HISTORY_CONTEXT_RE` guard (`retired|history|source:|correction|replaced|legacy|…`) so it flags only live, non-history references to `comms/inbox_watcher.md`. Run reports **Active Retired-Inbox References: 0**, exit 1 (legacy duplicate IDs / board divergences still surface). This is exactly the enhancement I suggested in REVIEW-017; it would have caught FU1.

**Single-writer file-ownership unchanged** ✓ — DECISION-20260614-002 preserves the Watcher governance/routing/ownership model (workspace isolation only). Verified the decision text and that no ownership rules changed.

## Observations (non-blocking)

- **`tasks/review.md` has a misplaced block:** a "Review Outcome (resubmission)" carrying TASK-020 (`--log-file` F1) content appears appended under the **TASK-027** entry. It's a concurrent-edit artifact — ironically the exact shared-checkout corruption TASK-027 eliminates going forward. Recommend the owner/Watcher tidy it; harmless to acceptance.
- The retired-inbox detector is keyword-heuristic (history-context allowlist). Good as a detection aid; a future tightening could scope it to instruction fields (Action/Requested Action) to reduce reliance on keyword context. Non-blocking.
- Board divergences rose 7 → 10 — transient board lag while TASK-027 is active/unmirrored, not a TASK-027 defect.

## Cutover Note

Per DECISION-20260614-002, accepted agents operate from their own clones. Effective now, my reviews run from `D:\Development\Sandbox\AgentBus_claude` (not the canonical checkout); the Watcher's cutover to `AgentBus_stan` is authorized to follow this acceptance.

## Acceptance Recommendation

**Accepted.** TASK-027 implements DECISION-20260614-002 Approach A correctly and completely: five per-agent clones with correct remotes, documented `pull --rebase` push discipline, no-impersonation structural validation, first-startup self-validation, consistent docs, and the optional active retired-inbox health check. The residual shared-checkout race on the AgentBus repo is closed. EPIC-002/EPIC-003 can resume once the Watcher completes the `AgentBus_stan` cutover.
