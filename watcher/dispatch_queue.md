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
- 2026-06-14: Codex resubmitted the TASK-020 F1 fix (Voice_Gen commit `19372bb` on `vg_e002_voice_gen_hardening__codex__TASK-020`, MSG-20260614-CODEX-03, EVENT-20260614-009); mirrored as Review, awaiting Claude re-review. TASK-021 still Ready.
- 2026-06-14: TASK-020 **accepted** by Claude CLI (REVIEW-018, MSG-20260614-CLAUDE-03, EVENT-20260614-013); mirrored to Done. EPIC-002 = 4/5 accepted. **TASK-021 held — EPIC-002 PAUSED pending TASK-027** (DECISION-20260614-002). This dispatch is paused; resume after TASK-027 completes.
- 2026-06-14: **EPIC-002 RESUMED** — TASK-027 accepted (EVENT-20260614-020); TASK-021 (`--dry-run`) is Ready again and is Codex's next item. Dispatch reactivated.
- 2026-06-14: TASK-021 implemented and submitted for review — Voice_Gen commit `6529caa` (MSG-20260614-CODEX-05, EVENT-20260614-021); mirrored as Review. **Last EPIC-002 item** — on acceptance, EPIC-002 is complete and this dispatch closes.
- 2026-06-15: TASK-021 **accepted** by Claude CLI (REVIEW-024, MSG-20260614-CLAUDE-07, EVENT-20260615-001); mirrored to Done. **EPIC-002 (Voice_Gen Hardening) COMPLETE** (TASK-016/018/019/020/021). Dispatch **Complete**.

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
Action: Implement the Ready EPIC-003 tasks on branch `vg_e003_text_to_audio_enhancements` in order (TASK-022 first; TASK-025 last). Use commit tag `[v0.3.0][vg_e003][TASK-0NN]`. Submit each task to Claude CLI for review; route outcomes to `comms/watcher_inbox/gemini.md`.
Status: Complete
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

- 2026-06-14 (FU1, REVIEW-017 / EVENT-20260614-008): the Action routing reference was corrected from the retired `comms/inbox_watcher.md` to `comms/watcher_inbox/gemini.md`. This was the one remaining live reference to the retired shared inbox; flagged by Claude and Codex (both correctly declined to edit Watcher-owned state), fixed here by the Watcher.
- 2026-06-14: TASK-022 **accepted** by Claude CLI (REVIEW-019, MSG-20260614-CLAUDE-04, EVENT-20260614-014); mirrored to Done. **TASK-023/024/025 held — EPIC-003 PAUSED pending TASK-027** (DECISION-20260614-002). This dispatch is paused; resume after TASK-027 completes.
- 2026-06-14: **EPIC-003 RESUMED** — TASK-027 accepted (EVENT-20260614-020); TASK-023 (progress reporting) is Gemini's next, then 024/025. Dispatch reactivated.
- 2026-06-14: TASK-023 (`de773cd`), TASK-024 (`3530bd5`), and TASK-025 (`793a80b`) implemented and submitted for review (MSG-20260614-GEMINI-03/04/05, EVENT-20260614-022); all mirrored as Review. On acceptance of all three, EPIC-003 is complete and this dispatch closes.
- 2026-06-14: TASK-023/024 **accepted** (REVIEW-021/022, EVENT-20260614-023); TASK-025 **accepted with follow-ups** (REVIEW-023, EVENT-20260614-024). **EPIC-003 feature-complete** (TASK-022/023/024/025). FU1 (real recorded end-to-end MOSS-TTS run) deferred to Thomas / a test window — tracked under Blocked. Dispatch **Complete**.

## DISPATCH-20260614-001

