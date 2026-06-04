# REVIEW-007

Reviewer: Claude CLI
Date: 2026-06-04
Related Task: TASK-014
Artifact: `text_to_audio.py`, `voice_gen_config.py`, `voice_gen.toml`, `README.md` — Voice_Gen commit `a83550f`, branch `vg_e001_shared_config`
Status: Accepted

## Summary

TASK-014 voice preset migration is complete and correctly implemented. The hardcoded `VoicePreset` dataclass and Lori/Lilybelle/Hannah registry are fully removed from `text_to_audio.py`. Voice discovery, CLI choices, interactive prompts, default voice, and `--voice all` all now derive from `APP_CONFIG.voices`. The `[text_to_audio] default_voice` key is validated at config load with a clear error message. EPIC-001 is complete.

## Findings

**`text_to_audio.py` — preset removal**

- `VoicePreset` dataclass import (`from dataclasses import dataclass`) removed. ✓
- `VOICE_PRESETS` dict with hardcoded Lori/Lilybelle/Hannah `VoicePreset` entries fully removed. ✓ Replaced by the single line `CONFIGURED_VOICES = APP_CONFIG.voices`.
- `CONFIG_DIR` and `VOICES_DIR` module-level constants removed — correct, they were only used for `VOICE_PRESETS` construction. ✓
- Hardcode scan confirms no Lori/Lilybelle/Hannah names or training-data paths remain in source. ✓

**Voice discovery**

- `--voice` argument: `choices=[*CONFIGURED_VOICES.keys(), "all"]` — dynamically built from config. ✓ Adding a `[voices.custom]` section to `voice_gen.toml` immediately exposes it as a valid CLI choice without source code changes.
- Interactive prompt: `voice_choices = ", ".join([*CONFIGURED_VOICES.keys(), "all"])` — same dynamic source. ✓
- Interactive validation: `if voice not in CONFIGURED_VOICES and voice != "all"` — correct guard. ✓
- `--voice all` expansion: `voices = list(CONFIGURED_VOICES) if args.voice == "all"` — iterates all configured voices. ✓
- Preset lookup in run loop: `preset = CONFIGURED_VOICES[voice]` — clean single-line access. ✓

**Default voice**

- New `[text_to_audio] default_voice = "lori"` in `voice_gen.toml`. ✓
- Same key in `DEFAULTS["text_to_audio"]` preserves backward compatibility when field is absent from TOML. ✓
- Validated at config load time against the loaded `voices` dict before `VoiceGenConfig` is constructed — `ConfigError` with a clear actionable message if the default doesn't match any `[voices.*]` section. ✓ Correct design: invalid config fails fast at load, not at first synthesis attempt.

**`voice_gen_config.py` changes**

- New `TextToAudioConfig` frozen dataclass: `default_voice: str`. Consistent with existing frozen dataclass pattern. ✓
- `_string()` helper extracted from `_path()` — `_path()` now delegates to `_string()` for the string extraction and validation, then wraps in `Path(os.path.expandvars(...)).expanduser()`. Clean refactor, no behavior change to existing path loading. ✓
- `VoiceGenConfig.text_to_audio: TextToAudioConfig` — new field, consistent with existing frozen dataclass design. ✓
- `load_config()` calls `_voices()` first so validation of `default_voice` can reference the populated voices dict. Correct ordering. ✓

**Output collision preservation**

`resolve_output_path()` and the timestamped output logic are untouched in TASK-014. Collision behavior confirmed intact by inspection. ✓

**Compile verification (Claude CLI)**

```
python -m py_compile voice_gen_config.py voice_gen_utils.py text_to_audio.py voice_gen.py  →  COMPILE OK
```

## Risks

None blocking. The migration is conservative: all existing voice names (`lori`, `lilybelle`, `hannah`) remain in `voice_gen.toml` with identical paths, so no existing workflow breaks. The default voice is still `lori`.

## Observations

**Non-blocking — `default_voice` lowercased in `load_config()`:**
`_string(data, "text_to_audio", "default_voice").lower()` — the `.lower()` is applied, matching the convention in `_voices()` where voice names are lowercased on load. Consistent. ✓

**EPIC-001 completion confirmed:**
All four TASK-011 through TASK-014 acceptance criteria are now satisfied:
- Shared utility helpers: `voice_gen_utils.py` (TASK-012) ✓
- Shared config system: `voice_gen_config.py` + `voice_gen.toml` (TASK-013) ✓
- No hardcoded voice presets or default paths in `text_to_audio.py` (TASK-014) ✓
- Future voice additions require only a `[voices.name]` TOML entry (TASK-014) ✓

## Acceptance Recommendation

**Accepted.** TASK-014 acceptance criteria are fully met:

- Hardcoded `VoicePreset` dataclass and Lori/Lilybelle/Hannah registry removed from `text_to_audio.py`. ✓
- `APP_CONFIG.voices` is the authoritative voice registry for CLI choices, interactive prompts, preset lookup, and `--voice all`. ✓
- `[text_to_audio] default_voice` is configurable and validated at load time. ✓
- `--voice all` iterates all configured voices. ✓
- Output collision behavior is preserved. ✓
- Adding a new voice requires only a TOML entry — no source edits. ✓

EPIC-001 (Shared Configuration Framework) is complete.
