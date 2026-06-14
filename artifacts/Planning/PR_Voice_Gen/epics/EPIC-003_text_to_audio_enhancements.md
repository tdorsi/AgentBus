# EPIC-003: Text_to_Audio Enhancements

## Objective

Enhance `text_to_audio.py` with defensive features and improved user feedback. This epic combines the original EPIC-003 (Per-chunk preservation) and EPIC-004 (Progress reporting) into a single implementation phase.

## Scope

- **Per-chunk WAV preservation:** Add an optional `--keep-chunks` flag to preserve intermediate numbered WAV files before final concatenation.
- **Progress Reporting:** Implement real-time progress tracking (e.g., "Processing chunk X of Y").
- **ETA Calculation:** Calculate and report an Estimated Time of Arrival for long-running inference tasks.

## Acceptance Criteria

### TASK-022: Implement Per-Chunk WAV Preservation
- `text_to_audio.py` accepts `--keep-chunks` (default is OFF).
- Naming scheme: `{output_path.stem}_chunk_{idx:03d}.wav`.
- Chunks written to the same directory as the final output WAV.
- Final concatenated output is byte-for-byte identical with or without the flag.
- No-op behavior under `--dry-run`.
- Commit tag: `[v0.3.0][vg_e003][TASK-022]`.
- Verification: `py_compile`, synthesis run with/without flag, dry-run check.

### TASK-023: Implement Enhanced Progress Tracking
- Use `voice_gen_utils` encoding-safe helpers (`info`/`ok`).
- Display "Processing chunk X of Y" during real synthesis only.
- No progress tracking during `--dry-run`.
- Clean output; no log corruption or interleaving.
- Commit tag: `[v0.3.0][vg_e003][TASK-023]`.
- Verification: `py_compile`, observed console output during synthesis.

### TASK-024: Implement ETA Reporting
- Base estimate on characters-per-second (CPS) of finished chunks.
- For `--voice all`, account for total remaining chunks across all voices.
- Initial status (before first chunk): "estimating...".
- Commit tag: `[v0.3.0][vg_e003][TASK-024]`.
- Verification: `py_compile`, observed console output for single-voice and `--voice all` runs.

### TASK-025: EPIC-003 Documentation & Validation
- `Voice_Gen/README.md` updated with new flags and behavior.
- Recorded end-to-end run of `text_to_audio.py` with features active on a multi-chunk input.
- Verified in `D:\Development\Sandbox`.
- Commit tag: `[v0.3.0][vg_e003][TASK-025]`.

## Branch

`vg_e003_text_to_audio_enhancements` (Parent: `vg_e001_shared_config`)

## Dependencies

- Requires EPIC-001 (`vg_e001_shared_config`) for configuration and utility helpers.
