# Active Tasks

Use this file for tasks that are claimed and in progress. Each active task should have one owner and a task ID.

Append updates beneath the relevant task. Do not remove history; move or summarize completed work only after review.

## TASK-011: Establish EPIC-001 Branch and Shared Configuration Architecture

Status: Review complete - accepted
Owner: Codex CLI
Reviewer: Claude CLI
Priority: High
Claimed: 2026-06-01
Updated: 2026-06-01
Related Epic: EPIC-001 Shared Configuration Framework
Related Branch: `vg_e001_shared_config`

### Goal

Start EPIC-001 by establishing the `vg_e001_shared_config` branch and defining the shared configuration/utility architecture before code migration.

### Work Notes

- 2026-06-01: Codex CLI claimed TASK-011 after Thomas requested EPIC-001 split into TASK-011 through TASK-014. Claude CLI is assigned as architecture reviewer while Codex performs implementation.
- 2026-06-01: Codex CLI created and pushed TASK-011 architecture notes on `vg_e001_shared_config` in commit `3ca96ad`: `docs/architecture/EPIC-001_shared_configuration_architecture.md`.
- 2026-06-01: Claude CLI reviewed architecture. Result: Accepted. See REVIEW-004. TASK-012 cleared to begin.

## TASK-012: Extract Shared Voice_Gen Utility Module

Status: Review complete - accepted
Owner: Codex CLI
Reviewer: Claude CLI
Priority: High
Claimed: 2026-06-01
Updated: 2026-06-01
Related Epic: EPIC-001 Shared Configuration Framework
Related Branch: `vg_e001_shared_config`

### Goal

Create `voice_gen_utils.py` and migrate shared terminal UI, logging, and prompt helpers from `voice_gen.py` and `text_to_audio.py`.

### Work Notes

- 2026-06-01: Codex CLI implemented shared utility extraction on `vg_e001_shared_config` in commit `b3ffc83`: `[v0.3.0][vg_e001][TASK-012] Extract shared utility helpers`.
- 2026-06-01: Verification completed: `python -m py_compile voice_gen_utils.py text_to_audio.py voice_gen.py`; `C:\Users\thoma\.conda\envs\moss-tts\python.exe text_to_audio.py --input D:\Training_Data\Audio\Test_Script\TTS_Script_01.txt --voice hannah --dry-run`; `python voice_gen.py --help`.
- 2026-06-01: Claude CLI reviewed. Result: Accepted. See REVIEW-005. TASK-013 cleared to begin.

## TASK-013: Implement Shared Voice_Gen Configuration System

Status: Review
Owner: Codex CLI
Reviewer: Claude CLI
Priority: High
Claimed: 2026-06-02
Updated: 2026-06-02
Related Epic: EPIC-001 Shared Configuration Framework
Related Branch: `vg_e001_shared_config`

### Goal

Create `voice_gen.toml` and load shared path/default settings from configuration instead of embedding operational defaults in each script.

### Work Notes

- 2026-06-02: Codex CLI implemented and pushed shared configuration loading on `vg_e001_shared_config` in commit `9564716`: `[v0.3.0][vg_e001][TASK-013] Add shared configuration system`.
- 2026-06-02: Verification completed: `python -m py_compile voice_gen_config.py voice_gen_utils.py text_to_audio.py voice_gen.py`; `python voice_gen.py --help`; `C:\Users\thoma\.conda\envs\moss-tts\python.exe text_to_audio.py --input D:\Training_Data\Audio\Test_Script\TTS_Script_01.txt --voice hannah --dry-run`; cross-directory dry-run from `D:\Development\AgentBus`.

## TASK-001: Validate AgentBus workflow

Status: Review — moved to tasks/review.md 2026-05-31 11:26
Owner: Claude CLI
Priority: High
Claimed: 2026-05-31
Updated: 2026-05-31

### Goal

Validate that agents can coordinate through AgentBus using the expected task, message, log, review, and decision flow.

### Work Notes

- 2026-05-31 11:24 — Claude CLI claimed this task. Reading sprint, rules, and inbox per agent_rules.md. Broadcasting claim and messaging Codex CLI to participate in cross-agent communication test.

## TASK-004: Build README Usage Instructions for Health Check CLI

Status: Review — moved to tasks/review.md 2026-05-31
Owner: Claude CLI
Priority: Medium
Claimed: 2026-05-31
Updated: 2026-05-31

### Goal

Document how to run and interpret the AgentBus Health Check CLI.

### Work Notes

- 2026-05-31 12:30 — Claude CLI claimed TASK-004. Thomas approved start. Reading README.md and agentbus_health.py before writing.

## TASK-003: Build AgentBus Health Check CLI

Status: Review
Owner: Codex CLI
Priority: High
Claimed: 2026-05-31
Updated: 2026-05-31

### Goal

Build a CLI that reads the AgentBus workspace and reports coordination health.

### Work Notes

- 2026-05-31 12:10 — Codex CLI claimed this task after completing and pushing TASK-002.
- 2026-05-31 12:18 — Codex CLI implemented `agentbus_health.py`, verified runtime output, and compiled the file successfully.

## TASK-006: Establish AgentBus Rules of Engagement and State Monitoring

Status: Review
Owner: Codex CLI
Priority: High
Claimed: 2026-06-01
Updated: 2026-06-01

### Goal

Establish clear rules of engagement and state monitoring for AgentBus agents.

### Work Notes

- 2026-06-01 — Codex CLI claimed TASK-006, created governance procedures and state files, and submitted for Claude review.

## TASK-007: Align Review Workflow Documentation

Status: Review
Owner: Codex CLI
Priority: Medium
Claimed: 2026-06-01
Updated: 2026-06-01

### Goal

Align AgentBus documentation and procedures with the implemented review workflow.

### Work Notes

- 2026-06-01 — Codex CLI claimed TASK-007, aligned review workflow documentation, and submitted for Claude review.

## TASK-008: Set Up Codex CLI TTS with Lori Voice

Status: Done — accepted 2026-05-31 per DECISION-20260531-003
Owner: Codex CLI
Priority: Medium
Claimed: 2026-06-01
Updated: 2026-05-31

### Goal

Configure Codex CLI with a TTS hook that speaks Codex responses aloud using the MOSS-TTS server and the Lori voice, without disrupting Claude CLI's Hannah server.

### Work Notes

- 2026-06-01 — Codex CLI claimed TASK-008.
- 2026-05-31 — Thomas / Quill accepted as setup-complete. Runtime validation deferred to TASK-009.
- Added CLI args to `tts_server_win.py` while preserving Hannah defaults.
- Added Lori config and launcher for port 8766.
- Created Codex TTS hook and `hooks.json` registration.
- Validated Python syntax, PowerShell hook syntax, hooks JSON, and Codex doctor.

### Blockers

- Runtime acceptance requires Thomas to confirm Lori audio is audible from an actual Codex response.
- Codex may require hook trust approval/reload before the new Stop hook runs.
- Lori server is not started because Hannah is running and GPU memory has only ~261 MB free.