Dispatch ID: DISPATCH-20260614-001
Trigger: Thomas authorized TASK-026 (Communication Isolation — residual code + infra) and a coordinated pause/snapshot/restart of all agents under the new single-writer rules.
Related Task: TASK-026
Assigned Agent: Codex CLI
Reviewer: Claude CLI
Action: After the coordinated pause/snapshot and restart under the new rules, implement TASK-026: add duplicate-ID + board-divergence detection to `agentbus_health.py`, confirm the per-agent Watcher inbox cutover, and verify the isolation rules. Submit to Claude CLI; route the outcome to `comms/watcher_inbox/codex.md`.
Status: Complete
Created: 2026-06-14
Updated: 2026-06-14

#### Notes

- Gated on the restart: all three agents (Codex, Claude, Gemini) first pause, snapshot completed work, and resume under the new communication-isolation rules. Project-repo working-tree isolation is operator (Thomas) infra.
- Governance/doc portion already landed (commit b6859a2, EVENT-20260614-001); this dispatch covers the residual code/infra/cutover only.
- 2026-06-14: Scope expanded to include the AGENTS.md startup-file cutover (EVENT-20260614-003). `D:\Development\AGENTS.md` (CLI-agnostic grounding) created and `GEMINI.md` repointed by the Watcher; Codex's startup config and remaining `CLAUDE.md` cross-references are part of TASK-026.
- 2026-06-14: Per-agent working trees established (EVENT-20260614-006) — `git worktree`s under `D:\Development\Sandbox\Voice_Gen_{codex,gemini,claude}` on per-task branches. Remaining for Codex: `agentbus_health.py` duplicate-ID/board-divergence detection, repoint Codex startup config to AGENTS.md, and cutover verification.
- 2026-06-14: TASK-026 implemented (AgentBus commit `207e2e9`) and **accepted with follow-ups** by Claude CLI (REVIEW-017, MSG-20260614-CLAUDE-02, EVENT-20260614-007); mirrored to Done. FU1 (DISPATCH-20260613-005 routing) fixed by the Watcher. Dispatch Complete.

#### Correction

## DISPATCH-20260614-002

Dispatch ID: DISPATCH-20260614-002
Trigger: Thomas approved DECISION-20260614-002 (AgentBus Working-Tree Isolation, Approach A) and directed: pause EPIC-002/EPIC-003, implement TASK-027 first, complete the Watcher cutover after.
Related Task: TASK-027
Assigned Agent: Codex CLI
Reviewer: Claude CLI
Action: Implement Approach A — create per-agent AgentBus clones under `D:\Development\Sandbox\AgentBus_<agent>` (`stan`, `codex`, `claude`, `gemini`, `quill`); update `procedures/agent_startup.md`, `procedures/branching_strategy.md`, and `D:\Development\AGENTS.md`; validate each active agent can pull / commit / push / receive messages / process dispatches from its own clone. Optional (REVIEW-017 FU): have `agentbus_health.py` flag active, non-history references to retired inboxes. Submit to Claude CLI; route outcome to `comms/watcher_inbox/codex.md`.
Status: Complete
Created: 2026-06-14
Updated: 2026-06-14

#### Notes

- **EPIC-002 and EPIC-003 are paused** until TASK-027 completes (TASK-021 and TASK-023/024/025 held).
- The canonical `D:\Development\AgentBus` becomes the human-operated reference checkout; no routine autonomous work from it after cutover.
- **Watcher → `AgentBus_stan` cutover happens after TASK-027 is complete** (per Thomas), not during.
- Commit tag for AgentBus work: `[agentbus][TASK-027]`.

#### Progress

- 2026-06-14: Codex implemented TASK-027 from its own `AgentBus_codex` clone (AgentBus commit `602e6b5`) and submitted for review (MSG-20260614-CODEX-04, EVENT-20260614-017); mirrored as Review. Validation boundary honored (structural-by-Codex, no impersonation); all five clones created with `origin` and verified `pull --rebase`-clean. Awaiting Claude's review; dispatch stays open until TASK-027 is accepted, then the Watcher cuts over to `AgentBus_stan` and EPIC-002/003 resume.
- 2026-06-14: TASK-027 **accepted** by Claude CLI (REVIEW-020, MSG-20260614-CLAUDE-05, EVENT-20260614-018); mirrored to Done. **Watcher cutover to `AgentBus_stan` complete** (EVENT-20260614-019) — this pass is the first committed from the stan clone. **EPIC-002/003 resumed** (EVENT-20260614-020). Dispatch **Complete**.

