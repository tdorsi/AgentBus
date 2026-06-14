# REVIEW-014

Reviewer: Claude CLI
Date: 2026-06-13
Related Task: TASK-019 (EPIC-002 Voice_Gen Hardening)
Artifact: Voice_Gen commit `8b993a5 [v0.3.0][vg_e002][TASK-019] Log dependency check failures`, branch `vg_e002_voice_gen_hardening`
Status: Accepted

## Summary

TASK-019 reorders `check_dependencies()` to run after `setup_logging()` (and after path validation) in `voice_gen.py`, so ffmpeg/ffprobe dependency failures are captured in the per-run log file rather than only stderr. The fix is correct and minimal, and console behavior and explicit failure exit are preserved. Accepted.

## The Fix

The diff only moves the `check_dependencies()` call site:
- Removed from immediately after `ui.banner(...)` (before logging existed).
- Re-added after `log_file = setup_logging(voice_name)` and the `validate_paths()` block, before the input-dir check and pipeline stages.

## Verification Against Criteria

**Dependency failures written to the run log** ✓
This is the crux, and it checks out. `check_dependencies()` already calls `log.error("Dependency check failed for %s at %s: %s", ...)` on failure, and its `err()` helper routes through the logger (`err()` → `ui.err(log, msg)`). Previously the call ran *before* `setup_logging()`, so the file handler did not exist and the failure reached only stderr (via logging's lastResort). After the move, the configured file handler is active, so the failure is written to the run-log artifact. The move is precisely what closes the gap.

**Logging initialized before dependency checks** ✓
`setup_logging(voice_name)` runs first; `check_dependencies()` follows.

**Console success/failure paths remain clear** ✓
`check_dependencies()` still calls `ok(...)` on success and `err(...)` + two `print(...)` install hints on failure — console output is unchanged.

**Explicit failure exit, no entry into stages** ✓
On failure it still `sys.exit(1)`. The call sits before the input-dir check, overwrite protection, and all stage execution.

**Commit tag** ✓ `[v0.3.0][vg_e002][TASK-019]`.

**No regression** ✓
Pure reordering; `check_dependencies()` body is unchanged. Normal startup proceeds exactly as before once dependencies pass.

## Verification (Codex, confirmed by inspection)

- `python -m py_compile voice_gen.py`.
- Simulated missing ffmpeg exits `1`, reports the generated log file, and confirms `LOG_HAS_FAILURE=True`.

## Observations (non-blocking)

- Because the per-run log file is named from `voice_name`, `check_dependencies()` now necessarily runs *after* the interactive `voice_name`/input/output prompts, so a user missing ffmpeg answers those prompts before seeing the dependency error (previously it failed before prompting). This is an inherent and acceptable trade-off of the "log the failure" requirement — capturing the failure in the run log requires logging, which requires the voice name. No change recommended.

## Acceptance Recommendation

**Accepted.** TASK-019 meets all criteria: dependency failures are now written to the run log, logging is initialized first, console behavior and explicit failure exit are preserved, and there is no regression. Recommend TASK-019 move to done; TASK-020 (`--log-file` plumbing) is next per DISPATCH-20260613-003 ordering.
