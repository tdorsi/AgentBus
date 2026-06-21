# Sprint Board

Watcher-owned aggregate board. This file is a derived view of `tasks/*`; individual task entries under `tasks/` remain authoritative for task details and history.

If this board conflicts with `tasks/*`, correct this board during the next Watcher pass instead of editing task history to match the board.

| Task | Status | Owner | Reviewer | Source |
| --- | --- | --- | --- | --- |
| TASK-001 | Done | Claude CLI | Human operator | `tasks/done.md` |
| TASK-002 | Review / stale pending response | Codex CLI | Thomas / Quill | `tasks/backlog.md`, `comms/broadcast.md` |
| TASK-003 | Review / stale pending response | Codex CLI | Thomas / Quill | `tasks/review.md`, `comms/broadcast.md` |
| TASK-004 | Review | Claude CLI | Thomas / Quill | `tasks/review.md` |
| TASK-005 | Backlog | Thomas / Quill | Thomas / Quill | `tasks/backlog.md` |
| TASK-006 | Review complete - accepted | Codex CLI | Claude CLI | `tasks/review.md` |
| TASK-007 | Review complete - accepted | Codex CLI | Claude CLI | `tasks/review.md` |
| TASK-008 | Done | Codex CLI | Thomas / Quill | `tasks/done.md` |
| TASK-009 | Done | Thomas / Codex CLI | Thomas | `tasks/done.md` |
| TASK-011 | Review complete - accepted | Codex CLI | Claude CLI | `tasks/active.md`, `reviews/REVIEW-004.md` |
| TASK-012 | Review complete - accepted | Codex CLI | Claude CLI | `tasks/review.md`, `reviews/REVIEW-005.md` |
| TASK-013 | Review complete - accepted | Codex CLI | Claude CLI | `tasks/review.md`, `reviews/REVIEW-006.md` |
| TASK-014 | Done / accepted | Codex CLI | Claude CLI | `tasks/review.md`, `reviews/REVIEW-007.md` |
| TASK-015 | Done | Codex CLI | Claude CLI | `tasks/done.md`, `tasks/review.md`, `reviews/REVIEW-010.md` |
| TASK-016 | Done / accepted | Codex CLI | Claude CLI | `tasks/done.md`, `tasks/review.md`, `reviews/REVIEW-012.md` |
| TASK-017 | Dropped (done by EPIC-001) | Codex CLI | Claude CLI | `tasks/backlog.md`, `reviews/REVIEW-011.md` |
| TASK-018 | Done / accepted | Codex CLI | Claude CLI | `tasks/done.md`, `tasks/review.md`, `reviews/REVIEW-013.md` |
| TASK-019 | Done / accepted | Codex CLI | Claude CLI | `tasks/done.md`, `tasks/review.md`, `reviews/REVIEW-014.md` |
| TASK-020 | Done / accepted | Codex CLI | Claude CLI | `tasks/done.md`, `reviews/REVIEW-018.md` |
| TASK-021 | Done / accepted | Codex CLI | Claude CLI | `tasks/done.md`, `reviews/REVIEW-024.md` |
| TASK-022 | Done / accepted | Gemini CLI | Claude CLI | `tasks/done.md`, `reviews/REVIEW-019.md` |
| TASK-023 | Done / accepted | Gemini CLI | Claude CLI | `tasks/done.md`, `reviews/REVIEW-021.md` |
| TASK-024 | Done / accepted | Gemini CLI | Claude CLI | `tasks/done.md`, `reviews/REVIEW-022.md` |
| TASK-025 | Done / accepted (w/ follow-ups) | Gemini CLI | Claude CLI | `tasks/done.md`, `reviews/REVIEW-023.md` |
| TASK-026 | Done / accepted (w/ follow-ups) | Codex CLI | Claude CLI | `tasks/done.md`, `tasks/review.md`, `reviews/REVIEW-017.md` |
| TASK-027 | Done / accepted | Codex CLI | Claude CLI | `tasks/done.md`, `tasks/review.md`, `reviews/REVIEW-020.md` |
| TASK-028 | Done / accepted | Gemini CLI | Claude CLI | `tasks/done.md`, `reviews/REVIEW-025.md` |
| TASK-029 | Done / accepted | Gemini CLI | Claude CLI | `tasks/done.md`, `reviews/REVIEW-026.md` |
| TASK-030 | Done / accepted | Codex CLI | Claude CLI | `tasks/done.md`, `reviews/REVIEW-027.md` |

## Backlog

| Task | Owner | Status |
| --- | --- | --- |
| TASK-005 | Thomas / Quill | Backlog |

## Ready

**Phase 3 — integration — is COMPLETE; the v0.3.0 RC is ASSEMBLED** (2026-06-21). Both epic merges are accepted and `vg_e001_shared_config` @ **`5ed908f`** now contains EPIC-001 + EPIC-003 + EPIC-002.

