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
| TASK-021 | Paused (pending TASK-027) | Codex CLI | Claude CLI | `tasks/backlog.md` |
| TASK-022 | Done / accepted | Gemini CLI | Claude CLI | `tasks/done.md`, `reviews/REVIEW-019.md` |
| TASK-023 | Paused (pending TASK-027) | Gemini CLI | Claude CLI | `tasks/backlog.md` |
| TASK-024 | Paused (pending TASK-027) | Gemini CLI | Claude CLI | `tasks/backlog.md` |
| TASK-025 | Paused (pending TASK-027) | Gemini CLI | Claude CLI | `tasks/backlog.md` |
| TASK-026 | Done / accepted (w/ follow-ups) | Codex CLI | Claude CLI | `tasks/done.md`, `tasks/review.md`, `reviews/REVIEW-017.md` |
| TASK-027 | Review (submitted `602e6b5`, awaiting Claude) | Codex CLI | Claude CLI | `tasks/review.md`, AgentBus commit `602e6b5` |

## Backlog

| Task | Owner | Status |
| --- | --- | --- |
| TASK-005 | Thomas / Quill | Backlog |

## Ready / Paused

**EPIC-002 and EPIC-003 are PAUSED pending TASK-027** (DECISION-20260614-002, approved by Thomas 2026-06-14). No new EPIC-002/003 implementation resumes until the AgentBus per-agent-clone isolation is complete.

EPIC-002 Voice_Gen Hardening — branch `vg_e002_voice_gen_hardening`. Owner Codex CLI, Reviewer Claude CLI. TASK-016/018/019/020 accepted; **TASK-021 held**.

| Task | Owner | Reviewer | Priority | Notes |
| --- | --- | --- | --- | --- |
| TASK-021 | Codex CLI | Claude CLI | High | `--dry-run` / scan-only mode — **held (pending TASK-027)** |

TASK-017 dropped per REVIEW-011 F1 (handler-clear already delivered by EPIC-001).

EPIC-003 Text_to_Audio Enhancements (combined w/ Progress Reporting) — branch `vg_e003_text_to_audio_enhancements`. Owner Gemini CLI, Reviewer Claude CLI. Under DISPATCH-20260613-005. TASK-022 accepted; **TASK-023/024/025 held**.

| Task | Owner | Reviewer | Priority | Notes |
| --- | --- | --- | --- | --- |
| TASK-023 | Gemini CLI | Claude CLI | Medium | Progress reporting — **held (pending TASK-027)** |
| TASK-024 | Gemini CLI | Claude CLI | Medium | ETA — **held (pending TASK-027)** |
| TASK-025 | Gemini CLI | Claude CLI | Medium | Docs + end-to-end validation — **held (pending TASK-027)** |

## In Progress

No in-progress tasks currently mirrored.

## Review

| Task | Owner | Reviewer | Status |
| --- | --- | --- | --- |
| TASK-027 | Codex CLI | Claude CLI | Review — AgentBus clone isolation submitted (`602e6b5`), awaiting Claude |
| TASK-003 | Codex CLI | Thomas / Quill | Review / stale pending response marker |
| TASK-004 | Claude CLI | Thomas / Quill | Review |

## Blocked

No blocked tasks currently mirrored.

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
| TASK-026 | Codex CLI | 2026-06-14 accepted w/ follow-ups by Claude CLI (REVIEW-017) |

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
