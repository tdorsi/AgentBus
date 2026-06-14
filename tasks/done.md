# Done Tasks

Use this file for tasks that have been reviewed and accepted.

Include the task ID, owner, completion date, and concise completion summary.

## TASK-025: EPIC-003 Documentation and End-to-End Validation

Status: Done (Accepted with Follow-ups)
Owner: Gemini CLI
Completed: 2026-06-14
Approved by: Claude CLI (`reviews/REVIEW-023.md`)

### Completion Summary

EPIC-003 docs accepted. `Voice_Gen/README.md` documents `--keep-chunks` and a new "Progress and ETA" section with sample output; README matches the implemented ETA format. Voice_Gen commit `793a80b`. **FU1 (deferred to Thomas / a test window):** the C4 "recorded real end-to-end run" was simulated, not a real MOSS-TTS synthesis — a real `--keep-chunks` + `--voice all` recorded run still needs GPU/model (Claude declined to run it to avoid contending with live TTS servers, cf. TASK-009). Code paths inspection-verified.

## TASK-024: Add ETA Calculation for Long Inference Runs

Status: Done
Owner: Gemini CLI
Completed: 2026-06-14
Approved by: Claude CLI (`reviews/REVIEW-022.md`)

### Completion Summary

EPIC-003 ETA reporting accepted. `text_to_audio.py` computes ETA from characters-per-second throughput, accounts for remaining voices under `--voice all` (`total_chars_in_file * len(voices)`, per-voice `global_chars_done`), shows "estimating…" before the first chunk, and is division-guarded. Meets REVIEW-015 C3. Voice_Gen commit `3530bd5`. Non-blocking nit (REVIEW-022): redundant input read/split in `main()` — future cleanup.

## TASK-023: Add Progress Reporting for Long Inference Runs

Status: Done
Owner: Gemini CLI
Completed: 2026-06-14
Approved by: Claude CLI (`reviews/REVIEW-021.md`)

### Completion Summary

EPIC-003 progress reporting accepted. `text_to_audio.py` emits a "Processing chunk X of Y" line via the shared `voice_gen_utils` `info()` helper, on real synthesis only (skipped under `--dry-run`/early-exit), with no log interleave. Meets REVIEW-015 C2. Voice_Gen commit `de773cd`.

## TASK-027: AgentBus Working-Tree Isolation (per-agent clones)

Status: Done
Owner: Codex CLI
Completed: 2026-06-14
Approved by: Claude CLI (`reviews/REVIEW-020.md`)

### Completion Summary

Closed the residual single-shared-checkout race on the AgentBus repo itself (RCA-20260613-001, DECISION-20260614-002, Approach A). Created per-agent AgentBus clones under `D:\Development\Sandbox\AgentBus_<agent>` (`stan/codex/claude/gemini/quill`), each with the GitHub `origin`; canonical `D:\Development\AgentBus` is now the human-operated reference checkout. Documented the `git pull --rebase`-before-push model + first-startup self-validation in `agent_startup.md`, `branching_strategy.md`, and `D:\Development\AGENTS.md`; added an `agentbus_health.py` scan for active retired-inbox references (reports 0). AgentBus commit `602e6b5`. Validated by Codex (structural, no impersonation) and accepted by Claude — both operating from their own clones, the first live use of the model. This Watcher pass is the first run from `AgentBus_stan`, completing the Watcher cutover.

## TASK-022: Add `--keep-chunks` Per-Chunk WAV Preservation

Status: Done
Owner: Gemini CLI
Completed: 2026-06-14
Approved by: Claude CLI (`reviews/REVIEW-019.md`)

### Completion Summary

First EPIC-003 task accepted. `text_to_audio.py` gains an optional `--keep-chunks` flag (default OFF, `store_true`) that side-writes each generated chunk as `<stem>_chunk_001.wav` before concatenation; the final WAV is byte-identical with/without the flag (pure side-write, `audio_parts` untouched), and the flag is a no-op under `--dry-run`. All four REVIEW-015 C1 criteria met. Voice_Gen commit `6ba3b98` on `vg_e003_text_to_audio_enhancements__gemini__TASK-022_v2` (branch-name `_v2` deviation noted, non-blocking).

## TASK-020: Add `--log-file` Override (plumbing only)

Status: Done
Owner: Codex CLI
Completed: 2026-06-14
Approved by: Claude CLI (`reviews/REVIEW-018.md`)

### Completion Summary

EPIC-002 hardening task accepted after F1 rework. `voice_gen.py` exposes `--log-file PATH`, threaded into the shared `setup_logging(log_file=...)`; default timestamped log behavior unchanged. REVIEW-016 F1 resolved — `Path(args.log_file).parent.mkdir(parents=True, exist_ok=True)` (guarded by `if args.log_file:`) runs before the handler opens, so a custom path into a non-existent directory no longer raises `FileNotFoundError`. Voice_Gen commits `bf31d45` (initial) + `19372bb` (F1 fix) on `vg_e002_voice_gen_hardening__codex__TASK-020`.

## TASK-026: Implement AgentBus Communication Isolation

