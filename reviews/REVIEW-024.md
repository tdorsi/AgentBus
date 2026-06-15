# REVIEW-024

Reviewer: Claude CLI
Date: 2026-06-14
Related Task: TASK-021 (EPIC-002 — Voice_Gen dry-run / scan-only mode)
Artifact: Voice_Gen commit `6529caa [v0.3.0][vg_e002][TASK-021] Add voice generation dry run`, branch `vg_e002_voice_gen_hardening__codex__TASK-021`
Status: Accepted

## Summary

TASK-021 adds `--dry-run` to `voice_gen.py`: it runs the input-prep/planning stages (1–4) through reference selection, prints a clear plan summary, then stops before any training/destructive work (stages 5–10). The flag name matches DECISION-20260613-004, the control flow is correct and robust across `--from-stage 1..4`, and no training artifacts are written. EPIC-002 is now fully accepted. Accepted.

## Verification Against Criteria

**Flag name `--dry-run`** ✓ — matches DECISION-20260613-004 (cross-tool consistency with `text_to_audio.py`).

**Runs stages 1–4, reports a plan** ✓ — `print_dry_run_summary()` reports voice, input/output, usable (`{ready} ready clip(s), {long} long file(s)`), split count, cleaned-candidate count, selected reference, an explicit "Stopped: before transcription, downloads, token encoding, fine-tuning, samples, config" line, and the log path; it also mirrors the summary to `log.info`. Matches the scan-only intent (#3a) — validate input audio / reference election before committing to the expensive run.

**Stops before stages 5–10** ✓ — the `if args.dry_run: print_dry_run_summary(...); return` (line ~994–1006) is placed after stage-4 reference selection and *before* `stage5_transcribe` (1010), `stage6_weights` (1022), `stage7_prepare_data` (1027), `stage8_finetune` (1037), `stage9_samples` (1043), and stage-10 config export. Confirmed by line order.

**No destructive training artifacts** ✓ — `samples_dir.mkdir(...)` is guarded `if not args.dry_run:` (and stage 9 creates it only when reached, which dry-run never is). Codex's run confirms only planning artifacts (`.voice_gen_state.json`, `reference.wav`, `clips/…`) are written and that `train_raw.jsonl`, `train_with_codes.jsonl`, `checkpoint/`, `samples/`, and `<voice>.yaml` are absent. Writing `reference.wav`/`clips/` is correct — those are the stage 1–4 outputs the user inspects.

**Robust across `--from-stage 1..4`** ✓ — every stage variable used by the summary (`short`, `long_`, `split_clips`, `all_clips`, `ref_wav`) has both a run-branch (`if from_stage <= N`) and a load-from-state else-branch, so all are defined for any allowed dry-run start. No `NameError` edge case.

**Sensible contradiction guard** ✓ — `if args.dry_run and args.from_stage > 4:` errors cleanly (`err(...)` + `sys.exit(1)`) since dry-run only covers stages 1–4.

**Style / integration** ✓ — uses shared `ui` helpers (`console_line`, `BOLD/CYAN/RESET`, `info/ok/err`); logs `Dry run: %s` in the config banner; compiles clean (`py_compile voice_gen.py voice_gen_utils.py`). Composes correctly with the other EPIC-002 features (TASK-016 overwrite protection still applies to a dry-run into an existing output dir — consistent, not a conflict).

## Acceptance Recommendation

**Accepted.** TASK-021 meets all dry-run/scan-only criteria with correct stage gating, robust variable handling, and no destructive writes. **EPIC-002 (Voice_Gen Hardening) is now complete** — TASK-016/018/019/020/021 all accepted. Next per the roadmap is Phase 3 integration toward the v0.3.0 RC (merge `vg_e002` + `vg_e003` into `vg_e001_shared_config`), once EPIC-003's FU1/TASK-028 real-run validation is also closed.
