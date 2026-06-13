# REVIEW-011

Reviewer: Claude CLI
Date: 2026-06-13
Related Task: EPIC-002 (task breakdown — TASK-016 through TASK-021, not yet created)
Artifact: Codex CLI EPIC-002 breakdown in `comms/inbox_claude.md` MSG-20260613-008; branch `vg_e002_voice_gen_hardening`
Status: Accepted with Changes

## Summary

Codex's EPIC-002 (Voice_Gen Hardening) task breakdown is well-structured: all six items from `comms/voice-gen_0.2.0_feature_request.md` map cleanly to TASK-016–021, with Critical-first ordering. Two of the six items, however, are already wholly or partly delivered by EPIC-001, and one acceptance criterion needs a carve-out to avoid breaking resume. With the changes below, the breakdown is ready for Stan to create the (reduced) task set. Two points need Product Owner sign-off (flagged P-O).

## Item Mapping (complete)

| Task | Feature item | Priority | Status of finding |
| --- | --- | --- | --- |
| TASK-016 | #3b Overwrite protection | Critical | Accept with tightened criteria |
| TASK-017 | #2a Handler clear | High | **Already done by EPIC-001 — drop/verify** |
| TASK-018 | #2b KeyboardInterrupt | High | Accept |
| TASK-019 | #2c Dependency-check logging order | High | Accept |
| TASK-020 | #2d `--log-file` override | Medium | **Mostly done — plumbing only** |
| TASK-021 | #3a Dry-run / scan-only | High | Accept (flag name decided below) |

## Findings

### F1 — TASK-017 is already satisfied by EPIC-001 (drop or downgrade)

`voice_gen_utils.setup_logging()` already calls `logger.handlers.clear()` (voice_gen_utils.py:49), and `voice_gen.py:84-86` routes its `setup_logging()` through that shared helper. The #2a duplicate-handler gap was closed during EPIC-001 (TASK-012). Recommend **dropping TASK-017** or reducing it to a one-line verification note in another task — there is no remaining implementation work.

### F2 — TASK-020 is plumbing only, not a from-scratch feature

The shared `setup_logging()` already accepts an optional `log_file` parameter (voice_gen_utils.py:41). `voice_gen.py` simply does not expose a `--log-file` CLI argument or pass it through. TASK-020 is therefore small: add the arg and thread it into the existing parameter. Its default must continue to resolve to the configured `LOG_DIR` (EPIC-001 config). Keep the task, but scope it as wiring, not new logging machinery.

### F3 — TASK-016 must carve out `--from-stage` resume

Overwrite protection must treat a legitimate `--from-stage` resume as an allowed write into the existing output directory, not a collision. Without this, the Critical safety feature would break the documented resume workflow. Add an explicit acceptance criterion: "Resuming with `--from-stage` into an existing output directory is permitted and is not treated as a collision."

### F4 — Commit tag is `[v0.3.0]` here (correct, opposite of AgentBus)

EPIC-002 is Voice_Gen *product* work, so commits use `[v0.3.0][vg_e002][TASK-0NN]` per `procedures/branching_strategy.md`. This is intentionally different from the `[agentbus]` track used for Watcher/governance work. Worth stating so the AgentBus convention is not carried over.

### F5 — Populate the EPIC-002 detail file

`artifacts/Planning/PR_Voice_Gen/epics/EPIC-002_voice_gen_hardening.md` is still a 0-byte stub. This breakdown should populate it with the epic objective and acceptance criteria so the epic is self-documenting before tasks are activated.

### F6 — Standardize per-task verification

EPIC-001 tasks each carried a verification step (compile + dry-run). Some EPIC-002 criteria mention "small local verification," others do not. Recommend each task include a compile check plus a relevant dry-run/scan verification, matching the EPIC-001 standard.

## Answers to Codex's Review Questions

1. **Override flag (P-O sign-off):** Fail-by-default is required (the Critical behavior). Recommend including `--force` as an optional, explicit, and **logged** override, provided it does not interfere with `--from-stage` resume. Final call on whether to ship `--force` in v0.3.0 is Thomas's.
2. **Dry-run flag name:** **`--dry-run`** — `text_to_audio.py` already uses `--dry-run`; matching it reduces cross-tool divergence, which was the explicit goal of EPIC-001.
3. **Merge TASK-019 / TASK-020:** **Keep separate.** Log-ordering correctness (019) and a new CLI flag (020) are distinct concerns with independent acceptance; separate tasks review more cleanly.

## Net Effect

After changes, EPIC-002 is ~4.5 tasks of real work rather than 6:
- TASK-016 (Critical, with resume carve-out), TASK-018, TASK-019, TASK-021 — full tasks.
- TASK-020 — reduced to CLI plumbing.
- TASK-017 — dropped or folded into a verification note.

## Acceptance Recommendation

**Accepted with Changes.** Recommend Stan create the board tasks with these adjustments: drop/downgrade TASK-017, scope TASK-020 as plumbing, add the `--from-stage` carve-out to TASK-016, confirm the `[v0.3.0][vg_e002]` commit tag, and have the breakdown populate the EPIC-002 detail file. Decide `--dry-run` as the flag name (Q2) and add a logged `--force` to TASK-016 pending Thomas's sign-off (Q1). Codex implementation should begin only after the adjusted tasks exist on `state/sprint_board.md`, per the DISPATCH-20260613-002 gates.
