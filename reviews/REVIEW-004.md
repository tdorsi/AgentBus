# REVIEW-004

Reviewer: Claude CLI
Date: 2026-06-01
Related Task: TASK-011
Artifact: `docs/architecture/EPIC-001_shared_configuration_architecture.md` (Voice_Gen commit `3ca96ad`, branch `vg_e001_shared_config`)
Status: Accepted with observations

## Summary

The EPIC-001 shared configuration architecture is well-designed, clearly scoped, and safe to proceed with. The two-module split (`voice_gen_utils.py` for UI/logging, `voice_gen_config.py` for config loading), the TOML structure, and the sequential migration plan all reflect sound engineering judgment. No blocking issues found. Three non-blocking observations and one actionable suggestion are noted below.

## Findings

**Strengths:**

- Separation of concerns between `voice_gen_utils.py` and `voice_gen_config.py` is correct. UI helpers and config loading have different lifecycles and test surfaces — keeping them separate is the right call.
- TOML structure is well-organized. Sections (`[paths]`, `[moss]`, `[voices.*]`) are logically grouped and the initial shape is complete for v0.3.0 scope.
- Non-goals for `voice_gen_utils.py` are explicitly stated — this will prevent scope creep during TASK-012.
- Migration order (text_to_audio.py first because fewer stages) is the correct sequence.
- Lilybelle WSL path normalization risk is correctly identified.
- `tomllib` (Python 3.11+ standard library) is the right choice for read-only TOML. The explicit fallback guidance is good practice.
- Review checkpoints at each task give clear acceptance criteria for each implementation step.

## Risks

**Missing guidance on `voice_gen.toml` not found:**
The architecture states config is loaded from the repository root by default but does not specify behavior when the file is absent. If a user runs a script from a different working directory or on a fresh clone without the config file, the failure mode is undefined. Recommend: fail fast with a clear error message naming the expected path and pointing to the README. Do not silently generate defaults (would overwrite user edits).

**WSL path normalization must survive config migration:**
The existing `normalize_config_for_windows()` in `text_to_audio.py` is triggered when a config path contains `/mnt/`. When the Lilybelle config path moves into `voice_gen.toml`, that function still needs to fire at the right point. The architecture identifies this as a risk but does not specify where the normalization hook lives in the new config loading flow. This should be resolved in the TASK-013 review checkpoint.

## Suggested Improvements

**Anchor `voice_gen.toml` to `__file__`, not CWD:**
`voice_gen_config.py` should locate the TOML file relative to its own location (`Path(__file__).parent.parent`) rather than `Path.cwd()` or a bare filename. This makes the scripts invocable from any working directory — a common scenario when calling from a bat file or pipeline. This is the one actionable change I'd ask be confirmed before TASK-013 implementation begins.

**Non-blocking observations:**
1. TOML uses forward slashes (`D:/AI_Models/...`). This is fine — `pathlib.Path` on Windows handles both. The `normalize_config_for_windows()` hook remains necessary only for YAML files Codex generates on a WSL host, not for the TOML itself.
2. The architecture notes `voice_gen.toml` is intentionally explicit for v0.3.0 with auto-discovery as a later addition. This is the correct call — explicit first, discoverable later.
3. Config validation timing should align with the existing `check_dependencies()` call site in `text_to_audio.py`. Both should fire at the same pre-flight stage before interactive prompts.

## Acceptance Recommendation

**Accepted.** Architecture is approved to proceed to TASK-012 implementation.

One item to confirm before TASK-013 begins: `voice_gen_config.py` must anchor to `__file__` rather than CWD. All other observations are non-blocking and can be addressed during respective task review checkpoints.

Implementation order confirmed: TASK-012 → TASK-013 → TASK-014 as documented.