- **TASK-029 (Gemini):** merge `vg_e003` → `vg_e001_shared_config`. **DONE / accepted** (REVIEW-026, merge `ffc7b5e`). DISPATCH-20260621-001 Complete.
- **TASK-030 (Codex):** merge `vg_e002` → `vg_e001_shared_config`. **DONE / accepted** (REVIEW-027, merge `5ed908f`). DISPATCH-20260621-002 Complete. Claude verified the only conflict surface (`README.md`) resolved as a correct union; both epics' source preserved byte-identical (`git diff 5ed908f ffc7b5e -- text_to_audio.py` and `git diff 5ed908f 6529caa -- voice_gen.py` both empty); compiles + integrated RC dry-run smoke clean.
- **v0.3.0 RC = `vg_e001_shared_config` @ `5ed908f`.** **Next step is a Thomas / Quill decision: declaring/tagging and cutting the final v0.3.0 release** (not a Watcher or reviewer action). Claude's review queue is empty.
- **EPIC-002** Voice_Gen Hardening: COMPLETE — TASK-016/018/019/020/021 accepted (TASK-017 dropped).
- **EPIC-003** Text_to_Audio Enhancements: COMPLETE — TASK-022/023/024/025 accepted and runtime-validated by TASK-028 (REVIEW-025; FU1 closed).
- Deferred to a later phase (per Thomas, EVENT-20260621-004): onnxruntime BFC Arena ~2.3 GB OOM on very long runs — out of scope for v0.3.0. Optional future refinement: warmup-inflated initial ETA.

## In Progress

No in-progress tasks. (Phase 3 complete; v0.3.0 RC assembled at `5ed908f`, awaiting Thomas / Quill release decision.)

## Review

| Task | Owner | Reviewer | Status |
| --- | --- | --- | --- |
| TASK-003 | Codex CLI | Thomas / Quill | Review / stale pending response marker |
| TASK-004 | Claude CLI | Thomas / Quill | Review |

## Blocked

No blocked items. (TASK-030 gate satisfied by TASK-029 acceptance, REVIEW-026.)

## Done

| Task | Owner | Completed |
| --- | --- | --- |
| TASK-001 | Claude CLI | 2026-05-31 |
| TASK-008 | Codex CLI | 2026-05-31 |
| TASK-009 | Thomas / Codex CLI | 2026-06-01 |
| TASK-014 | Codex CLI | 2026-06-04 accepted by Claude CLI |
| TASK-015 | Codex CLI | 2026-06-13 accepted by Claude CLI |
| TASK-016 | Codex CLI | 2026-06-13 accepted by Claude CLI (REVIEW-012) |
| TASK-018 | Codex CLI | 2026-06-13 accepted by Claude CLI (REVIEW-013) |
| TASK-019 | Codex CLI | 2026-06-13 accepted by Claude CLI (REVIEW-014) |
| TASK-020 | Codex CLI | 2026-06-14 accepted by Claude CLI (REVIEW-018) |
| TASK-022 | Gemini CLI | 2026-06-14 accepted by Claude CLI (REVIEW-019) |
| TASK-027 | Codex CLI | 2026-06-14 accepted by Claude CLI (REVIEW-020) |
| TASK-026 | Codex CLI | 2026-06-14 accepted w/ follow-ups by Claude CLI (REVIEW-017) |
| TASK-023 | Gemini CLI | 2026-06-14 accepted by Claude CLI (REVIEW-021) |
| TASK-024 | Gemini CLI | 2026-06-14 accepted by Claude CLI (REVIEW-022) |
| TASK-025 | Gemini CLI | 2026-06-14 accepted w/ follow-ups by Claude CLI (REVIEW-023) |
| TASK-021 | Codex CLI | 2026-06-15 accepted by Claude CLI (REVIEW-024) — **EPIC-002 complete** |
| TASK-028 | Gemini CLI | 2026-06-15 accepted by Claude CLI (REVIEW-025) — **EPIC-003 runtime-validated; FU1 closed** |
| TASK-029 | Gemini CLI | 2026-06-21 accepted by Claude CLI (REVIEW-026) — **EPIC-003 merged into v0.3.0 RC** (`ffc7b5e`) |
| TASK-030 | Codex CLI | 2026-06-21 accepted by Claude CLI (REVIEW-027) — **EPIC-002 merged; v0.3.0 RC assembled** (`5ed908f`) |

## Validation Cycle

The TASK-015 validation cycle is recorded as:

1. Review Accepted: `EVENT-20260613-001` mirrors TASK-014 acceptance.
2. Board Updated: this file mirrors TASK-014 as done and TASK-015 as review requested after completion.
3. Event Logged: `watcher/event_log.md` records events 001-004.
4. Dispatch Generated: `DISPATCH-20260613-001` assigns Codex CLI to TASK-015.
5. Broadcast Generated: `MSG-20260613-003` announces the status change.

## Accepted Review Pass

The REVIEW-010 Watcher pass is recorded as:

1. Review Accepted: `EVENT-20260613-006` mirrors TASK-015 acceptance from `reviews/REVIEW-010.md`.
2. Board Updated: this file mirrors TASK-015 as done.
3. Event Logged: `watcher/event_log.md` records EVENT-20260613-006.
4. Dependent Work Checked: no dependent work dispatched; Watcher v1 is complete.
5. Broadcast Generated: `MSG-20260613-005` announces TASK-015 completion.
