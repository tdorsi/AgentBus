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

Status: Done — accepted by Claude CLI 2026-06-13
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
- 2026-06-13: Claude CLI accepted TASK-015 in REVIEW-010. Watcher pass moved task to done.

### Blockers

- None.

### Review Notes

- Submitted for Claude CLI review in `tasks/review.md`.
- Accepted by Claude CLI in `reviews/REVIEW-010.md`.

### Completion Summary

Watcher Governance Model v1 implemented and accepted. Required Watcher files, Watcher inbox, sprint board, README updates, routing model, correction procedure, state ownership matrix, and end-to-end validation cycle are in place.

## TASK-016: Add Voice_Gen Overwrite Protection

Status: Review — submitted by Codex CLI 2026-06-13
Owner: Codex CLI
Reviewer: Claude CLI
Priority: Critical
Created: 2026-06-13
Updated: 2026-06-13
Related Epic: EPIC-002 Voice_Gen Hardening
Related Branch: `vg_e002_voice_gen_hardening`
Related Reviews: REVIEW-011
Related Files: `D:\Development\Voice_Gen\voice_gen.py`

### Goal

Prevent reruns from silently overwriting existing voice training artifacts (feature item #3b).

### Acceptance Criteria

- `voice_gen.py` detects an existing output directory or critical generated artifacts for the selected voice before writing.
- Default behavior is non-destructive: stop with a clear message when collision risk exists (fail-by-default).
- **Resuming with `--from-stage` into an existing output directory is permitted and is NOT treated as a collision** (REVIEW-011 F3 carve-out).
- Ship an explicit, **logged** `--force` override (approved per **DECISION-20260613-004**). `--force` must NOT interfere with `--from-stage` resume.
- Commit tag: `[v0.3.0][vg_e002][TASK-016]`.
- Verification: compile check plus a relevant dry-run/scan verification.

### Work Notes

- 2026-06-13: Created by Watcher (Stan) from Codex's EPIC-002 breakdown (inbox_claude MSG-20260613-008) as adjusted by Claude's REVIEW-011 (Accepted with Changes). `--force` approved by Thomas in DECISION-20260613-004 (W006).
- 2026-06-13: Codex CLI claimed TASK-016 and began implementation on `vg_e002_voice_gen_hardening`.
- 2026-06-13: Codex CLI implemented and pushed commit `9a52d61`: `[v0.3.0][vg_e002][TASK-016] Add overwrite protection`.

### Blockers

- None.

### Review Notes

- Submitted for Claude CLI review in `tasks/review.md`.

## TASK-017: Clear Duplicate Logging Handlers — DROPPED

Status: Dropped (already delivered by EPIC-001)
Owner: Codex CLI
Reviewer: Claude CLI
Priority: High (originally)
Created: 2026-06-13
Updated: 2026-06-13
Related Epic: EPIC-002 Voice_Gen Hardening
Related Reviews: REVIEW-011

### Disposition

Dropped per REVIEW-011 F1. Feature item #2a (handler-clear) is already satisfied: `voice_gen_utils.setup_logging()` calls `logger.handlers.clear()` and `voice_gen.py` routes through that shared helper (delivered in EPIC-001 / TASK-012). No implementation work remains. The verification that repeated setup does not duplicate output is folded into the per-task verification standard for the remaining EPIC-002 tasks. The TASK-017 ID is retired (not reused).

## TASK-018: Add Graceful KeyboardInterrupt Handling

Status: Review — submitted by Codex CLI 2026-06-13
Owner: Codex CLI
Reviewer: Claude CLI
Priority: High
Created: 2026-06-13
Updated: 2026-06-13
Related Epic: EPIC-002 Voice_Gen Hardening
Related Branch: `vg_e002_voice_gen_hardening`
Related Files: `D:\Development\Voice_Gen\voice_gen.py`

### Goal

Make Ctrl+C cancellation user-friendly and consistent with `text_to_audio.py` (feature item #2b).

### Acceptance Criteria

- `voice_gen.py` catches `KeyboardInterrupt` at the top level.
- Console output reports cancellation without a traceback.
- Process exits with code 130.
- Cancellation handling does not swallow other unexpected exceptions.
- Commit tag: `[v0.3.0][vg_e002][TASK-018]`. Verification: compile check plus a relevant dry-run/scan verification.

### Work Notes

- 2026-06-13: Created by Watcher (Stan) from Codex's EPIC-002 breakdown, accepted in REVIEW-011.
- 2026-06-13: Codex CLI implemented and pushed commit `c2d62e8`: `[v0.3.0][vg_e002][TASK-018] Add keyboard interrupt handling`.

### Blockers

- None.

## TASK-019: Log Dependency Checks Correctly

Status: Review — submitted by Codex CLI 2026-06-13
Owner: Codex CLI
Reviewer: Claude CLI
Priority: High
Created: 2026-06-13
Updated: 2026-06-13
Related Epic: EPIC-002 Voice_Gen Hardening
Related Branch: `vg_e002_voice_gen_hardening`
Related Files: `D:\Development\Voice_Gen\voice_gen.py`

### Goal

Ensure ffmpeg/ffprobe dependency failures are written to the run log (feature item #2c).

### Acceptance Criteria

- Logging is initialized before dependency checks can fail, or dependency failures are otherwise captured in a log artifact.
- Dependency success/failure paths remain clear on console.
- Failure exits remain explicit and do not proceed into pipeline stages.
- Kept separate from TASK-020 per REVIEW-011 Q3.
- Commit tag: `[v0.3.0][vg_e002][TASK-019]`. Verification: compile check plus a relevant dry-run/scan verification.

### Work Notes

- 2026-06-13: Created by Watcher (Stan) from Codex's EPIC-002 breakdown, accepted in REVIEW-011.
- 2026-06-13: Codex CLI implemented and pushed commit `8b993a5`: `[v0.3.0][vg_e002][TASK-019] Log dependency check failures`.

### Blockers

- None.

## TASK-020: Add `--log-file` Override (plumbing only)

Status: Review — submitted by Codex CLI 2026-06-13
Owner: Codex CLI
Reviewer: Claude CLI
Priority: Medium
Created: 2026-06-13
Updated: 2026-06-13
Related Epic: EPIC-002 Voice_Gen Hardening
Related Branch: `vg_e002_voice_gen_hardening`
Related Reviews: REVIEW-011
Related Files: `D:\Development\Voice_Gen\voice_gen.py`, `D:\Development\Voice_Gen\voice_gen_utils.py`

### Goal

Allow callers to redirect Voice_Gen logs to a chosen path (feature item #2d). **Scope reduced to plumbing** per REVIEW-011 F2: the shared `voice_gen_utils.setup_logging()` already accepts a `log_file` parameter — only the CLI argument and pass-through are missing.

### Acceptance Criteria

- `voice_gen.py` accepts `--log-file PATH` and threads it into the existing `setup_logging(log_file=...)` parameter.
- Default (flag absent) resolves to the configured `LOG_DIR` (EPIC-001 config) with the existing timestamped log behavior unchanged.
- The override path is parent-created or fails with a clear error, matching existing project style.
- README or inline usage text documents the flag.
- Commit tag: `[v0.3.0][vg_e002][TASK-020]`. Verification: compile check plus a relevant dry-run/scan verification.

### Work Notes

- 2026-06-13: Created by Watcher (Stan); scoped as CLI plumbing per REVIEW-011 F2 (not new logging machinery).
- 2026-06-13: Codex CLI implemented and pushed commit `bf31d45`: `[v0.3.0][vg_e002][TASK-020] Add log file override`.

### Blockers

- None.

## TASK-021: Add Voice_Gen Dry-Run / Scan-Only Mode

Status: Ready
Owner: Codex CLI
Reviewer: Claude CLI
Priority: High
Created: 2026-06-13
Updated: 2026-06-13
Related Epic: EPIC-002 Voice_Gen Hardening
Related Branch: `vg_e002_voice_gen_hardening`
Related Reviews: REVIEW-011
Related Files: `D:\Development\Voice_Gen\voice_gen.py`

### Goal

Let users validate input audio planning before transcription or training (feature item #3a).

### Acceptance Criteria

- `voice_gen.py` exposes a **`--dry-run`** flag (name decided in REVIEW-011 Q2 for consistency with `text_to_audio.py`).
- The mode runs planning through the pre-training stages needed to report usable files, split plan, cleaned/scored candidates, and the selected reference candidate — without launching transcription, downloads, token encoding, fine-tuning, or sample generation.
- Output is clear enough to decide whether a full run is worth starting.
- The mode does not write destructive training artifacts.
- Commit tag: `[v0.3.0][vg_e002][TASK-021]`. Verification: compile check plus a `--dry-run` verification.

### Work Notes

- 2026-06-13: Created by Watcher (Stan) from Codex's EPIC-002 breakdown, accepted in REVIEW-011. Suggested implementation order places this last (builds on safer output/log behavior).

### Blockers

- None.

## TASK-022: Add `--keep-chunks` Per-Chunk WAV Preservation

Status: Ready
Owner: Gemini CLI
Reviewer: Claude CLI
Priority: Medium
Created: 2026-06-13
Updated: 2026-06-13
Related Epic: EPIC-003 Text_to_Audio Enhancements (combined)
Related Branch: `vg_e003_text_to_audio_enhancements`
Related Reviews: REVIEW-015
Related Files: `D:\Development\Voice_Gen\text_to_audio.py`

### Goal

Add an optional `--keep-chunks` flag that writes each generated audio chunk to a numbered file before concatenation (feature item #4b).

### Acceptance Criteria

- `--keep-chunks` defaults OFF.
- Chunk files are named `<stem>_chunk_001.wav` (zero-padded, ordered).
- The final concatenated WAV is byte-identical with or without the flag.
- The flag is a no-op under `--dry-run` (no chunk files written).
- Commit tag: `[v0.3.0][vg_e003][TASK-022]`. Verification: compile check plus a run/dry-run verification.

### Work Notes

- 2026-06-13: Created by Watcher (Stan) from Gemini's EPIC-003 breakdown as adjusted by Claude's REVIEW-015 (Accepted with Changes).

### Blockers

- None.

## TASK-023: Add Progress Reporting for Long Inference Runs

Status: Ready
Owner: Gemini CLI
Reviewer: Claude CLI
Priority: Medium
Created: 2026-06-13
Updated: 2026-06-13
Related Epic: EPIC-003 Text_to_Audio Enhancements (combined)
Related Branch: `vg_e003_text_to_audio_enhancements`
Related Reviews: REVIEW-015
Related Files: `D:\Development\Voice_Gen\text_to_audio.py`, `D:\Development\Voice_Gen\voice_gen_utils.py`

### Goal

Report progress during long inference runs (progress tracking + status), pulled forward from EPIC-004.

### Acceptance Criteria

- Progress output uses the shared `voice_gen_utils` console helpers (no divergent formatting).
- Progress reporting applies to real synthesis only (not `--dry-run`).
- Progress lines do not interleave with / corrupt log output.
- Commit tag: `[v0.3.0][vg_e003][TASK-023]`. Verification: compile check plus a real-run verification.

### Work Notes

- 2026-06-13: Created by Watcher (Stan) from Gemini's EPIC-003 breakdown, accepted with changes in REVIEW-015.

### Blockers

- None.

## TASK-024: Add ETA Calculation for Long Inference Runs

Status: Ready
Owner: Gemini CLI
Reviewer: Claude CLI
Priority: Medium
Created: 2026-06-13
Updated: 2026-06-13
Related Epic: EPIC-003 Text_to_Audio Enhancements (combined)
Related Branch: `vg_e003_text_to_audio_enhancements`
Related Reviews: REVIEW-015
Related Files: `D:\Development\Voice_Gen\text_to_audio.py`

### Goal

Estimate time remaining for long inference runs (ETA), pulled forward from EPIC-004.

### Acceptance Criteria

- ETA is computed from completed-chunk throughput (chars or chunks per second of finished work).
- For `--voice all`, ETA accounts for remaining voices, not just the current one.
- The pre-first-chunk state (no throughput data yet) is defined and displayed sensibly (e.g. "estimating…").
- Commit tag: `[v0.3.0][vg_e003][TASK-024]`. Verification: compile check plus a real-run verification.

### Work Notes

- 2026-06-13: Created by Watcher (Stan) from Gemini's EPIC-003 breakdown, accepted with changes in REVIEW-015. Builds on TASK-023.

### Blockers

- None.

## TASK-025: EPIC-003 Documentation and End-to-End Validation

Status: Ready
Owner: Gemini CLI
Reviewer: Claude CLI
Priority: Medium
Created: 2026-06-13
Updated: 2026-06-13
Related Epic: EPIC-003 Text_to_Audio Enhancements (combined)
Related Branch: `vg_e003_text_to_audio_enhancements`
Related Reviews: REVIEW-015
Related Files: `D:\Development\Voice_Gen\text_to_audio.py`, `D:\Development\Voice_Gen\README.md`

### Goal

Document the new EPIC-003 features and record an end-to-end validation run.

### Acceptance Criteria

- README documents `--keep-chunks`, progress reporting, and ETA behavior.
- A real multi-chunk run exercising `--keep-chunks` together with progress/ETA is performed and the result recorded.
- Commit tag: `[v0.3.0][vg_e003][TASK-025]`. Verification: the recorded end-to-end run is the verification.

### Work Notes

- 2026-06-13: Created by Watcher (Stan) from Gemini's EPIC-003 breakdown, accepted with changes in REVIEW-015. Final task in the suggested order.

### Blockers

- None.

## TASK-026: Implement AgentBus Communication Isolation (residual code + infra)

Status: Dispatched to Codex CLI 2026-06-14 (DISPATCH-20260614-001) — begins on restart under the new rules
Owner: Codex CLI
Reviewer: Claude CLI
Priority: High
Created: 2026-06-14
Updated: 2026-06-14
Related: `RCA.md` (RCA-20260613-001), `reviews/Agent_Bus_Action_Plan_draft.md`

> ID note: the action-plan draft labeled this "TASK-016", but that ID is taken (Voice_Gen overwrite protection, accepted via REVIEW-012). Renumbered to TASK-026.

### Goal

Complete the communication-isolation plan. The governance/doc portions were authored by the Watcher (per-agent inboxes, `watcher_rules.md`, `routing_table.md`, `procedures/review_response.md`, README). This task covers the remaining code + infrastructure + cutover.

### Acceptance Criteria

- `agentbus_health.py` detects duplicate message IDs across `comms/*` and `comms/watcher_inbox/*` (where practical) and flags `state/sprint_board.md` rows that disagree with `tasks/*`.
- Per-agent project working trees / clones established for Voice_Gen (e.g., `Voice_Gen_codex`, `Voice_Gen_claude_review`, `Voice_Gen_gemini`); no two agents share one project checkout for git writes.
- Cutover confirmed: all agents post to `comms/watcher_inbox/<agent>.md`; no agent is instructed to append to the retired shared `comms/inbox_watcher.md`.
- Watcher confirmed reading per-agent inboxes during a pass.
- README and `watcher_rules.md` isolation rules verified consistent with implementation.
- **AGENTS.md startup-file cutover:** all platform startup files reference the shared CLI-agnostic grounding `D:\Development\AGENTS.md`. `GEMINI.md` already repointed (Watcher, 2026-06-14); update Codex's startup config/instructions and any remaining `CLAUDE.md` cross-references to use `AGENTS.md` as the cross-agent anchor (`CLAUDE.md` stays as Claude Code's own platform file). Confirm per-platform memory dirs `D:\Memory\<Platform>\`.

### Work Notes

- 2026-06-14: Created by Watcher (Stan) from Thomas's action plan. Governance/doc updates already landed by the Watcher; this task is the residual code/infra/cutover. Not yet dispatched — awaiting Thomas's go to assign Codex.

### Blockers

- None.

## TASK-027: AgentBus Working-Tree Isolation (close the residual shared-checkout race)

Status: Active — claimed by Codex CLI 2026-06-14 (DISPATCH-20260614-002)
Owner: Codex CLI
Reviewer: Claude CLI
Priority: High
Created: 2026-06-14
Related: `RCA.md` (RCA-20260613-001), DECISION-20260614-001, **DECISION-20260614-002** (Approach A chosen), REVIEW-017 (Claude's root-cause note), TASK-026

### Goal

Close the residual concurrent-write race on the **AgentBus coordination repo itself**. TASK-026 isolated the *Voice_Gen* checkouts, but all agents still share a **single AgentBus working tree/index**. That is how, on 2026-06-14, a reviewer commit ended up stacked on Codex's feature branch alongside a concurrent TASK-022 commit and fast-forwarded onto `main` unintentionally (benign that time — see REVIEW-017 / Claude's transparency note). The single-writer *file-ownership* model is in place; the gap is the shared *checkout/index*.

### Context / candidate approaches

The AgentBus repo's coordination updates commit directly to `main` (not per-task feature branches), so the Voice_Gen worktree-per-task pattern doesn't map directly. Candidate approaches to evaluate:

- **(A, recommended) Per-agent AgentBus clones** — each agent (and the Watcher) operates in its own clone of AgentBus, commits its own files, and runs `git pull --rebase` immediately before `git push origin main`. Concurrent pushes serialize naturally via git (non-fast-forward → rebase → push); the shared-index contamination disappears. Pairs with the existing per-file single-writer ownership.
- **(B, fallback) Strict single-writer discipline** on one shared AgentBus checkout — commit-and-push atomically, one writer at a time, pull --rebase before each push. Lighter setup, but reintroduces serialization and relies on discipline.

**Approach A selected** per DECISION-20260614-002: per-agent AgentBus clones under `D:\Development\Sandbox\AgentBus_<agent>` (`AgentBus_stan`, `AgentBus_codex`, `AgentBus_claude`, `AgentBus_gemini`, `AgentBus_quill`); each agent works only in its own clone with `git pull --rebase` before push. The canonical `D:\Development\AgentBus` becomes the **human-operated reference checkout** (manual review / admin / PO / PM / inspection — no routine autonomous work). Approach B (single-writer discipline on one shared checkout) is the rejected fallback.

### Acceptance Criteria

- Per-agent AgentBus clones exist under `D:\Development\Sandbox\AgentBus_<agent>` (`stan`, `codex`, `claude`, `gemini`, `quill`), each with `origin` configured; canonical `D:\Development\AgentBus` is the human-operated reference checkout after cutover.
- No two agents share one AgentBus working tree/index; pushes to `origin/main` serialize via `git pull --rebase` before push.
- Validation is structural by Codex, with no impersonation: Codex verifies and documents all five clones have the correct `origin` remote, successful `git fetch`, clean `git pull --rebase`, and expected clean branch state. Codex does not commit, push, or post messages as another agent.
- Per-agent self-validation on first startup is documented: each agent validates its own pull -> trivial change -> commit -> push -> inbox/dispatch read path from its own clone.
- Docs updated: `procedures/agent_startup.md` (AgentBus clone step + first-startup self-validation), `procedures/branching_strategy.md`, and `D:\Development\AGENTS.md` (clone locations, `pull --rebase` before push, canonical reference checkout).
- (Optional, from REVIEW-017 FU note) `agentbus_health.py` flags active, non-history references to retired/foreign inboxes.
- Existing single-writer file-ownership rules (DECISION-20260614-001) remain in force and consistent.

### Work Notes

- 2026-06-14: Drafted by Watcher (Stan) at Thomas's direction, from Claude's REVIEW-017 root-cause note. Not dispatched; a durable `DECISION` extension may accompany the approach choice (Thomas / Quill).
- 2026-06-14: Thomas approved DECISION-20260614-002 and DISPATCH-20260614-002. Codex CLI claimed TASK-027 from its isolated AgentBus clone.

### Blockers

- None (design choice A vs B pending).

## TASK-028: EPIC-003 Runtime End-to-End Validation (TASK-025 FU1)

Status: Dispatched 2026-06-14 (DISPATCH-20260614-003)
Owner: Gemini CLI
Reviewer: Claude CLI
Priority: Medium
Created: 2026-06-14
Related: TASK-025 / REVIEW-023 FU1, EPIC-003; precedent TASK-009 (deferred runtime validation)
Related Files: `D:\Development\Voice_Gen\text_to_audio.py`, `D:\Development\Voice_Gen\README.md`

### Goal

Perform the **real** (not simulated) end-to-end MOSS-TTS run that TASK-025's C4 deferred — exercising `--keep-chunks` together with progress + ETA, and `--voice all`, and record the result. Thomas confirmed the TTS server is open and not in use (2026-06-14), so the window is available now.

### Acceptance Criteria

- A real MOSS-TTS synthesis run completes via `text_to_audio.py` against the live server (no simulation).
- `--keep-chunks` writes numbered chunk WAVs (`<stem>_chunk_001.wav` …); the final concatenated WAV is correct/consistent with/without the flag.
- `--voice all` is exercised across the configured voices.
- Real progress + ETA output is observed (the actual `Processing chunk X of Y … | ETA: …` line; "estimating…" at start).
- The run is **recorded** (console/log output and/or produced artifacts) and referenced in the submission, so acceptance rests on a real run rather than inspection.
- Coordinate to avoid disrupting other TTS usage; do not stop a server another agent/Thomas is using.

### Work Notes

- 2026-06-14: Created by Watcher (Stan) at Thomas's direction to discharge TASK-025 FU1 now that a test window is open. Owner Gemini (EPIC-003 feature owner); reviewer Claude.

### Blockers

- None (test window open).
