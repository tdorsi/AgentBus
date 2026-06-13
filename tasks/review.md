# Review Queue

Use this file for tasks that are ready for human or assigned agent review.

Include the task ID, owner, summary of completed work, files changed, and specific review request.

## TASK-015: Implement Watcher Governance Model v1

Status: Review
Owner: Codex CLI
Reviewer: Claude CLI
Submitted: 2026-06-13
Related Decisions: DECISION-20260613-001, DECISION-20260613-002, DECISION-20260613-003
Related Review: REVIEW-009

### Summary of Completed Work

- Added Watcher governance rules defining responsibilities, authority, allowed/forbidden actions, state ownership, correction procedure, broadcast ownership, and operating procedures.
- Added Watcher routing table for review outcomes, task completions, blockers, direct agent questions, team announcements, durable decisions, and sync events.
- Added Watcher dispatch queue with a template and `DISPATCH-20260613-001` assigning TASK-015 to Codex CLI.
- Added Watcher event log with the required validation sequence.
- Added `comms/inbox_watcher.md` and seeded it with the validation input and response.
- Added `state/sprint_board.md` as a Watcher-owned aggregate board derived from `tasks/*`.
- Updated README with Watcher role, routing model, state ownership, and dispatch workflow.
- Updated AgentBus task/status/log/snapshot records for TASK-015.

### Files Changed

- `README.md`
- `watcher/watcher_rules.md`
- `watcher/routing_table.md`
- `watcher/dispatch_queue.md`
- `watcher/event_log.md`
- `comms/inbox_watcher.md`
- `comms/broadcast.md`
- `state/sprint_board.md`
- `state/agent_status.md`
- `state/state_snapshot.md`
- `state/sync_log.md`
- `tasks/backlog.md`
- `tasks/active.md`
- `tasks/review.md`
- `logs/codex.md`

### Validation

- Confirmed all required files exist.
- Ran `python .\agentbus_health.py`; it detects TASK-015 and reports no blocked tasks. It still reports five older stale review messages with empty response sections from prior work.
- Verified the TASK-015 validation cycle is recorded:
  - Review Accepted: `watcher/event_log.md` EVENT-20260613-001.
  - Board Updated: `state/sprint_board.md`.
  - Event Logged: `watcher/event_log.md` EVENT-20260613-001 through EVENT-20260613-004.
  - Dispatch Generated: `watcher/dispatch_queue.md` DISPATCH-20260613-001.
  - Broadcast Generated: `comms/broadcast.md` MSG-20260613-003.
- Searched for `[v0.3.0]` in the new Watcher implementation surfaces; only pre-existing Voice_Gen history and the REVIEW-009 condition remain.

### Review Request

Claude CLI: review TASK-015 against REVIEW-009 conditions C1-C5, additive governance compatibility, routing clarity, correction procedure, state ownership, and the recorded validation cycle.

### Review Outcome

Reviewer: Claude CLI
Date: 2026-06-13
Result: Accepted

All TASK-015 acceptance criteria met; all five REVIEW-009 conditions (C1-C5) satisfied; additive compatibility preserved; end-to-end validation cycle recorded. See `reviews/REVIEW-010.md`. Watcher Governance Model v1 is in place. Recommend TASK-015 move to done.

### Review Outcome

## TASK-012: Extract Shared Voice_Gen Utility Module

Status: Review
Owner: Codex CLI
Reviewer: Claude CLI
Submitted: 2026-06-01
Related Branch: `vg_e001_shared_config`
Commit: `b3ffc83 [v0.3.0][vg_e001][TASK-012] Extract shared utility helpers`

### Summary of Completed Work

- Added `voice_gen_utils.py` for shared console formatting, logging setup, prompt helpers, and safe console fallback behavior.
- Updated `voice_gen.py` to use shared helper wrappers while preserving existing stage behavior and command-line interface.
- Updated `text_to_audio.py` to use shared helper wrappers while preserving existing dry-run, timestamped output, and inference workflow behavior.
- Added safe fallback for Unicode separator/status symbols on Windows consoles that cannot encode box-drawing characters.

### Files Changed

- `voice_gen_utils.py`
- `voice_gen.py`
- `text_to_audio.py`

### Verification

- `python -m py_compile voice_gen_utils.py text_to_audio.py voice_gen.py`
- `C:\Users\thoma\.conda\envs\moss-tts\python.exe text_to_audio.py --input D:\Training_Data\Audio\Test_Script\TTS_Script_01.txt --voice hannah --dry-run`
- `python voice_gen.py --help`

### Review Request

Claude CLI: review whether TASK-012 satisfies the shared utility module acceptance criteria, preserves existing workflow behavior, and keeps training/inference-specific logic out of `voice_gen_utils.py`.

### Review Outcome

Reviewer: Claude CLI
Date: 2026-06-01
Result: Accepted

See `reviews/REVIEW-005.md`. TASK-013 cleared to begin.

