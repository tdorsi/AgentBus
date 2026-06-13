# Backlog

Use this file for known work that is not currently claimed. Append new tasks using `task_template.md`.

## TASK-011: Establish EPIC-001 Branch and Shared Configuration Architecture

Status: Active - claimed by Codex CLI 2026-06-01
Owner: Codex CLI
Reviewer: Claude CLI
Priority: High
Created: 2026-06-01
Updated: 2026-06-01
Related Epic: EPIC-001 Shared Configuration Framework
Related Branch: `vg_e001_shared_config`
Related Files: `procedures/branching_strategy.md`, `artifacts/Planning/PR_Voice_Gen/epics/EPIC-001_shared_configuration_framework.md`, `D:\Development\Voice_Gen\voice_gen.py`, `D:\Development\Voice_Gen\text_to_audio.py`

### Goal

Start EPIC-001 by establishing the `vg_e001_shared_config` branch and defining the shared configuration/utility architecture before code migration.

### Context

EPIC-001 is the prerequisite for Voice_Gen v0.3.0. The branching strategy requires an Epic integration branch named `vg_e001_shared_config`. Claude should review the architecture while Codex performs implementation.

### Acceptance Criteria

- `vg_e001_shared_config` exists and is based on `voice-gen_0.2.0`.
- The branch relationship follows `procedures/branching_strategy.md`.
- Codex documents the proposed architecture for `voice_gen_utils.py` and `voice_gen.toml`.
- Codex identifies migration boundaries for `voice_gen.py` and `text_to_audio.py`.
- Claude CLI reviews the architecture before broad implementation proceeds.
- Follow-up implementation tasks remain aligned with TASK-012 through TASK-014.

### Work Notes

- 2026-06-01: Created from EPIC-001 planning documents. Codex assigned implementation ownership; Claude assigned architecture review.

### Blockers

- None.

### Review Notes

### Completion Summary

## TASK-012: Extract Shared Voice_Gen Utility Module

Status: Review - submitted by Codex CLI 2026-06-01
Owner: Codex CLI
Reviewer: Claude CLI
Priority: High
Created: 2026-06-01
Updated: 2026-06-01
Related Epic: EPIC-001 Shared Configuration Framework
Related Branch: `vg_e001_shared_config`
Related Files: `D:\Development\Voice_Gen\voice_gen.py`, `D:\Development\Voice_Gen\text_to_audio.py`, `D:\Development\Voice_Gen\voice_gen_utils.py`

### Goal

Create `voice_gen_utils.py` and migrate shared terminal UI, logging, and prompt helpers from `voice_gen.py` and `text_to_audio.py`.

### Context

Claude's v0.2.0 review found duplicated banner, console formatting, logging setup, status helpers, and prompt behavior. EPIC-001 requires both applications to use shared utility functions.

### Acceptance Criteria

- `voice_gen_utils.py` provides shared banner, header, status, logging, and prompt helpers.
- `voice_gen.py` imports and uses shared helpers without changing existing training behavior.
- `text_to_audio.py` imports and uses shared helpers without changing existing inference behavior.
- Existing command-line workflows continue to run.
- Syntax checks pass for all touched Python files.
- Claude CLI reviews utility architecture and migration quality.

### Work Notes

- 2026-06-01: Codex CLI implemented and pushed commit `b3ffc83` on `vg_e001_shared_config`.

### Blockers

### Review Notes

### Completion Summary

## TASK-013: Implement Shared Voice_Gen Configuration System

Status: Review complete - accepted by Claude CLI 2026-06-02
Owner: Codex CLI
Reviewer: Claude CLI
Priority: High
Created: 2026-06-01
Updated: 2026-06-02
Related Epic: EPIC-001 Shared Configuration Framework
Related Branch: `vg_e001_shared_config`
Related Files: `D:\Development\Voice_Gen\voice_gen.toml`, `D:\Development\Voice_Gen\voice_gen.py`, `D:\Development\Voice_Gen\text_to_audio.py`

### Goal

Create `voice_gen.toml` and load shared path/default settings from configuration instead of embedding operational defaults in each script.

### Context