#### Correction

## DISPATCH-20260614-003

Dispatch ID: DISPATCH-20260614-003
Trigger: Thomas opened a test window (TTS server free, 2026-06-14) to discharge TASK-025 FU1 (REVIEW-023) — the real recorded EPIC-003 end-to-end run.
Related Task: TASK-028
Assigned Agent: Gemini CLI
Reviewer: Claude CLI
Action: From your own Voice_Gen worktree, run a **real** MOSS-TTS synthesis via `text_to_audio.py` exercising `--keep-chunks` + `--voice all` with progress + ETA, against the live server. Record the run (console/log output + produced chunk/final WAV evidence) and submit to Claude CLI with a `tasks/review.md` entry; route the outcome to `comms/watcher_inbox/gemini.md`.
Status: Complete
Created: 2026-06-14
Updated: 2026-06-14

#### Notes

- This is the runtime confirmation deferred from TASK-025 C4 (analogous to TASK-009 for Lori audio). Feature code is already accepted (REVIEW-021/022/023); this run validates it on real hardware.
- Coordinate to avoid disrupting other TTS usage; do not stop a server in use by Thomas or another agent.
- Operate from `AgentBus_gemini` for coordination writes and your Voice_Gen worktree for the run.

#### Progress

- 2026-06-15: Gemini ran the real e2e validation (MSG-20260614-GEMINI-06, EVENT-20260615-002): 67 chunk WAVs written, `--keep-chunks`/progress/ETA exercised 30+ min on the live server; run then crashed at chunk 68/133 on an environment `onnxruntime` 2.3 GB allocation error (not a feature defect). Mirrored as Review, awaiting Claude's FU1 confirmation.
- 2026-06-15: TASK-028 **accepted** by Claude CLI (REVIEW-025, MSG-20260615-CLAUDE-08, EVENT-20260615-003) — **TASK-025 FU1 closed**; evidence verified directly. Mirrored to Done. **EPIC-003 runtime-validated.** Dispatch **Complete**.

#### Correction

## DISPATCH-20260621-001

Dispatch ID: DISPATCH-20260621-001
Trigger: Thomas authorized Phase 3 integration (2026-06-21), directing the merge-up in order: `vg_e003` first, then `vg_e002`. EPIC-002 + EPIC-003 are complete and runtime-validated; merge preconditions (review complete, work accepted) are satisfied.
Related Task: TASK-029
Assigned Agent: Gemini CLI
Reviewer: Claude CLI
Action: From your own Voice_Gen worktree, integrate EPIC-003 into the v0.3.0 RC. **(1) Consolidate:** establish the `vg_e003_text_to_audio_enhancements` epic branch off `vg_e001_shared_config` containing the accepted EPIC-003 stack (TASK-022/023/024/025, integrated tip `793a80b`) and push it (the epic branch is currently not on origin and unpopulated). **(2) Merge upward:** merge `vg_e003_text_to_audio_enhancements` into `vg_e001_shared_config`, resolving EPIC-003-scope conflicts. **(3) Verify:** `py_compile` + `--dry-run` smoke; confirm `--keep-chunks`/progress/ETA on the integrated branch. Merge commit `[v0.3.0][vg_e003]`; push `vg_e001_shared_config`. Submit to Claude CLI with a `tasks/review.md` entry; route the outcome to `comms/watcher_inbox/gemini.md`. Prune merged EPIC-003 session branches after acceptance.
Status: Complete
Created: 2026-06-21
Updated: 2026-06-21

