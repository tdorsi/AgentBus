# EPIC-002: Voice_Gen Hardening

Status: Active
Owner: Codex CLI
Reviewer: Claude CLI
Release: v0.3.0
Branch: `vg_e002_voice_gen_hardening`
Parent Branch: `vg_e001_shared_config`
Created: 2026-06-13
Updated: 2026-06-13

## Objective

Harden `voice_gen.py` before additional Voice_Gen feature work by adding non-destructive output behavior, improving cancellation and logging reliability, and adding a scan-only planning mode.

## Background

EPIC-001 moved shared utilities, configuration, voice discovery, and defaults into reusable infrastructure. EPIC-002 builds on that foundation and focuses only on the training pipeline (`voice_gen.py`).

The scope comes from `comms/voice-gen_0.2.0_feature_request.md`, Codex's EPIC-002 breakdown in `comms/inbox_claude.md` MSG-20260613-008, Claude's `reviews/REVIEW-011.md`, and Thomas's `DECISION-20260613-004`.

## In Scope

- `TASK-016`: overwrite protection with fail-by-default behavior, `--from-stage` resume carve-out, and logged `--force`.
- `TASK-018`: graceful `KeyboardInterrupt` handling with exit code 130.
- `TASK-019`: dependency-check logging order so ffmpeg/ffprobe failures reach the run log.
- `TASK-020`: `--log-file` CLI plumbing into the existing shared logging helper.
- `TASK-021`: `--dry-run` / scan-only mode.

## Out of Scope

- `TASK-017` handler-clear implementation. It is dropped because EPIC-001 already delivered `logger.handlers.clear()` through `voice_gen_utils.setup_logging()`.
- Text-to-audio enhancements, including per-chunk preservation and default output improvements. Those belong to later EPIC-003 scope.
- Progress reporting and batch input processing. Those remain later epics.

## Acceptance Criteria

- All active EPIC-002 tasks are implemented on `vg_e002_voice_gen_hardening`.
- Each task is committed with `[v0.3.0][vg_e002][TASK-0NN]`.
- Each task receives Claude CLI review before being marked done.
- Verification for each task includes a compile check plus a relevant dry-run or scan-style validation where applicable.
- Existing EPIC-001 behavior remains intact.
- `--from-stage` resume remains usable for iterative training runs.

## Implementation Order

1. `TASK-016` overwrite protection.
2. `TASK-018` graceful cancellation.
3. `TASK-019` dependency-check logging order.
4. `TASK-020` `--log-file` CLI plumbing.
5. `TASK-021` `--dry-run` / scan-only mode.

## Review Notes

- Claude accepted the breakdown with changes in `reviews/REVIEW-011.md`.
- Thomas approved `--force` for TASK-016 and `--dry-run` as the TASK-021 flag name in `DECISION-20260613-004`.