EPIC-001 requires a shared configuration system for `MOSS_ROOT`, `LOG_DIR`, `VOICES_DIR`, `DEFAULT_OUTPUT_DIR`, and `DEFAULT_INPUT_FILE`. This is also the foundation for later Voice_Gen hardening and Text_to_Audio enhancements.

### Acceptance Criteria

- `voice_gen.toml` exists at the Voice_Gen repository root.
- Both applications can load shared configuration successfully.
- Configuration includes `MOSS_ROOT`, `LOG_DIR`, `VOICES_DIR`, `DEFAULT_OUTPUT_DIR`, and `DEFAULT_INPUT_FILE`.
- Reasonable defaults preserve the current local workflow.
- Missing or invalid config values produce clear logged errors.
- README or adjacent docs explain the configuration file.

### Work Notes

- 2026-06-02: Codex CLI implemented and pushed commit `9564716` on `vg_e001_shared_config`.

### Blockers

### Review Notes

### Completion Summary

## TASK-014: Migrate Voice Presets and Default Paths to Configuration

Status: Review - submitted by Codex CLI 2026-06-04
Owner: Codex CLI
Reviewer: Claude CLI
Priority: High
Created: 2026-06-01
Updated: 2026-06-04
Related Epic: EPIC-001 Shared Configuration Framework
Related Branch: `vg_e001_shared_config`
Related Files: `D:\Development\Voice_Gen\voice_gen.toml`, `D:\Development\Voice_Gen\text_to_audio.py`, `D:\Development\Voice_Gen\README.md`

### Goal

Remove hardcoded voice presets and default input/output paths from `text_to_audio.py` by making them configuration-driven and discoverable.

### Context

EPIC-001 acceptance criteria require that no hardcoded voice presets or hardcoded default paths remain. Future voices created by `voice_gen.py` should become available to `text_to_audio.py` without source-code edits.

### Acceptance Criteria

- Built-in voice presets are loaded from configuration and/or discovered from configured voice/config directories.
- `text_to_audio.py` no longer hardcodes Lori, Lilybelle, Hannah, default input file, or default output directory in source.
- Existing Lori, Lilybelle, and Hannah workflows continue functioning.
- Interactive prompts use configured defaults.
- Output collision behavior remains intact.
- README documents how to add or discover a new voice preset.

### Work Notes

- 2026-06-04: Codex CLI implemented and pushed commit `a83550f` on `vg_e001_shared_config`.

### Blockers

### Review Notes

### Completion Summary

## TASK-001: Validate AgentBus workflow

Status: Active — claimed by Claude CLI 2026-05-31
Owner: Claude CLI
Priority: High
Created: 2026-05-31
Updated: 2026-05-31
Related Files: `sprint.md`, `agent_rules.md`, `tasks/active.md`, `tasks/review.md`, `tasks/done.md`, `comms/`, `logs/`

### Goal

Validate that agents can coordinate through AgentBus using the expected task, message, log, review, and decision flow.

### Context

AgentBus has been bootstrapped as a markdown-only coordination workspace.

### Acceptance Criteria

- One agent claims this task in `tasks/active.md`.
- The agent appends at least one log entry.
- Any cross-agent or human request uses a message ID.
- The task reaches `tasks/review.md`, then `tasks/done.md` after review.

### Work Notes

### Blockers

### Review Notes

### Completion Summary

## TASK-007: Align Review Workflow Documentation

Status: Review
Owner: Codex CLI
Priority: Medium
Created: 2026-06-01
Updated: 2026-06-01
Related Files: `README.md`, `procedures/README.md`, `procedures/review_response.md`, `procedures/check_for_updates.md`, `reviews/`

### Goal

Align AgentBus documentation and procedures with the implemented review workflow.

### Context

During TASK-006 review, Claude reported a possible missing `reviews/` directory. Subsequent investigation confirmed `reviews/README.md`, `reviews/review_template.md`, and review artifacts exist. The follow-up is to make review discovery and review workflow behavior explicit.

### Acceptance Criteria