#### Notes

- This is the **first** of the two Phase 3 merges per Thomas's sequencing. TASK-030 (EPIC-002) is gated on this being accepted.
- Watcher-verified branch state (2026-06-21): `vg_e003_text_to_audio_enhancements` is absent on origin and empty locally (tip `a83550f` = vg_e001 base); accepted work is the linear session stack, integrated tip `793a80b` (`…__gemini__TASK-025`), which Claude reviewed as a clean 022→023→024→025 stack that compiles. Hence the consolidation step before merging up.
- Feature work merges upward only — do not merge `vg_e001_shared_config` into the feature branch.

#### Progress

- 2026-06-21: Gemini consolidated the EPIC-003 stack onto `vg_e003_text_to_audio_enhancements` (pushed to origin), merged it up into `vg_e001_shared_config` with `--no-ff` (merge `ffc7b5e`), and submitted for review (`tasks/review.md`). **TASK-029 accepted** by Claude CLI (REVIEW-026, MSG-20260621-CLAUDE-09, EVENT-20260621-005) — merge correct by construction, integrated tree byte-identical to the accepted EPIC-003 code, compiles + dry-run smoke clean. Mirrored to Done. Dispatch **Complete**. Unblocks DISPATCH-20260621-002 (TASK-030).

#### Correction

## DISPATCH-20260621-002

Dispatch ID: DISPATCH-20260621-002
Trigger: Thomas authorized Phase 3 integration (2026-06-21), directing `vg_e002` to merge after `vg_e003` is complete.
Related Task: TASK-030
Assigned Agent: Codex CLI
Reviewer: Claude CLI
Action: After TASK-029 (EPIC-003 integration) is **accepted**, integrate EPIC-002 into the v0.3.0 RC from your own Voice_Gen worktree. **(1) Consolidate:** merge the accepted `vg_e002_voice_gen_hardening__codex__TASK-021` (tip `6529caa`) up into the `vg_e002_voice_gen_hardening` epic branch and push (origin epic tip `19372bb` is missing TASK-021). **(2) Merge upward:** merge `vg_e002_voice_gen_hardening` into `vg_e001_shared_config` (which by then contains EPIC-003), resolving EPIC-002-scope conflicts. **(3) Verify:** `py_compile` + `voice_gen.py --help` + `--dry-run` smoke; confirm EPIC-002 and EPIC-003 features coexist. Merge commit `[v0.3.0][vg_e002]`; push `vg_e001_shared_config` (assembled v0.3.0 RC). Submit to Claude CLI with a `tasks/review.md` entry; route the outcome to `comms/watcher_inbox/codex.md`. Prune merged session branches after acceptance.
Status: Complete
Created: 2026-06-21
Updated: 2026-06-21

#### Notes

- Held until TASK-029 lands so EPIC-002 merges on top of the EPIC-003-integrated `vg_e001_shared_config` tip. The Watcher will flip this to Dispatched and broadcast when TASK-029 is accepted.
- **2026-06-21: GATE SATISFIED — activated.** TASK-029 accepted (REVIEW-026, EVENT-20260621-005); `vg_e001_shared_config` now contains EPIC-003 (tip `ffc7b5e`). TASK-030 flipped Pending → Dispatched; Codex notified via broadcast MSG-20260621-003 (EVENT-20260621-006). This is the **final** Phase 3 merge — its acceptance assembles the full v0.3.0 RC.

#### Progress

- 2026-06-21: Codex consolidated accepted TASK-021 (`6529caa`) onto `vg_e002_voice_gen_hardening`, merged EPIC-002 up onto the EPIC-003 RC tip (`ffc7b5e`) with `--no-ff` (merge `5ed908f`), pushed `vg_e001_shared_config`, and submitted for review. **TASK-030 accepted** by Claude CLI (REVIEW-027, MSG-20260621-CLAUDE-10, EVENT-20260621-007) — README conflict resolved as a correct union, both epics' source byte-identical, compiles + integrated RC smoke clean. Mirrored to Done. Dispatch **Complete**. **v0.3.0 RC assembled at `vg_e001_shared_config` `5ed908f` (EVENT-20260621-008).**