## TASK-013: Implement Shared Voice_Gen Configuration System

Status: Review
Owner: Codex CLI
Reviewer: Claude CLI
Submitted: 2026-06-02
Related Branch: `vg_e001_shared_config`
Commit: `9564716 [v0.3.0][vg_e001][TASK-013] Add shared configuration system`

### Summary of Completed Work

- Added `voice_gen_config.py` with typed config loading, path normalization, default merging, clear config errors, and runtime path validation.
- Added repository-root `voice_gen.toml` with shared path settings, MOSS runtime paths, and voice preset sections for TASK-014 migration.
- Updated `text_to_audio.py` to load shared path/default settings, log the active config file, validate runtime paths, and use configured interactive input/output defaults.
- Updated `voice_gen.py` to load shared path/default settings, log the active config file, validate runtime paths, and use the configured default output root.
- Updated README with the config file location, sections, keys, and error behavior.

### Files Changed

- `voice_gen_config.py`
- `voice_gen.toml`
- `voice_gen.py`
- `text_to_audio.py`
- `README.md`

### Verification

- `python -m py_compile voice_gen_config.py voice_gen_utils.py text_to_audio.py voice_gen.py`
- `python voice_gen.py --help`
- `C:\Users\thoma\.conda\envs\moss-tts\python.exe text_to_audio.py --input D:\Training_Data\Audio\Test_Script\TTS_Script_01.txt --voice hannah --dry-run`
- `C:\Users\thoma\.conda\envs\moss-tts\python.exe D:\Development\Voice_Gen\text_to_audio.py --input D:\Training_Data\Audio\Test_Script\TTS_Script_01.txt --voice hannah --dry-run` from `D:\Development\AgentBus`

### Review Request

Claude CLI: review TASK-013 for config layout, module-relative `voice_gen.toml` anchoring, path validation behavior, compatibility with existing workflows, and readiness for TASK-014 voice preset migration.

### Review Outcome

Reviewer: Claude CLI
Date: 2026-06-02
Result: Accepted

All acceptance criteria met. Critical item from REVIEW-004 (`Path(__file__).parent` anchor) confirmed correct. See `reviews/REVIEW-006.md`. TASK-014 cleared to begin.

## TASK-014: Migrate Voice Presets and Default Paths to Configuration

Status: Review
Owner: Codex CLI
Reviewer: Claude CLI
Submitted: 2026-06-04
Related Branch: `vg_e001_shared_config`
Commit: `a83550f [v0.3.0][vg_e001][TASK-014] Migrate voice presets to configuration`

### Summary of Completed Work

- Removed the hardcoded `VoicePreset` dataclass and Lori/Lilybelle/Hannah registry from `text_to_audio.py`.
- Made `APP_CONFIG.voices` the authoritative, discoverable voice registry for CLI choices, interactive choices, preset lookup, and `--voice all`.
- Added configurable `[text_to_audio] default_voice` with validation that the selected default exists.
- Preserved configured interactive input/output defaults and timestamped output collision behavior.
- Documented adding a new voice preset, changing the default voice, and `--voice all` behavior.

### Files Changed

- `text_to_audio.py`
- `voice_gen_config.py`
- `voice_gen.toml`
- `README.md`

### Verification

- `python -m py_compile voice_gen_config.py voice_gen_utils.py text_to_audio.py voice_gen.py`
- `C:\Users\thoma\.conda\envs\moss-tts\python.exe text_to_audio.py --help`
- `C:\Users\thoma\.conda\envs\moss-tts\python.exe text_to_audio.py --input D:\Training_Data\Audio\Test_Script\TTS_Script_01.txt --voice all --dry-run`
- `C:\Users\thoma\.conda\envs\moss-tts\python.exe text_to_audio.py --input D:\Training_Data\Audio\Test_Script\TTS_Script_01.txt --dry-run`
- Interactive blank-response dry-run confirmed configured input, output directory, and default voice.
- Temporary TOML test confirmed a new `[voices.custom]` preset is discovered without Python changes.
- Hardcode scan found no Lori/Lilybelle/Hannah names or training-data paths in `text_to_audio.py`.

### Review Request

Claude CLI: review TASK-014 for complete removal of hardcoded voice presets/defaults from `text_to_audio.py`, configured voice discovery, default voice validation, `--voice all` behavior, output collision preservation, and EPIC-001 completion readiness.

### Review Outcome

Reviewer: Claude CLI
Date: 2026-06-04
Result: Accepted

All acceptance criteria met. Hardcoded presets fully removed; `APP_CONFIG.voices` is now the authoritative registry. Default voice configurable and validated at load time. See `reviews/REVIEW-007.md`. EPIC-001 is complete.

## TASK-003: Build AgentBus Health Check CLI

Owner: Codex CLI
Ready: 2026-05-31

### Summary

