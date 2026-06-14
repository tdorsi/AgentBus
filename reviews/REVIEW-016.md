# REVIEW-016

Reviewer: Claude CLI
Date: 2026-06-13
Related Task: TASK-020 (EPIC-002 Voice_Gen Hardening — `--log-file` override, plumbing only)
Artifact: Voice_Gen commit `bf31d45 [v0.3.0][vg_e002][TASK-020] Add log file override`, branch `vg_e002_voice_gen_hardening`
Status: Changes Requested

## Summary

TASK-020 adds a `--log-file PATH` argument and threads it into the existing shared `voice_gen_utils.setup_logging(..., log_file=...)` helper — correct, minimal plumbing as scoped in REVIEW-011. Default timestamped behavior is preserved, the flag is documented, and the active log path is logged. One acceptance criterion is not met: a custom `--log-file` whose parent directory does not exist fails with an unhandled traceback rather than creating the parent or failing cleanly. Returning as **Changes Requested** for that one fix.

## What's Correct

- `--log-file` argument added to `parse_args()`. ✓
- `setup_logging(voice_name, log_file=None)` gains an optional param and passes it through to `ui.setup_logging(log, LOG_DIR, voice_name, log_file=log_file)` — wires into the EPIC-001 shared helper's existing `log_file` parameter, no new logging machinery. ✓
- Default behavior preserved: when `--log-file` is absent, `None` is passed and the shared helper falls back to the timestamped `LOG_DIR/<stamp>_<voice>.log` path. ✓
- Usage header documents the flag; `main()` logs `"  Log file   : %s"`. ✓
- Commit tag `[v0.3.0][vg_e002][TASK-020]`. ✓
- Scope is plumbing-only, matching REVIEW-011. ✓

## Required Change

**F1 — Custom `--log-file` parent directory is not created (criterion miss).**

The TASK-020 acceptance criterion (from the breakdown / REVIEW-011) states: *"The override path is parent-created or fails with a clear error, matching existing project style."*

`voice_gen_utils.setup_logging()` calls `log_dir.mkdir(parents=True, exist_ok=True)` for the **default** `LOG_DIR`, but when a custom `log_file` is supplied it goes straight to `logging.FileHandler(log_file, ...)` without creating `log_file.parent`. `logging.FileHandler` does not create parent directories, so:

```
python voice_gen.py --log-file D:/Logs/run.log    # when D:/Logs does not exist
```

raises an unhandled `FileNotFoundError` traceback. That is neither "parent-created" nor a "clear error matching existing project style" (the project convention is `err(...)` + `sys.exit(1)`, as in `check_dependencies()` / `validate_paths()`).

The default path and a custom path into an existing directory both work — only a custom path into a missing directory is affected.

**Suggested fix (one line, smallest scope):** in `voice_gen.py`'s `setup_logging` wrapper (or `main()`), create the parent before delegating:

```python
if args.log_file:
    Path(args.log_file).parent.mkdir(parents=True, exist_ok=True)
```

Alternatively, add `log_file.parent.mkdir(parents=True, exist_ok=True)` inside the shared `voice_gen_utils.setup_logging()` (benefits `text_to_audio.py` too, but is a shared-helper change — note that EPIC-001 reviewers should be aware). Either is acceptable; the wrapper-level fix keeps the change inside TASK-020 scope. If you prefer "fail clean" over "auto-create," a guarded check that prints `err(...)` and `sys.exit(1)` when the parent is missing also satisfies the criterion.

## Verification (Codex, reviewed)

- `python -m py_compile voice_gen.py`; `python voice_gen.py --help`.
- Inline check: `parse_args()` accepts `--log-file`, `setup_logging()` returns the requested path, file created.
- Note: the recorded verification used a path whose parent already existed, so it did not exercise the F1 case.

## Acceptance Recommendation

**Changes Requested.** Plumbing is correct and in scope; resolve F1 (create the `--log-file` parent directory, or fail with a clear `err()`+exit) and resubmit. Everything else meets the criteria. Expected to be a one-line change and a quick re-review.
