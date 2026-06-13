# REVIEW-013

Reviewer: Claude CLI
Date: 2026-06-13
Related Task: TASK-018 (EPIC-002 Voice_Gen Hardening)
Artifact: Voice_Gen commit `c2d62e8 [v0.3.0][vg_e002][TASK-018] Add keyboard interrupt handling`, branch `vg_e002_voice_gen_hardening`
Status: Accepted

## Summary

TASK-018 adds graceful top-level `KeyboardInterrupt` handling to `voice_gen.py` via a `run_cli()` wrapper around `main()`. Ctrl+C now prints a clean cancellation message and exits with code 130, with no traceback, and without swallowing any other exception. The change is minimal (8 lines) and matches `text_to_audio.py`'s behavior. Accepted.

## Implementation

```python
def run_cli():
    try:
        main()
    except KeyboardInterrupt:
        print("\nCancelled.")
        raise SystemExit(130)

if __name__ == "__main__":
    run_cli()
```

## Verification Against Criteria

**Top-level `KeyboardInterrupt` handling** ✓
`run_cli()` wraps `main()` and is the sole `__main__` entry point (line 1018). Any interrupt raised anywhere in `main()` or the stage flow propagates to this handler.

**No traceback on cancellation** ✓
The interrupt is caught and replaced with `print("\nCancelled.")` + `raise SystemExit(130)`. `SystemExit` with an integer code exits silently (no traceback), and the original `KeyboardInterrupt` is consumed.

**Exit code 130** ✓
`raise SystemExit(130)` — the Unix Ctrl+C convention, matching `text_to_audio.py`.

**Does not swallow other unexpected exceptions** ✓
Only `KeyboardInterrupt` is caught. Confirmed by inspection: the only `except KeyboardInterrupt` in the file is this one (line 1012), and there is no bare `except:` or `except BaseException` in `voice_gen.py` that could intercept Ctrl+C earlier. `main()`'s existing `except Exception` paths cannot catch `KeyboardInterrupt` (it derives from `BaseException`, not `Exception`), so non-interrupt errors continue down the existing pipeline error path unchanged.

**Commit tag** ✓ `[v0.3.0][vg_e002][TASK-018]` — correct Voice_Gen track.

**No regression / additive** ✓
Adds one wrapper function and redirects the `__main__` guard from `main()` to `run_cli()`. Normal completion path is unchanged.

## Verification (Codex, confirmed by inspection)

- `python -m py_compile voice_gen.py`.
- Subprocess test mocking `main` to raise `KeyboardInterrupt` → prints `Cancelled.`, no traceback, `RETURN_CODE=130`.

## Acceptance Recommendation

**Accepted.** TASK-018 meets all acceptance criteria: top-level `KeyboardInterrupt` handling, clean cancellation without traceback, exit code 130, and no swallowing of other exceptions. Recommend TASK-018 move to done; TASK-019 is next per DISPATCH-20260613-003 ordering.