- `README.md` references the `reviews/` directory.
- `procedures/README.md` references the review workflow.
- `procedures/review_response.md` aligns with the actual reviews structure.
- `procedures/check_for_updates.md` explicitly includes review synchronization behavior.
- Review artifacts are discoverable by all agents.
- Stale-state assumptions are documented as governance guidance.

### Work Notes

- 2026-06-01: Codex CLI aligned review workflow documentation and stale-state guidance.

### Blockers

- None.

### Review Notes

- Submitted for Claude review.

### Completion Summary

## TASK-006: Establish AgentBus Rules of Engagement and State Monitoring

Status: Review
Owner: Codex CLI
Priority: High
Created: 2026-06-01
Updated: 2026-06-01
Related Files: `README.md`, `sprint.md`, `comms/broadcast.md`, `procedures/`, `state/`

### Goal

Establish clear rules of engagement and state monitoring for AgentBus agents.

### Context

Thomas requested governance procedures and state files so agents consistently treat GitHub `origin/main` as source of truth, standardize update checks, and have clear startup, task claiming, review response, and state monitoring processes.

### Acceptance Criteria

- `procedures/agent_startup.md` exists.
- `procedures/task_claiming.md` exists.
- `procedures/review_response.md` exists.
- `state/sync_log.md` exists.
- `state/state_snapshot.md` exists.
- `README.md`, `sprint.md`, and `comms/broadcast.md` are updated.
- `procedures/check_for_updates.md` is standardized around `origin/main`.
- TASK-006 is submitted for Claude review.

### Work Notes

- 2026-06-01: Codex CLI created governance procedures and state monitoring files.

### Blockers

- None.

### Review Notes

- Submitted to Claude CLI for review.

### Completion Summary

## TASK-002: Establish AgentBus POC Team Structure

Status: Review
Owner: Codex CLI
Priority: High
Created: 2026-05-31
Updated: 2026-05-31
Related Files: `roles.md`, `sprint.md`, `tasks/backlog.md`, `decisions/decision_log.md`, `comms/broadcast.md`

### Goal

Establish the planning structure for the AgentBus Health Check CLI proof of concept.

### Context

Quill requested this task in `MSG-20260531-004` after Thomas approved the next AgentBus POC. `roles.md` defines Thomas as Product Owner, Quill as Senior Analyst / PM, and Claude CLI plus Codex CLI as the Development Team.

### Acceptance Criteria

- `roles.md` exists and is referenced.
- `sprint.md` reflects the Health Check CLI POC sprint.
- `tasks/backlog.md` includes TASK-002 through TASK-005.
- `decisions/decision_log.md` records the approved role model and POC direction.
- `comms/broadcast.md` announces the POC and next steps to all agents.
- Changes are committed and pushed to `main`.

### Work Notes

- 2026-05-31: Codex CLI established the POC sprint structure and task breakdown.

### Blockers

- None.

### Review Notes

- Ready for Quill review after commit and push.

### Completion Summary

- POC planning structure created and announced.

## TASK-003: Build AgentBus Health Check CLI

Status: Review
Owner: Codex CLI
Priority: High
Created: 2026-05-31
Updated: 2026-05-31
Related Files: `sprint.md`, `roles.md`, `tasks/`, `comms/`, `decisions/`

### Goal

Build a CLI that reads the AgentBus workspace and reports coordination health.

### Context

The CLI should support the Health Check POC by summarizing active tasks, blocked tasks, messages needing response, recent decisions, and last update timing.

### Acceptance Criteria

- CLI can run locally from the AgentBus repository.
- CLI reports active tasks and blocked tasks.
- CLI reports messages that appear to need response.
- CLI reports recent decisions.
- CLI reports last update timing for key coordination files.
- CLI avoids reading ignored runtime output as primary input.

### Work Notes

- 2026-05-31: Codex CLI claimed this task after completing TASK-002.
- 2026-05-31: Codex CLI implemented `agentbus_health.py`; runtime and compile checks pass.

### Blockers

### Review Notes

- Ready for TASK-005 review by Thomas / Quill.

### Completion Summary

## TASK-004: Build README Usage Instructions for Health Check CLI

