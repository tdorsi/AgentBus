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

#### Progress

- 2026-06-13: TASK-016 implemented and submitted for review — Voice_Gen commit `9a52d61`; mirrored as Review on the board (W007, EVENT-20260613-013). TASK-018/019/020/021 remain Ready. Dispatch stays open until all EPIC-002 tasks are accepted.
- 2026-06-13: TASK-016 **accepted** by Claude CLI (REVIEW-012, W008, EVENT-20260613-014); mirrored to Done. TASK-018 is next per the suggested order (already Ready); TASK-019/020/021 still Ready. Dispatch remains open.
- 2026-06-13: TASK-018 implemented and submitted for review — Voice_Gen commit `c2d62e8`; mirrored as Review on the board (W009, EVENT-20260613-015). TASK-019/020/021 remain Ready. Dispatch stays open until all EPIC-002 tasks are accepted.
- 2026-06-13: TASK-018 **accepted** by Claude CLI (REVIEW-013, W010, EVENT-20260613-016); mirrored to Done. 2 of 5 accepted. TASK-019 is next per the suggested order (already Ready); TASK-020/021 still Ready. Dispatch remains open.
- 2026-06-13: TASK-019 implemented and submitted for review — Voice_Gen commit `8b993a5`; mirrored as Review on the board (W011, EVENT-20260613-021). TASK-020/021 remain Ready. Dispatch stays open until all EPIC-002 tasks are accepted.
- 2026-06-13: TASK-019 **accepted** by Claude CLI (REVIEW-014, W012, EVENT-20260613-022); mirrored to Done. 3 of 5 accepted. TASK-020 is next per the suggested order.
- 2026-06-13: TASK-020 implemented and submitted for review — Voice_Gen commit `bf31d45`; mirrored as Review on the board (EVENT-20260613-023). TASK-021 remains Ready. Dispatch stays open until all EPIC-002 tasks are accepted.
- 2026-06-13: TASK-020 returned **Changes Requested** by Claude CLI (REVIEW-016 F1, W014, EVENT-20260613-024) — custom `--log-file` parent dir not created. Kept in Review/changes-requested; fix routed to Codex CLI (`comms/inbox_codex.md` MSG-20260613-018). TASK-021 still Ready. Dispatch remains open.

#### Correction

## DISPATCH-20260613-004

Dispatch ID: DISPATCH-20260613-004
Trigger: Thomas authorized EPIC-003 (Text_to_Audio Enhancements) with Gemini CLI as owner and Claude CLI as reviewer, and confirmed combining EPIC-004 (Progress Reporting) into EPIC-003 while deferring EPIC-005 (Batch Input). EPIC-001 is complete, satisfying the dependency.
Related Task: EPIC-003 (tasks not yet created; breakdown pending)
Assigned Agent: Gemini CLI
Reviewer: Claude CLI
Action: Claim EPIC-003. Create branch `vg_e003_text_to_audio_enhancements` from `vg_e001_shared_config` per `procedures/branching_strategy.md`. Propose a task breakdown (TASK-022+) covering the combined scope, then submit the breakdown to Claude CLI for review BEFORE implementation begins. Populate the empty EPIC-003 detail file.
Status: Dispatched
Created: 2026-06-13
Updated: 2026-06-13

#### Notes

Combined EPIC-003 scope (all `text_to_audio.py`):
- #4b — Per-chunk WAV preservation (optional `--keep-chunks`).
- Progress / ETA reporting (pulled forward from EPIC-004): progress tracking, status reporting, ETA for long inference runs.

Out of scope: EPIC-005 Batch Input — deferred to a later release.

Workflow gates (same as EPIC-002, per Thomas 2026-06-13):
1. Gemini claims EPIC-003, creates the branch, and proposes the task breakdown as part of claiming.
2. Claude CLI reviews the breakdown and posts notable concerns.
3. After Claude's review, the Watcher creates the resulting tasks (TASK-022+) on `state/sprint_board.md`.
4. Gemini begins implementation only after the tasks exist on the board.

Commit tag: `[v0.3.0][vg_e003][TASK-0NN]`.

Planning-doc note: the roadmap (`voice_gen_roadmap.md`) and release plan (`Releases/voice_gen_v0.3.0.md`) need amendment to reflect the 003+004 combine and 005 deferral — owned by Thomas / Quill, not the Watcher.

#### Progress

- 2026-06-13: Gemini claimed EPIC-003, targeted branch `vg_e003_text_to_audio_enhancements`, populated the EPIC-003 detail file, and posted the breakdown to Claude (W011-Gemini, MSG-20260613-016). Claude accepted with changes (REVIEW-015, W013). Breakdown dispatch is **Complete**; implementation continues under DISPATCH-20260613-005.

#### Correction

## DISPATCH-20260613-005

Dispatch ID: DISPATCH-20260613-005
Trigger: Claude CLI accepted the EPIC-003 breakdown with changes (REVIEW-015 / W013); Watcher created the adjusted tasks on the board (EVENT-20260613-025).
Related Task: TASK-022, TASK-023, TASK-024, TASK-025
Assigned Agent: Gemini CLI
Reviewer: Claude CLI
Action: Implement the Ready EPIC-003 tasks on branch `vg_e003_text_to_audio_enhancements` in order (TASK-022 first; TASK-025 last). Use commit tag `[v0.3.0][vg_e003][TASK-0NN]`. Submit each task to Claude CLI for review; route outcomes to `comms/inbox_watcher.md`.
Status: Dispatched
Created: 2026-06-13
Updated: 2026-06-13

#### Notes

Per REVIEW-015 acceptance criteria:
- TASK-022 `--keep-chunks`: default off; `<stem>_chunk_001.wav` naming; final WAV byte-identical with/without; no-op under `--dry-run`.
- TASK-023 progress: shared `voice_gen_utils` console helpers; real-synthesis only; no log interleave.
- TASK-024 ETA: completed-chunk throughput basis; `--voice all` counts remaining voices; pre-first-chunk state defined.
- TASK-025: README + recorded real multi-chunk run exercising `--keep-chunks` with progress/ETA.

No Product Owner hold for EPIC-003.

#### Correction

## DISPATCH-20260614-001

Dispatch ID: DISPATCH-20260614-001
Trigger: Thomas authorized TASK-026 (Communication Isolation — residual code + infra) and a coordinated pause/snapshot/restart of all agents under the new single-writer rules.
Related Task: TASK-026
Assigned Agent: Codex CLI
Reviewer: Claude CLI
Action: After the coordinated pause/snapshot and restart under the new rules, implement TASK-026: add duplicate-ID + board-divergence detection to `agentbus_health.py`, confirm the per-agent Watcher inbox cutover, and verify the isolation rules. Submit to Claude CLI; route the outcome to `comms/watcher_inbox/codex.md`.
Status: Dispatched
Created: 2026-06-14
Updated: 2026-06-14

#### Notes

- Gated on the restart: all three agents (Codex, Claude, Gemini) first pause, snapshot completed work, and resume under the new communication-isolation rules. Project-repo working-tree isolation is operator (Thomas) infra.
- Governance/doc portion already landed (commit b6859a2, EVENT-20260614-001); this dispatch covers the residual code/infra/cutover only.

#### Correction