Implemented `agentbus_health.py`, a standard-library Python CLI that reads the AgentBus workspace and reports active tasks, blocked tasks, messages needing response, recent decisions, and last update timing for key coordination files.

### Files Changed

- `agentbus_health.py`
- `.gitignore`
- `tasks/active.md`
- `tasks/backlog.md`

### Review Request

Thomas / Quill: review CLI output and confirm whether it satisfies the Health Check POC expectations for TASK-005.

## TASK-001: Validate AgentBus workflow

Status: Review
Owner: Claude CLI
Submitted: 2026-05-31 11:26

### Summary of Completed Work

- Claude CLI claimed TASK-001 and executed full task lifecycle.
- Cross-agent message round-trip completed with Codex CLI via MSG-20260531-001 through MSG-20260531-003.
- All agents logged work in their respective log files.
- All messages used correct IDs and templates.

### Files Changed

- tasks/active.md — TASK-001 claimed and tracked
- tasks/backlog.md — marked as claimed
- sprint.md — agent assignment updated
- logs/claude.md — two log entries appended
- logs/codex.md — one log entry appended by Codex CLI
- comms/broadcast.md — MSG-20260531-001 posted
- comms/inbox_codex.md — MSG-20260531-002 sent, response acknowledged
- comms/inbox_claude.md — MSG-20260531-003 received from Codex CLI

### Review Request

Human operator: please confirm all acceptance criteria are satisfied and approve move to tasks/done.md.

Approved and moved to tasks/done.md — 2026-05-31 by human operator.

## TASK-004: Build README Usage Instructions for Health Check CLI

Status: Review
Owner: Claude CLI
Submitted: 2026-05-31

### Summary of Completed Work

- Added `## Health Check CLI` section to `README.md`.
- Covers requirements, usage, all CLI flags, annotated output example, exit code table, and troubleshooting for the three most likely issues.
- No local paths, secrets, or runtime-specific details included.
- Documentation is consistent with `agentbus_health.py` as implemented by Codex CLI in TASK-003.

### Files Changed

- README.md
- tasks/active.md
- tasks/backlog.md
- logs/claude.md

### Review Request

Quill / Thomas: please confirm documentation is accurate, complete, and meets TASK-004 acceptance criteria. Ready to move to done on approval.

## TASK-006: Establish AgentBus Rules of Engagement and State Monitoring

Status: Review
Owner: Codex CLI
Submitted: 2026-06-01

### Summary of Completed Work

- Added startup, task claiming, and review response procedures.
- Standardized update-check behavior around `origin/main` as source of truth.
- Added sync and state snapshot files.
- Updated README, sprint, and broadcast with governance changes.

### Files Changed

- `README.md`
- `sprint.md`
- `comms/broadcast.md`
- `procedures/check_for_updates.md`
- `procedures/agent_startup.md`
- `procedures/task_claiming.md`
- `procedures/review_response.md`
- `state/sync_log.md`
- `state/state_snapshot.md`
- `tasks/backlog.md`
- `tasks/active.md`
- `tasks/review.md`

### Review Request

Claude CLI: review the rules of engagement and state monitoring procedures for clarity and usability by local agents.

### Review Outcome

Reviewer: Claude CLI
Date: 2026-05-31
Result: Accepted

All acceptance criteria met. Procedures are clear and actionable. The `reviews/` directory exists on disk and is in use — the procedure references are valid. Two non-blocking observations recorded in reviews/REVIEW-002.md. TASK-006 approved to move to done.

## TASK-007: Align Review Workflow Documentation

Status: Review
Owner: Codex CLI
Submitted: 2026-06-01

### Summary of Completed Work

- Added `reviews/` to the README directory overview.
- Added explicit review workflow guidance to README and `procedures/README.md`.
- Updated `procedures/review_response.md` to describe review artifact discovery and stale-state revalidation.
- Updated `procedures/check_for_updates.md` to include review synchronization behavior.
- Included `reviews/REVIEW-002.md` so the shared repository contains the TASK-006 review artifact.

### Files Changed

- `README.md`
- `procedures/README.md`
- `procedures/review_response.md`
- `procedures/check_for_updates.md`
- `reviews/REVIEW-002.md`
- `tasks/backlog.md`
- `tasks/active.md`
- `tasks/review.md`
- `comms/broadcast.md`
- `comms/inbox_claude.md`
- `state/agent_status.md`
- `state/sync_log.md`
- `state/state_snapshot.md`

### Review Request

Claude CLI: review whether TASK-007 fully resolves the stale review-directory finding from TASK-006 and makes review artifacts discoverable for all agents.

### Review Outcome

Reviewer: Claude CLI
Date: 2026-05-31
Result: Accepted

All acceptance criteria met. Stale-state governance rule documented in three independent locations (procedures/README.md, review_response.md, check_for_updates.md). REVIEW-002 committed to origin/main. TASK-007 approved to move to done. See reviews/REVIEW-003.md.
