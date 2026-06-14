# REVIEW-018

Reviewer: Claude CLI
Date: 2026-06-14
Related Task: TASK-020 (EPIC-002 — `--log-file` override, F1 resubmission)
Artifact: Voice_Gen commit `19372bb [v0.3.0][vg_e002][TASK-020] Create custom log parent directory`, branch `vg_e002_voice_gen_hardening__codex__TASK-020`
Status: Accepted

## Summary

The TASK-020 resubmission resolves REVIEW-016 finding F1 exactly as requested. A custom `--log-file` whose parent directory does not exist no longer raises an unhandled `FileNotFoundError`; the parent is created before the file handler opens. Minimal (2 lines), correctly placed, default behavior unchanged. Accepted.

## The Fix

```python
# Logging must start before dependency checks so failures are written to the run log.
if args.log_file:
    Path(args.log_file).parent.mkdir(parents=True, exist_ok=True)
log_file = setup_logging(voice_name, Path(args.log_file) if args.log_file else None)
```

## Verification Against REVIEW-016 F1

- **Custom `--log-file` parent created** ✓ — `Path(args.log_file).parent.mkdir(parents=True, exist_ok=True)` runs immediately before `setup_logging()` opens the `FileHandler`, so `--log-file D:/Logs/run.log` into a non-existent `D:/Logs` now succeeds instead of raising `FileNotFoundError`.
- **Guarded to custom paths only** ✓ — wrapped in `if args.log_file:`; the default timestamped path (handled inside the shared helper, which already `mkdir`s `LOG_DIR`) is untouched.
- **Idempotent** ✓ — `exist_ok=True`, so an existing parent does not error.
- **Default behavior unchanged** ✓ — when the flag is absent the new block is skipped; `setup_logging(voice_name, None)` falls back to the timestamped log exactly as before.
- **Scope** ✓ — change confined to `voice_gen.py` (2 insertions), no new logging machinery.
- **Commit tag** ✓ `[v0.3.0][vg_e002][TASK-020]`.

## Verification (reviewer)

- `python -m py_compile voice_gen.py voice_gen_utils.py` → COMPILE OK (run in reviewer worktree `Sandbox/Voice_Gen_claude` at `19372bb`).
- Diff is exactly the two F1 lines.

## Acceptance Recommendation

**Accepted.** REVIEW-016 F1 is resolved; the `--log-file` override now creates its parent directory before opening the log, with default behavior preserved and no regression. TASK-020 is complete. EPIC-002 (TASK-016/018/019/020) is now fully accepted; TASK-021 (`--dry-run`/scan-only) remains the last EPIC-002 item.
