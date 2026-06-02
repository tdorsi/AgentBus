# REVIEW-006

Reviewer: Claude CLI
Date: 2026-06-02
Related Task: TASK-013
Artifact: `voice_gen_config.py`, `voice_gen.toml`, `voice_gen.py`, `text_to_audio.py`, `README.md` — Voice_Gen commit `9564716`, branch `vg_e001_shared_config`
Status: Accepted

## Summary

TASK-013 shared configuration system is complete and correctly implemented. The critical anchor condition from REVIEW-004 is satisfied. The module delivers a clean, frozen-dataclass config model, a safe deep-merge of defaults + overrides, `expandvars` path expansion, clear error messages at every failure point, and pre-flight `validate_paths()` calls in both scripts. TASK-014 is cleared to begin.

## Findings

**`voice_gen_config.py` — new configuration module**

- `CONFIG_PATH = Path(__file__).parent / "voice_gen.toml"` — ✓ module-relative anchor confirmed. This was the single required condition from REVIEW-004 before TASK-013 could begin. Correctly placed so both scripts are invocable from any working directory (verified: dry-run from `D:\Development\AgentBus` passed in Codex's verification).
- `DEFAULTS` dict covers all five EPIC-001 required keys (`moss_root`, `log_dir`, `voices_dir`, `default_output_dir`, `default_input_file`) plus `moss_repo`, `weights_dir`, `ffmpeg_dir`, `config_dir`, `llama_cpp_dir`, `onnx_dir`. No required key is missing.
- `load_config()` deep-merges DEFAULTS with TOML contents — partial TOML overrides work correctly. A TOML that only changes one key leaves all others at their defaults. Correct approach.
- `_deep_merge` recursion handles dict values from defaults by passing `{}` as the second argument, ensuring dict entries are copied rather than shared. ✓
- `validate_paths()` accepts an explicit key list so each caller specifies only the paths it actually needs — not overzealous. `voice_gen.py` validates `["moss_repo", "weights_dir", "voices_dir", "onnx_dir"]`; `text_to_audio.py` validates `["moss_root", "moss_repo", "voices_dir", "config_dir", "llama_cpp_dir", "onnx_dir"]`. Both call this before heavy operations begin. ✓
- `_path()` applies `os.path.expandvars()` before `expanduser()` — Windows environment variables (`%USERPROFILE%`, `%APPDATA%`, etc.) work in TOML values. ✓
- `_voices()` lowercases all voice names on load — consistent lookup regardless of how names appear in the TOML. ✓
- `ConfigError(RuntimeError)` with explicit messages: names the file path on missing config file, names `[section] key` on invalid value, lists all missing paths on `validate_paths()` failure. Error messages are actionable.
- Frozen dataclasses (`VoiceGenConfig`, `PathConfig`, `MossConfig`, `VoiceConfig`) — immutable config object. Good design: no accidental mutation post-load.
- `tomllib` (Python 3.11 stdlib) — no new dependency introduced. ✓

**`voice_gen.toml`**

- All five EPIC-001 required keys present.
- All three voice presets (Lori, Lilybelle, Hannah) defined under `[voices.*]` sections — these are now in config, no longer in source code. TASK-014 can use `APP_CONFIG.voices` as the authoritative voice registry.
- `voice_gen.toml` is identical to the `DEFAULTS` dict in `voice_gen_config.py`, which is correct: the file documents the defaults explicitly for users who need to customise. No divergence between source defaults and TOML values.

**`voice_gen.py` and `text_to_audio.py` migration**

- Both scripts import `voice_gen_config`, call `load_config()` at module level, and exit cleanly with a `ConfigError` message if config is invalid — no traceback noise for user-facing config errors.
- All previously hardcoded path constants (`MOSS_REPO`, `WEIGHTS_DIR`, `VOICES_DIR`, `ONNX_ENC`, `ONNX_DEC`, `LOG_DIR`, `FFMPEG_DIR` in `voice_gen.py`; `MOSS_ROOT`, `MOSS_REPO`, `LLAMA_CPP_DIR`, `CONFIG_DIR`, `VOICES_DIR`, `LOG_DIR`, `ONNX_DIR` in `text_to_audio.py`) are now derived from `APP_CONFIG`. ✓
- Interactive prompts updated: `default_input_file` and `default_output_dir` now come from config. ✓
- Config path logged at run start (`log.info("Config: %s", APP_CONFIG.path)` / `log.info("  Config     : %s", APP_CONFIG.path)`) — useful for debugging misconfigured paths. ✓
- Pipeline logic, stage execution, ffmpeg calls, inference, DLL loading — all untouched. ✓

**`README.md`**

- Configuration section added explaining `voice_gen.toml` sections, module-relative resolution behaviour, and fast-fail semantics. ✓

**Compile and import verification (Claude CLI)**

```
python -m py_compile voice_gen_config.py voice_gen_utils.py text_to_audio.py voice_gen.py  →  OK (no output)
```

## Risks

None blocking. The config load happens at module import time — a missing or invalid `voice_gen.toml` will cause a clean `SystemExit(1)` with a message, not a raw exception. The deep-merge and frozen-dataclass design means misconfiguration fails fast and loudly rather than silently.

## Observations

**Non-blocking — `log_dir` in `validate_paths()` lookup but not validated by either caller:**
`validate_paths()` exposes `"log_dir"` as a valid key, but neither `voice_gen.py` nor `text_to_audio.py` includes it in their validation lists. This is correct behaviour: `log_dir` doesn't need to pre-exist since logging setup typically creates it. No action needed.

**TASK-014 readiness confirmed:**
`APP_CONFIG.voices` is a `dict[str, VoiceConfig]` fully populated from `[voices.*]` TOML sections. `text_to_audio.py` can replace any hardcoded `PRESETS` dict with a lookup against `APP_CONFIG.voices` in TASK-014 with no changes to `voice_gen_config.py`. The data path is ready.

## Acceptance Recommendation

**Accepted.** TASK-013 acceptance criteria are fully met:

- `voice_gen.toml` exists at the Voice_Gen repository root. ✓
- Both applications load shared configuration successfully. ✓
- Configuration includes `MOSS_ROOT`, `LOG_DIR`, `VOICES_DIR`, `DEFAULT_OUTPUT_DIR`, and `DEFAULT_INPUT_FILE`. ✓
- Reasonable defaults preserve the current local workflow. ✓
- Missing or invalid config values produce clear logged errors. ✓
- README documents the configuration file. ✓

TASK-014 cleared to begin.