Status updated to **Complete** (2026-06-21).
- Watcher-verified branch state (2026-06-21): `6529caa` (TASK-021, accepted REVIEW-024) is **not** an ancestor of `origin/vg_e002_voice_gen_hardening` — consolidation required first.
- Declaring/tagging the final v0.3.0 RC or cutting the release is a Thomas / Quill decision, separate from this merge task.

#### Correction

## DISPATCH-20260621-003

Dispatch ID: DISPATCH-20260621-003
Trigger: Thomas authorized cutting the v0.3.0 release (2026-06-21) and confirmed the release topology: release branch `voice-gen_0.3.0` from the RC + annotated tag `v0.3.0` + advance `main`.
Related Task: TASK-031
Assigned Agent: Codex CLI
Reviewer: Claude CLI
Action: From your own Voice_Gen worktree/clone, cut the **v0.3.0** release from the RC `vg_e001_shared_config` @ `5ed908f` (release mechanics only — no feature-code changes). **(1)** Create release branch `voice-gen_0.3.0` from `5ed908f` and push. **(2)** Create an **annotated** tag `v0.3.0` on the release commit and push the tag. **(3)** Advance `main`: merge `voice-gen_0.3.0` into `main` with `--no-ff` and a `[v0.3.0][RELEASE]` merge commit; push `main`. **(4)** Verify: `git tag` shows `v0.3.0` at the expected commit, `5ed908f` is an ancestor of `origin/main`, `py_compile` clean on the release tip. **(5)** Cleanup: prune the now-fully-merged session + epic branches (`…__codex__TASK-021/030`, `…__gemini__TASK-022_v2/023/024/025`, `vg_e002_voice_gen_hardening`, `vg_e003_text_to_audio_enhancements`) on origin and locally; keep `vg_e001_shared_config`, `voice-gen_0.2.0`, `voice-gen_0.3.0`, `main`. Submit to Claude CLI with a `tasks/review.md` entry; route the outcome to `comms/watcher_inbox/codex.md`.
Status: Complete
Created: 2026-06-21
Updated: 2026-06-21

#### Notes

- Watcher-verified (2026-06-21): all epic/session branches are merged up into the RC `5ed908f`; `main` (`2eb1d32`) is a clean ancestor of the RC (FF-able), but the release merge into `main` should carry an explicit `[v0.3.0][RELEASE]` marker per `branching_strategy.md` Commit Message Policy — hence `--no-ff`.
- This is the final step of Voice_Gen v0.3.0. After acceptance, `v0.3.0` is released and `main` reflects current production.

#### Progress (DISPATCH-20260621-003)

- 2026-06-21: Codex completed and submitted the release cut (MSG-20260621-CODEX-07, EVENT-20260621-010). Watcher-verified on origin: annotated tag `v0.3.0` → `5ed908f`; `voice-gen_0.3.0` = `5ed908f`; `main` @ `ab6dd2a` (`[v0.3.0][RELEASE]`, RC is ancestor); merged session/epic branches pruned (only `main`, `vg_e001_shared_config`, `voice-gen_0.2.0`, `voice-gen_0.3.0` remain). Mirrored as Review; awaiting Claude.
- 2026-06-21: **TASK-031 accepted** by Claude CLI (REVIEW-028, MSG-20260621-CLAUDE-11, EVENT-20260621-011) — all three trees (main/release-branch/tag) byte-identical to the accepted RC, no unmerged work lost in pruning, prior releases retained, compiles. Mirrored to Done. **Voice_Gen v0.3.0 RELEASED** (EVENT-20260621-012). Dispatch **Complete**.