Status: Active — claimed by Claude CLI 2026-05-31
Owner: Claude CLI
Priority: Medium
Created: 2026-05-31
Updated: 2026-05-31
Related Files: `README.md`, `git_notes.md`, Health Check CLI files

### Goal

Document how to run and interpret the AgentBus Health Check CLI.

### Context

Claude CLI owns usage documentation after Codex CLI establishes the CLI behavior.

### Acceptance Criteria

- README or appropriate documentation includes CLI usage.
- Instructions explain expected output and basic troubleshooting.
- Documentation does not expose secrets or local-only runtime details.

### Work Notes

### Blockers

### Review Notes

### Completion Summary

## TASK-005: Review and Test Health Check CLI

Status: Backlog
Owner: Thomas / Quill
Priority: High
Created: 2026-05-31
Updated: 2026-05-31
Related Files: Health Check CLI files, `README.md`, `sprint.md`

### Goal

Review and test the Health Check CLI against the approved POC goals.

### Context

Thomas owns final acceptance. Quill coordinates review and synthesizes findings.

### Acceptance Criteria

- CLI output is useful for Product Owner and PM review.
- CLI handles current AgentBus files without errors.
- CLI does not require GitHub or remote access to run.
- Follow-up issues are recorded as tasks or review notes.

### Work Notes

### Blockers

### Review Notes

### Completion Summary

## TASK-008: Set Up Codex CLI TTS with Lori Voice

Status: Blocked
Owner: Codex CLI
Priority: Medium
Created: 2026-05-31
Updated: 2026-05-31
Related Files: `D:\AI_Models\Voice\moss-tts\tts_server_win.py`, `D:\AI_Models\Voice\moss-tts\repo\configs\llama_cpp\`, `D:\AI_Models\Voice\moss-tts\voices\`, `C:\Users\thoma\.claude\tts-hook.ps1`, `C:\Users\thoma\.claude\settings.json`

### Goal

Configure Codex CLI with a TTS hook that speaks Codex responses aloud using the MOSS-TTS server and the Lori voice, mirroring the setup Claude CLI has with the Hannah voice.

### Context

Claude CLI currently has a Stop hook (`C:\Users\thoma\.claude\tts-hook.ps1`) that fires after each response, strips markdown, and POSTs the text to the MOSS-TTS server at `http://127.0.0.1:8765/synthesize`. That server loads `hannah.yaml` and uses `Hannah_ref.wav` as the zero-shot reference.

Lori uses the base MOSS-TTS-GGUF model (zero-shot — no fine-tuned GGUF exists for Lori). The reference audio and a suitable config already exist. Because the server's CONFIG_PATH and PORT are currently hardcoded, a second instance for Lori requires CLI argument support in the server script. Claude CLI's Hannah server must remain on port **8765** and must not be disrupted.

### Reference Information

**Lori reference audio**
`D:\AI_Models\Voice\moss-tts\voices\Lori_ref.wav`

**Base MOSS-TTS GGUF weights (used for Lori zero-shot)**
`D:\AI_Models\Voice\moss-tts\weights\MOSS-TTS-GGUF\MOSS_TTS_Q4_K_M.gguf`
Embeddings: `D:\AI_Models\Voice\moss-tts\weights\MOSS-TTS-GGUF\embeddings\`
LM heads: `D:\AI_Models\Voice\moss-tts\weights\MOSS-TTS-GGUF\lm_heads\`
Tokenizer: `D:\AI_Models\Voice\moss-tts\weights\MOSS-TTS-GGUF\tokenizer\`

**Base config to use as Lori template (magnus.yaml)**
`D:\AI_Models\Voice\moss-tts\repo\configs\llama_cpp\magnus.yaml`
Points to the MOSS-TTS-GGUF weights above. Suitable for Lori zero-shot as-is.

**Hannah config (reference for yaml structure)**
`D:\AI_Models\Voice\moss-tts\repo\configs\llama_cpp\hannah.yaml`

**Server script**
`D:\AI_Models\Voice\moss-tts\tts_server_win.py`
CONFIG_PATH, REFERENCE_AUDIO, and PORT are currently hardcoded constants (lines 43–47).
Hannah server: port **8765**.
Lori server should run on port **8766**.

**Server launcher bat (reference)**
`D:\AI_Models\Voice\moss-tts\start_server_win.bat`
Activates the `moss-tts` conda env, sets CUDA 12 DLL paths, and launches the server.

**Claude CLI hook (reference implementation)**
`C:\Users\thoma\.claude\tts-hook.ps1`
Reads the last assistant message from the Claude transcript, strips markdown, splits into 400-char sentence chunks, and POSTs each chunk to `http://127.0.0.1:8765/synthesize`. Falls back to SAPI George voice if the server is unavailable.

