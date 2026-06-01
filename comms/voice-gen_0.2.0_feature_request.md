# Feature Enhancement Log — Voice_Gen v0.2.0

Author: Claude CLI
Date: 2026-06-01
Branch reviewed: `voice-gen_0.2.0`
Source: Code comparison of `voice_gen.py` (v0.1.0 pipeline) and `text_to_audio.py` (v0.2.0 inference utility)

---

## Background

During a cross-program review of `voice_gen.py` and `text_to_audio.py`, several divergences
were identified where one program had stronger safeguards or features than the other.
The review also surfaced known follow-ups logged by Codex CLI in the v0.2.0 session snapshot.
These are collected here as candidate features for a future release.

Items are grouped by theme and ordered within each group by estimated impact.

---

## 1. Shared Utility Module

**Both scripts duplicate:** banner, color constants (`BOLD`, `CYAN`, `GREEN`, `YELLOW`, `RED`,
`RESET`), console helpers (`ok`, `warn`, `err`, `info`, `header`), `setup_logging()`, and
`ask()` for interactive input.

**Proposed:** Extract these into `voice_gen_utils.py` (or `vg_common.py`) and import from both
scripts. This eliminates drift — any improvement to logging or terminal output only needs to
land in one place.

**Why it matters:** The v0.2.0 review required manually aligning Unicode symbols, handler
clearing, and separator characters across two files. A shared module makes that maintenance
free going forward.

---

## 2. Defensive Coding Gaps in voice_gen.py

These features exist in `text_to_audio.py` and should be back-ported to `voice_gen.py`:

### 2a. Duplicate handler guard in setup_logging()

`voice_gen.py` does not call `log.handlers.clear()` before adding handlers. If the function
is called more than once (reimport, test harness), every log line doubles. `text_to_audio.py`
already has this fix.

**Fix:** Add `log.handlers.clear()` as the first line of `voice_gen.py`'s `setup_logging()`.

### 2b. KeyboardInterrupt handling

Pressing Ctrl+C during a long stage (fine-tuning, transcription, HF download) produces a
full Python traceback. `text_to_audio.py` handles `KeyboardInterrupt` at the `__main__` level:
prints `"Cancelled."` and exits with code 130 (Unix convention). `voice_gen.py` should match.

**Fix:** Wrap `main()` call in `if __name__ == "__main__":` with explicit `KeyboardInterrupt`
handler.

### 2c. check_dependencies() runs before setup_logging()

In `voice_gen.py`, `check_dependencies()` (which verifies ffmpeg/ffprobe) executes before
`setup_logging()`. Failures print to console but are never written to the log file. If a user
reports a dependency error, there is no log artifact to inspect.

**Fix:** Start logging before dependency checks, or at minimum write dependency failures to
the log file before exiting.

### 2d. No --log-file override

`text_to_audio.py` exposes `--log-file` so callers can redirect logs to a specific path.
`voice_gen.py` always writes to a timestamped file in `LOG_DIR` with no override option.

**Fix:** Add `--log-file` argument to `voice_gen.py` matching `text_to_audio.py`'s
implementation.

---

## 3. Feature Parity — voice_gen.py Missing Capabilities

### 3a. Dry-run / plan-only mode

`text_to_audio.py` has `--dry-run` (chunks the text and prints sizes without loading MOSS).
`voice_gen.py` has no equivalent. A `--plan` or `--scan-only` flag that runs stages 1–4
(scan, split, clean, score) without transcription or training would let users validate
input audio quality before committing to a full pipeline run.

### 3b. Overwrite protection

`text_to_audio.py` detects output file collision and generates a timestamped fallback name
rather than silently overwriting. `voice_gen.py` does not check for existing output
artifacts — re-running with the same voice name and output directory overwrites prior results.

---

## 4. Feature Enhancements — text_to_audio.py

### 4a. Voice presets configurable from disk

`VOICE_PRESETS` is a hardcoded dict in `text_to_audio.py`. Adding a new voice requires
editing source code. The presets should be discovered at startup by scanning `CONFIG_DIR`
for `*.yaml` files and pairing each with a matching reference WAV in `VOICES_DIR`. This
makes new voices from `voice_gen.py` immediately available to `text_to_audio.py` without
any code change.

### 4b. Per-chunk intermediate WAV preservation

An optional `--keep-chunks` flag that writes each generated audio chunk to a numbered
file (e.g., `output_chunk_001.wav`) before concatenation. Useful for:
- QA listening to identify which chunk degraded
- Recovery when concatenation fails after a long run
- Side-by-side voice comparison at the chunk level

### 4c. Normalize default output directory

The interactive default output path is not set (user must type or accept blank). The
preferred test output folder `D:\Training_Data\Audio\TestOut` should be the default,
matching how Thomas runs the tool in practice.

### 4d. Default input path is hardcoded in source

The interactive fallback sets `default_input = r"D:\Training_Data\Audio\Test_Script\TTS_Script_01.txt"`.
This works for the current dev environment but is fragile. Recommend making this
discoverable (last-used path from a small state file, or a config env var) rather than
a hardcoded constant in source.

---

## 5. Longer-Term Architecture

These are lower priority and may warrant their own planning task:

- **Shared config file** — a `voice_gen.ini` or `voice_gen.toml` at the repo root for
  MOSS_ROOT, LOG_DIR, VOICES_DIR, and default output path. Both scripts read from it.
  Eliminates the hardcoded Windows paths scattered across both files.

- **Progress reporting** — for long inference runs (`--voice all` over a large text file),
  an estimated time remaining based on chars-per-second of completed chunks would improve
  the interactive experience.

- **Batch input** — accept a directory of `.txt` files rather than a single file, writing
  one WAV per input file. Useful for generating audio from a set of scripts in one pass.

---

## Summary Table

| # | Item | Affects | Effort |
|---|------|---------|--------|
| 1 | Shared utility module | Both | Medium |
| 2a | Handler clear in setup_logging | voice_gen.py | Low |
| 2b | KeyboardInterrupt handling | voice_gen.py | Low |
| 2c | Dependency check logging order | voice_gen.py | Low |
| 2d | --log-file override | voice_gen.py | Low |
| 3a | Dry-run / scan-only mode | voice_gen.py | Medium |
| 3b | Overwrite protection | voice_gen.py | Low |
| 4a | Configurable voice presets | text_to_audio.py | Medium |
| 4b | Per-chunk WAV preservation | text_to_audio.py | Low |
| 4c | Default output directory | text_to_audio.py | Low |
| 4d | Default input path (configurable) | text_to_audio.py | Low |
| 5 | Shared config file | Both | Medium |
| 5 | Progress / ETA reporting | text_to_audio.py | Medium |
| 5 | Batch input mode | text_to_audio.py | Medium |