#### Correction

## DISPATCH-20260621-004

Dispatch ID: DISPATCH-20260621-004
Trigger: Thomas observed (2026-06-21) that the `v0.3.0` git tag is not published as a GitHub Release and the CHANGELOG/README don't document v0.3.0; he authorized finalizing the release docs and confirmed the **re-cut / move-tag** approach.
Related Task: TASK-032
Assigned Agent: Codex CLI
Reviewer: Claude CLI
Action: From your own Voice_Gen worktree/clone (docs + release mechanics only — no feature-code changes): **(1)** add a `[v0.3.0]` section to `CHANGELOG.md` (EPIC-001/002/003 changes, dated 2026-06-21, existing changelog style) and update `README.md` to reflect v0.3.0. **(2)** Commit the docs (`[v0.3.0][docs]`). **(3) Re-cut the tag:** move the annotated `v0.3.0` tag to the docs commit (`git tag -f -a v0.3.0`, force-push the tag) so the tagged tree contains the v0.3.0 docs. **(4)** Ensure `main` and `voice-gen_0.3.0` both contain the docs commit (tag/main/release branch converge). **(5) Publish** the v0.3.0 GitHub Release via `gh release create v0.3.0` with notes from the new CHANGELOG section, marked Latest. **(6)** Verify: tag peels to the docs commit, `git show v0.3.0:CHANGELOG.md` has the `[v0.3.0]` section, `gh release view v0.3.0` exists, `py_compile` clean. Submit to Claude CLI (`tasks/review.md`); route outcome to `comms/watcher_inbox/codex.md`.
Status: Dispatched
Created: 2026-06-21
Updated: 2026-06-21

#### Notes

- Moving an already-accepted tag + force-push is **explicitly authorized by Thomas** (2026-06-21, re-cut approach); safe because no GitHub Release is published yet (no consumers).
- Watcher-verified: only `v0.1.0` has a published Release (`gh release list`); CHANGELOG newest entry is `[v0.2.0]`.
- TASK-033 (branch prune) is gated on this task's acceptance.

#### Progress

- 2026-06-21: Codex completed and submitted TASK-032 (MSG-20260621-CODEX-08, EVENT-20260621-014). Watcher-verified on origin + GitHub: docs commit `d18ad52`; annotated tag `v0.3.0` moved → `d18ad52` with `[v0.3.0]` CHANGELOG section present; `voice-gen_0.3.0` = `d18ad52`, `main` = `3402658` (both contain the docs commit); **GitHub Release `Voice_Gen v0.3.0` published, marked Latest**. Mirrored as Review; awaiting Claude. Dispatch stays open until TASK-032 is accepted.

#### Correction

## DISPATCH-20260621-005

Dispatch ID: DISPATCH-20260621-005
Trigger: Thomas sequenced branch pruning after the v0.3.0 docs/Release are finalized ("once those items are updated we can review and prune").
Related Task: TASK-033
Assigned Agent: Codex CLI
Reviewer: Claude CLI
Action: After TASK-032 is **accepted**, review the remaining origin + local branches and prune the unnecessary ones (at minimum `vg_e001_shared_config`, which == the released tree). Ancestry-check each deletion candidate first; keep `main`, `voice-gen_0.2.0`, `voice-gen_0.3.0`, and any branch a tag/release depends on; do not delete tags. Record what was pruned with evidence; submit to Claude CLI (`tasks/review.md`); route outcome to `comms/watcher_inbox/codex.md`.
Status: Pending — gated on TASK-032 acceptance
Created: 2026-06-21
Updated: 2026-06-21

#### Notes

- Session/epic branches were already pruned in TASK-031; remaining origin heads are `main`, `vg_e001_shared_config`, `voice-gen_0.2.0`, `voice-gen_0.3.0`. The Watcher will flip this to Dispatched when TASK-032 is accepted.

#### Correction
