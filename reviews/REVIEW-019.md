# REVIEW-019

Reviewer: Claude CLI
Date: 2026-06-14
Related Task: TASK-022 (EPIC-003 — per-chunk WAV preservation, `--keep-chunks`)
Artifact: Voice_Gen commit `6ba3b98 [v0.3.0][vg_e003][TASK-022] Implement per-chunk WAV preservation`, branch `vg_e003_text_to_audio_enhancements__gemini__TASK-022_v2`
Status: Accepted

## Summary

TASK-022 adds an opt-in `--keep-chunks` flag to `text_to_audio.py` that writes each generated chunk to a numbered WAV beside the final output. The implementation meets all four REVIEW-015 C1 criteria — default off, `<stem>_chunk_001.wav` naming, final WAV byte-identical with/without the flag, and a no-op under `--dry-run` — verified by inspecting the surrounding control flow, not just the diff. Minimal and additive. Accepted.

## Verification Against REVIEW-015 C1

**Default OFF** ✓ — `--keep-chunks` is `action="store_true"` (default `False`); the `synthesize_file` parameter defaults to `keep_chunks: bool = False`; the write is guarded by `if keep_chunks:`. Absent the flag, behavior is unchanged.

**Naming `<stem>_chunk_001.wav`** ✓ — `output_path.with_name(f"{output_path.stem}_chunk_{idx:03d}.wav")`. The generation loop is `for idx, chunk in enumerate(chunks, start=1)`, so the first chunk is `_chunk_001.wav` (1-based, zero-padded to 3), written to the same directory as the final output.

**Final WAV byte-identical with/without the flag** ✓ — the chunk block is a pure side-write: `audio_parts.extend(generated_parts)` happens first and unconditionally; the `if keep_chunks:` block then writes a *separate* file via `sf.write(chunk_path, np.concatenate(generated_parts), SAMPLE_RATE)` and never mutates `audio_parts` or the inter-chunk silence handling. The concatenated final output is therefore independent of `keep_chunks`. (The per-chunk file is the chunk's own audio, without the inter-chunk silence — correct for QA/recovery use.)

**No-op under `--dry-run`** ✓ — `synthesize_file` handles `if dry_run:` with its own preview loop and `return "dry-run", output_path` *before* the real generation loop that contains the `keep_chunks` block. Under `--dry-run`, the chunk-write path is never reached, so no files are written.

**Empty-parts edge case** ✓ — `np.concatenate(generated_parts) if generated_parts else np.array([], dtype=np.float32)` avoids a concatenate error on an empty chunk.

**Commit tag** ✓ `[v0.3.0][vg_e003][TASK-022]`. **Scope** ✓ — one optional param, one guarded block, one arg, one pass-through; `sf`/`np`/`SAMPLE_RATE` already in use.

## Verification (reviewer)

- `python -m py_compile text_to_audio.py` → COMPILE OK (reviewer worktree `Sandbox/Voice_Gen_claude` at `6ba3b98`).
- Control-flow inspected to confirm the dry-run early return precedes the chunk loop and `idx` is 1-based.

## Observations (non-blocking)

- Branch name came through as `…__TASK-022_v2` rather than the convention `vg_e003_text_to_audio_enhancements__gemini__TASK-022` (already flagged by the Watcher) — harmless, just affects history tidiness.
- Process note: the TASK-022 submission was posted to `comms/watcher_inbox/gemini.md` (MSG-20260614-GEMINI-02) but no `## TASK-022` entry was added to the `tasks/review.md` queue. I've added a minimal entry there to record the outcome; future EPIC-003 submissions should include the `tasks/review.md` entry per `procedures/review_response.md`.

## Acceptance Recommendation

**Accepted.** TASK-022 satisfies all REVIEW-015 C1 criteria with a clean, additive implementation and verified dry-run/byte-identical behavior. TASK-023 (progress reporting) is next per the DISPATCH-20260613-005 ordering.
