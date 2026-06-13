# Watcher Dispatch Queue

The dispatch queue tracks work that the Watcher has routed or is preparing to route. It is Watcher-owned state.

## Dispatch Template

### DISPATCH-YYYYMMDD-000

Dispatch ID:
Trigger:
Related Task:
Assigned Agent:
Reviewer:
Action:
Status: Pending | Dispatched | Complete | Cancelled | Corrected
Created:
Updated:

#### Notes

#### Correction

## DISPATCH-20260613-001

Dispatch ID: DISPATCH-20260613-001
Trigger: REVIEW-007 accepted TASK-014 and completed EPIC-001; Thomas authorized TASK-015 through MSG-20260613-002.
Related Task: TASK-015
Assigned Agent: Codex CLI
Reviewer: Claude CLI
Action: Claim and implement the additive Watcher Governance Model v1, satisfying REVIEW-009 conditions C1-C5 and recording the end-to-end validation scenario.
Status: Complete
Created: 2026-06-13
Updated: 2026-06-13

#### Notes

This dispatch is the validation-cycle dispatch for TASK-015. It demonstrates that an accepted review and authorized follow-up can be routed into a concrete next action.

2026-06-13: Codex CLI completed the dispatch action and submitted TASK-015 for Claude CLI review.

#### Correction

## DISPATCH-20260613-002

Dispatch ID: DISPATCH-20260613-002
Trigger: Thomas authorized EPIC-002 (Voice_Gen Hardening, v0.3.0 Phase 2). EPIC-001 is complete, satisfying the dependency.
Related Task: EPIC-002 (tasks not yet created; breakdown pending)
Assigned Agent: Codex CLI
Reviewer: Claude CLI
Action: Claim EPIC-002. Create branch `vg_e002_voice_gen_hardening` from `vg_e001_shared_config` per `procedures/branching_strategy.md`. Propose a task breakdown covering the six hardening items, then submit the breakdown for Claude CLI review BEFORE implementation begins.
Status: Dispatched
Created: 2026-06-13
Updated: 2026-06-13

#### Notes

EPIC-002 scope (from `comms/voice-gen_0.2.0_feature_request.md`):
- #3b Overwrite protection — Critical
- #2a Handler clear in `setup_logging()` — High
- #2b KeyboardInterrupt handling — High
- #2c Dependency-check logging order — High
- #3a Dry-run / scan-only mode — High
- #2d `--log-file` override — Med

Workflow gates (per Thomas, 2026-06-13):
1. Codex claims EPIC-002, creates the branch, and proposes the task breakdown as part of claiming.
2. Claude CLI reviews the breakdown and posts notable concerns.
3. After Claude's review, the Watcher creates the resulting tasks (TASK-016+) on `state/sprint_board.md`.
4. Codex begins implementation only after the tasks exist on the board.

Branch creation may proceed now; implementation waits for board task creation in step 3.

2026-06-13: Codex completed the dispatch action (W004) — branch `vg_e002_voice_gen_hardening` created and breakdown posted (MSG-20260613-008). Claude reviewed the breakdown (REVIEW-011, W005). Dispatch is now Complete; implementation continues under DISPATCH-20260613-003.

#### Correction

## DISPATCH-20260613-003

Dispatch ID: DISPATCH-20260613-003
Trigger: Claude CLI accepted the EPIC-002 breakdown with changes (REVIEW-011 / W005); Watcher created the adjusted tasks on the board (EVENT-20260613-010).
Related Task: TASK-016, TASK-018, TASK-019, TASK-020, TASK-021
Assigned Agent: Codex CLI
Reviewer: Claude CLI
Action: Implement the Ready EPIC-002 tasks on branch `vg_e002_voice_gen_hardening` in the suggested order (TASK-016 first; TASK-021 last). Use commit tag `[v0.3.0][vg_e002][TASK-0NN]`. Submit each task to Claude CLI for review per the standard workflow. Also populate the empty `artifacts/Planning/PR_Voice_Gen/epics/EPIC-002_voice_gen_hardening.md` detail file (REVIEW-011 F5).
Status: Dispatched
Created: 2026-06-13
Updated: 2026-06-13

#### Notes

- TASK-016 ships fail-by-default overwrite protection with a `--from-stage` resume carve-out, plus a logged `--force` override **approved per DECISION-20260613-004** (must not interfere with `--from-stage` resume).
- TASK-020 is plumbing only (CLI arg + pass-through to the existing `setup_logging(log_file=...)`; default resolves to configured `LOG_DIR`).
- TASK-021 flag name is `--dry-run`.
- TASK-017 is dropped (delivered by EPIC-001); do not implement.

#### Correction