**Claude CLI hook registration (reference)**
`C:\Users\thoma\.claude\settings.json`
Registers the hook under the `hooks` key as a `Stop` event with `"async": true`. The Codex CLI equivalent hook registration path and format should mirror this pattern for Codex CLI's own config directory.

**Audio tokenizer (shared by both server instances)**
`D:\AI_Models\Voice\moss-tts\weights\MOSS-Audio-Tokenizer-ONNX\encoder.onnx`
`D:\AI_Models\Voice\moss-tts\weights\MOSS-Audio-Tokenizer-ONNX\decoder.onnx`

### Acceptance Criteria

- `tts_server_win.py` accepts `--config`, `--reference`, and `--port` CLI args; existing defaults (Hannah config, Hannah_ref.wav, port 8765) are preserved so Claude CLI's setup requires no changes.
- `lori.yaml` exists at `D:\AI_Models\Voice\moss-tts\repo\configs\llama_cpp\lori.yaml`, pointing to MOSS-TTS-GGUF weights and `Lori_ref.wav`.
- A Lori server launcher exists (e.g., `start_server_lori.bat`) that starts the server on port 8766 with `lori.yaml` and `Lori_ref.wav`.
- A Codex CLI TTS hook script exists, adapted from `C:\Users\thoma\.claude\tts-hook.ps1`, targeting port 8766.
- The hook is registered in Codex CLI's settings using the same event pattern as Claude CLI's `Stop` hook.
- Claude CLI's Hannah server on port 8765 is unaffected.
- Thomas confirms Lori audio is audible when Codex CLI responds.

### Work Notes

- 2026-06-01: Codex CLI claimed TASK-008 and began Lori TTS setup.
- 2026-06-01: Implemented server args, Lori config/launcher, Codex hook script, and Codex hook registration.

### Blockers

- Thomas must confirm Lori audio is audible from a real Codex response after hook trust/reload and Lori server startup.
- Hannah server is currently healthy on port 8765, but GPU memory is nearly full with only ~261 MB free. Lori server was not started to avoid disrupting Hannah.

### Review Notes

### Completion Summary

- Accepted as setup-complete per DECISION-20260531-003. Runtime validation deferred to TASK-009.

## TASK-009: Perform Lori Runtime Audio Validation

Status: Blocked
Owner: Thomas / Codex CLI
Priority: Medium
Created: 2026-05-31
Updated: 2026-05-31
Related Files: `D:\AI_Models\Voice\moss-tts\start_server_lori.bat`, `D:\AI_Models\Voice\moss-tts\repo\configs\llama_cpp\lori.yaml`, `D:\AI_Models\Voice\moss-tts\voices\Lori_ref.wav`

### Goal

Confirm Lori TTS audio is audible when Codex CLI generates a response, completing the final acceptance criterion of TASK-008.

### Context

TASK-008 implementation is complete. Runtime validation was deferred because Hannah is active on port 8765 and GPU memory is constrained (~261 MB free). Starting a second server risks disrupting Hannah. DECISION-20260531-003 directs that validation happen during a planned test window.

### Acceptance Criteria

- Lori MOSS-TTS server starts successfully on port 8766 using `start_server_lori.bat`.
- A Codex CLI response triggers the TTS hook and Lori audio plays correctly.
- Hannah server on port 8765 is unaffected.

### Work Notes

### Blockers

- GPU memory must be available, or Hannah must be intentionally stopped for the test window.

### Review Notes

### Completion Summary

## TASK-015: Implement Watcher Governance Model v1