Status: Done (Accepted with Follow-ups)
Owner: Codex CLI
Completed: 2026-06-14
Approved by: Claude CLI (`reviews/REVIEW-017.md`)

### Completion Summary

Communication-isolation residual code/infra accepted (AgentBus commit `207e2e9`). `agentbus_health.py` now detects duplicate message IDs across `comms/*` + `comms/watcher_inbox/*` and event/dispatch IDs under `watcher/*`, and flags `sprint_board.md` rows that disagree with merged `tasks/*` (exit 1 gate — RCA P7). README/health-check docs, Watcher startup text cut over to per-agent inboxes, and a Codex startup pointer added at `C:\Users\thoma\.codex\AGENTS.md → D:\Development\AGENTS.md`. Worktree isolation verified (4 trees). Follow-up FU1 (Watcher-owned `DISPATCH-20260613-005` routing reference) fixed by the Watcher in the same pass (EVENT-20260614-008). Cutover is verified and in effect.

## TASK-018: Add Graceful KeyboardInterrupt Handling

Status: Done
Owner: Codex CLI
Completed: 2026-06-13
Approved by: Claude CLI (`reviews/REVIEW-013.md`)

### Completion Summary

Second EPIC-002 task accepted. `voice_gen.py` now wraps execution in a top-level `run_cli()` that catches `KeyboardInterrupt`, prints `Cancelled.` with no traceback, and exits with code 130; other exceptions are unaffected (no bare/`BaseException` handler swallowing Ctrl+C). Minimal and additive. Voice_Gen commit `c2d62e8 [v0.3.0][vg_e002][TASK-018] Add keyboard interrupt handling`.

## TASK-016: Add Voice_Gen Overwrite Protection

Status: Done
Owner: Codex CLI
Completed: 2026-06-13
Approved by: Claude CLI (`reviews/REVIEW-012.md`)

### Completion Summary

First EPIC-002 (Voice_Gen Hardening) task accepted. `voice_gen.py` now has fail-by-default overwrite protection that exits before any write on collision risk, a `--from-stage` resume carve-out (resume into an existing output dir is permitted, not a collision), and a logged `--force` override — all matching DECISION-20260613-004. Additive with no regression; README and the EPIC-002 detail file updated. Voice_Gen commit `9a52d61 [v0.3.0][vg_e002][TASK-016] Add overwrite protection`.

## TASK-015: Implement Watcher Governance Model v1

Status: Done
Owner: Codex CLI
Completed: 2026-06-13
Approved by: Claude CLI (`reviews/REVIEW-010.md`)

### Completion Summary

Implemented the additive, role-based AgentBus Watcher Governance Model v1. Added Watcher rules, routing table, dispatch queue, event log, Watcher inbox, and sprint board; updated README and AgentBus state records; documented correction procedure, broadcast ownership, and state ownership; recorded and reviewed the required end-to-end validation cycle. Claude CLI accepted all acceptance criteria and REVIEW-009 conditions C1-C5.

## TASK-009: Perform Lori Runtime Audio Validation

Status: Done
Owner: Thomas / Codex CLI
Completed: 2026-06-01
Approved by: Thomas

### Completion Summary

Lori MOSS-TTS server started successfully on port 8766. Codex verified the health endpoint returned ready, queued a direct synthesis request, confirmed the queue drained, and Thomas confirmed the Lori voice test passed. Runtime validation for TASK-008 is complete.

## TASK-008: Set Up Codex CLI TTS with Lori Voice

Status: Done
Owner: Codex CLI
Completed: 2026-05-31
Approved by: Thomas / Quill (DECISION-20260531-003)

### Completion Summary

All implementation files in place: `tts_server_win.py` updated to accept `--config`, `--reference`, and `--port` CLI args; `lori.yaml` created; Lori server launcher created; Codex CLI TTS hook script created and registered. Live audio confirmation deferred to TASK-009 — runtime validation blocked pending available GPU memory or a planned test window. Hannah server on port 8765 unaffected.

## TASK-001: Validate AgentBus workflow

Status: Done
Owner: Claude CLI
Completed: 2026-05-31
Approved by: Human operator

### Completion Summary

Full AgentBus task lifecycle validated end-to-end. Claude CLI claimed the task, broadcast to all agents, executed a cross-agent message round-trip with Codex CLI, logged all work, and submitted for review. All acceptance criteria met. Both agents followed message ID, log, and inbox conventions correctly on first run.
## TASK-019: Log Dependency Checks Correctly

Status: Done — accepted by Claude CLI 2026-06-13
Owner: Codex CLI
Reviewer: Claude CLI
Completed: 2026-06-13
Related Epic: EPIC-002 Voice_Gen Hardening
Related Branch: `vg_e002_voice_gen_hardening`
Related Review: REVIEW-014
Commit: `8b993a5 [v0.3.0][vg_e002][TASK-019] Log dependency check failures`

### Summary

Moved Voice_Gen dependency checks after run logging initialization so ffmpeg/ffprobe failures are captured in the generated log file while preserving console messaging and explicit failure exit behavior.
