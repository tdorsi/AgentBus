# REVIEW-012

Reviewer: Claude CLI
Date: 2026-06-13
Related Task: TASK-016 (EPIC-002 Voice_Gen Hardening)
Artifact: Voice_Gen commit `9a52d61 [v0.3.0][vg_e002][TASK-016] Add overwrite protection`, branch `vg_e002_voice_gen_hardening`
Status: Accepted

## Summary

TASK-016 adds fail-by-default overwrite protection to `voice_gen.py` with a logged `--force` override and a correct `--from-stage` resume carve-out. The implementation matches the REVIEW-011 adjustments and DECISION-20260613-004 exactly, is purely additive, and is non-destructive (it exits before any output is written). Accepted.

## Verification Against Criteria

**Fail-by-default protection** ✓
`enforce_output_protection(output_dir, from_stage, force)` is called in `main()` after path validation and the input-dir check but **before** any output directory is created or written (`clips_dir`/`samples_dir`/`checkpoint_dir` follow the call). On collision it prints a clear message and `sys.exit(1)` — nothing is overwritten. `find_output_collisions()` flags the existing output dir plus critical artifacts (`reference.wav`, `train_raw.jsonl`, `train_with_codes.jsonl`, `.voice_gen_state.json`, `clips/`, `checkpoint/`, `samples/`).

**`--from-stage` resume carve-out (DECISION-004)** ✓
`if from_stage > 1: info(...); log.info(...); return` — resume is checked first and allowed without collision blocking. The `--from-stage` default is `1`, so only stages 2+ count as resume; a fresh run (stage 1) is correctly protected. This is the carve-out REVIEW-011 F3 required.

**Logged `--force` override (DECISION-004)** ✓
`if force: warn(...); log.warning(...)` plus a per-path `log.warning` of each existing artifact, then proceeds. Override is explicit on console and in the log. Because resume is evaluated before force, `--force` does not interfere with `--from-stage` resume.

**Clear user guidance** ✓
On block: "Refusing to reuse an existing output directory for a fresh run. Use --from-stage N to resume an existing run, or --force to intentionally reuse this output path." `--force` is documented in the module usage header and README.

**EPIC-002 detail file populated (REVIEW-011 F5)** ✓
`artifacts/Planning/PR_Voice_Gen/epics/EPIC-002_voice_gen_hardening.md` is now 56 lines (previously a 0-byte stub).

**Commit tag (REVIEW-011 F4)** ✓
`[v0.3.0][vg_e002][TASK-016]` — correct Voice_Gen product track.

**No regression** ✓
Change is additive: new constants, one new arg (`--force`), one new function, one call site, one log line. When the output dir does not exist or when resuming, behavior is unchanged.

## Verification (Codex, spot-checked)

- `python -m py_compile voice_gen.py`; `python voice_gen.py --help`.
- Collision run exits 1 before artifact writes, advising `--from-stage`/`--force`.
- `enforce_output_protection(Path('.'), 2, False)` → resume carve-out allowed.
- `enforce_output_protection(Path('.'), 1, True)` → force override allowed.

Logic confirmed by inspection of commit `9a52d61`.

## Observations (non-blocking)

- `find_output_collisions()` always includes the output dir itself when it exists, so directory existence alone blocks a fresh run even with no critical artifacts. This is intentional fail-safe behavior consistent with the Critical #3b intent (the per-voice output dir is meant to be unique per run); the critical-file/dir list adds useful detail to the log. No change needed.

## Acceptance Recommendation

**Accepted.** TASK-016 satisfies all criteria from REVIEW-011 and DECISION-20260613-004: fail-by-default overwrite protection, logged `--force`, correct `--from-stage` resume carve-out, populated EPIC-002 detail file, correct commit tag, and no regression. Recommend TASK-016 move to done; TASK-018 (next per DISPATCH-20260613-003 ordering) is clear to proceed.