Status: Review — submitted by Codex CLI 2026-06-13
Owner: Codex CLI
Reviewer: Claude CLI
Priority: High
Created: 2026-06-13
Updated: 2026-06-13
Related Files: `watcher/`, `comms/inbox_watcher.md`, `state/sprint_board.md`, `README.md`, `Watcher_Agent_feature.md`
Related Decisions: DECISION-20260613-001, DECISION-20260613-002, DECISION-20260613-003
Related Reviews: REVIEW-008, REVIEW-009

### Goal

Implement the additive, role-based AgentBus Watcher Governance Model v1 as approved in DECISION-20260613-001/002/003, resolving the REVIEW-008 blocking findings and the REVIEW-009 conditions.

### Context

The Watcher is a coordination role (not a software service) activated on request (DECISION-001). It owns operational state surfaces while agents continue managing `tasks/*`, `reviews/*`, and `logs/*` (DECISION-003). Existing procedures remain valid and Watcher procedures are introduced in parallel. Per the established split, Codex CLI implements and Claude CLI reviews.

### Acceptance Criteria

**Files created (use explicit paths):**
- `watcher/watcher_rules.md` — responsibilities, authority, allowed/forbidden actions, state ownership, and worked examples for Accepted review, Blocked task, New task activation, Broadcast creation.
- `watcher/routing_table.md` — message routing (review outcome / task completion / blocker → Watcher inbox; question for Codex → `inbox_codex.md`; question for Claude → `inbox_claude.md`; team announcement → `broadcast.md`).
- `watcher/dispatch_queue.md` — template with Dispatch ID, Trigger, Assigned Agent, Action, Status.
- `watcher/event_log.md` — state-transition ledger (task accepted/completed/blocked, epic activated, dispatch generated).
- `comms/inbox_watcher.md` — Watcher inbox.
- `state/sprint_board.md` — board with Backlog / Ready / In Progress / Review / Blocked / Done, including ownership and status columns.

**Documentation:**
- `README.md` updated to describe the Watcher role, routing model, state ownership, and dispatch workflow.
- Watcher operating procedures documented for Review Accepted, Blocked Task, and EPIC Completion triggers.

**REVIEW-009 conditions (must be satisfied):**
- C1 — `state/sprint_board.md` is defined as a derived/reflective aggregate of `tasks/*`: the Watcher mirrors task state into the board; `tasks/*` remains authoritative for individual task state, `sprint_board.md` for the aggregate board view.
- C2 — Broadcast ownership is documented: agents retain `broadcast.md` for announcements and review notices; the Watcher owns status-change broadcasts only.
- C3 — AgentBus infrastructure does **not** use the Voice_Gen `[v0.3.0]` release tag; TASK-015 commits use an AgentBus track or are untagged.
- C4 — `watcher/watcher_rules.md` documents a correction procedure (how to undo a bad dispatch or revert an event-log entry) in addition to the "Override Watcher action → Thomas/Quill" authority.
- C5 — `watcher/dispatch_queue.md` is reflected in the state-ownership documentation (it was absent from the DECISION-002 File Authority Matrix).

**Compatibility & validation:**
- Existing procedures (`task_claiming.md`, `review_response.md`, `check_for_updates.md`) remain valid and unretired (additive model).
- Documentation is internally consistent; roles, routing, and sprint ownership are unambiguous.
- The Watcher can be performed by Claude, Codex, or a future local Director agent.
- End-to-end validation: demonstrate one complete cycle — Review Accepted → Watcher receives update → sprint board updated → event logged → dispatch generated → broadcast generated. The run is recorded and submitted for review.

### Work Notes

- 2026-06-13: Created from the approved Watcher Governance Proposal v1 (Quill) and REVIEW-009. Codex assigned implementation; Claude assigned review.
- 2026-06-13: Codex CLI claimed TASK-015 and began implementing Watcher governance files and validation records.
- 2026-06-13: Codex CLI completed Watcher governance implementation and submitted TASK-015 for Claude CLI review.

### Blockers

- None.

### Review Notes

- Submitted for Claude CLI review in `tasks/review.md`.

### Completion Summary
