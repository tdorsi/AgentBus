# REVIEW-022

Reviewer: Claude CLI
Date: 2026-06-14
Related Task: TASK-024 (EPIC-003 — ETA reporting)
Artifact: Voice_Gen commit `3530bd5 [v0.3.0][vg_e003][TASK-024] Implement ETA reporting`, branch `vg_e003_text_to_audio_enhancements__gemini__TASK-024`
Status: Accepted

## Summary

TASK-024 adds a characters-per-second ETA to the progress line, correct across single-voice and `--voice all` runs, with a clean "estimating…" start and safe arithmetic. Meets the C3 criteria. One minor, non-blocking efficiency nit. Accepted.

## Verification Against Criteria (REVIEW-015 C3)

**CPS-based estimate** ✓ — `cps = chars_finished / elapsed_total`; `seconds_remaining = (global_total_chars - chars_finished) / cps`, formatted `ETA: {m}m {s}s`. Throughput derived from completed work, exactly as specified.

**`--voice all` aware** ✓ — `main()` computes `total_chars_in_file` once and sets `global_total_chars = total_chars_in_file * len(voices)`; `global_chars_done` accumulates `+= total_chars_in_file` after each voice and is passed in, so `chars_finished = global_chars_done + sum(len(c) for c in chunks[:idx-1])` correctly spans completed voices plus completed chunks of the current voice. The estimate reflects all remaining work across the run.

**"estimating…" start** ✓ — the guard `if chars_finished > 0 and elapsed_total > 0:` falls to `eta_str = "ETA: estimating..."` on the very first chunk of the first voice (`chars_finished == 0`). From the first chunk of the second voice onward, `chars_finished > 0` yields a real ETA.

**Safety** ✓ — division guarded (`chars_finished > 0 and elapsed_total > 0` ⇒ `cps > 0`); `chars_remaining` stays positive (the count excludes the current chunk, so it is ≥ the current chunk's length on the last iteration). No divide-by-zero, no negative ETA.

**Dry-run unaffected** ✓ — the ETA block is inside the generation loop (after the `dry_run` early return). The extra `read_text`/`split_text` and `start_time_global` in `main()` run harmlessly in dry-run but produce no progress/ETA output.

**Consistency with TASK-023** ✓ — extends the same `info(...)` line: `Processing chunk X of Y (N chars) | {eta_str}`.

Commit tag ✓. Compile verified at the integrated tip (REVIEW-023).

## Observations (non-blocking)

- **Redundant read/split in `main()`:** to obtain `total_chars_in_file`, `main()` now calls `read_text(input_path)` + `split_text(...)`, and `synthesize_file()` reads and splits the same file again internally — so the input is parsed 1 + N times for an N-voice run. Functionally correct (same `chunk_chars`, so counts match) and negligible for CLI text input; a future tidy could compute the count once and pass chunks/total through. Not worth blocking.

## Acceptance Recommendation

**Accepted.** ETA reporting meets all C3 criteria with correct `--voice all` accounting and safe arithmetic. The redundant read is a minor, optional cleanup.
