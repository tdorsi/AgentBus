# REVIEW-015

Reviewer: Claude CLI
Date: 2026-06-13
Related Task: EPIC-003 (task breakdown — TASK-022 through TASK-025, not yet created)
Artifact: Gemini CLI EPIC-003 breakdown in `comms/inbox_claude.md` MSG-20260613-016; dispatch DISPATCH-20260613-004
Status: Accepted with Changes

## Summary

Gemini CLI's EPIC-003 (Text_to_Audio Enhancements) breakdown is correctly scoped to the two themes Thomas authorized in DISPATCH-20260613-004 — per-chunk WAV preservation (#4b) and progress/ETA reporting (pulled forward from EPIC-004), with EPIC-005 batch input correctly excluded. The four-task split (TASK-022–025) and ordering are sensible. The main gap is that the acceptance criteria are thin relative to the EPIC-002 standard; they need fleshing out before Stan creates the board tasks. No scope or governance problems. Two items are noted for Gemini to confirm.

## Governance / Scope Check

✓ DISPATCH-20260613-004 confirms Thomas authorized EPIC-003 with Gemini CLI as owner and Claude CLI as reviewer, folding EPIC-004 (Progress Reporting) into EPIC-003 and deferring EPIC-005. Breakdown matches that scope. No overlap with EPIC-001 (progress/ETA and keep-chunks are genuinely new — unlike the earlier EPIC-003 items #4a/#4c, which EPIC-001 already delivered and which are correctly absent here).

## Task-by-Task

| Task | Theme | Assessment |
| --- | --- | --- |
| TASK-022 | `--keep-chunks` per-chunk WAV | Accept, tighten criteria (C1) |
| TASK-023 | Progress tracking | Accept, tighten criteria (C2) |
| TASK-024 | ETA reporting | Accept, specify basis (C3) |
| TASK-025 | Docs + validation | Accept (C4) |

## Findings / Required Changes (fold into the board tasks)

**C1 — TASK-022 (`--keep-chunks`) needs explicit criteria:**
- Default is OFF; absent the flag, behavior is identical to today (no extra files).
- Specify the naming scheme (e.g. `<output_stem>_chunk_001.wav`) and that chunks are written to the output directory alongside the final WAV.
- The final concatenated output must be byte-for-byte unchanged whether or not the flag is set.
- Behavior under `--dry-run` must be a no-op (dry-run generates no audio), not an error.

**C2 — TASK-023 (progress) needs criteria:**
- Use the shared `voice_gen_utils` console helpers (encoding-safe `info`/`ok`) for output consistency with the rest of the tool.
- "Processing chunk X of Y" should appear only during real synthesis, not under `--dry-run`.
- Must not corrupt or interleave with existing log output.

**C3 — TASK-024 (ETA) needs the calculation basis specified:**
- Base the estimate on completed-chunk throughput (chars/sec or sec/chunk of finished chunks), per the original feature-log #5 proposal.
- For `--voice all`, account for the remaining voices, not just remaining chunks of the current voice.
- Define behavior before the first chunk completes (e.g. "estimating…").

**C4 — TASK-025 (docs/validation):** acceptance should include an actual end-to-end run of `text_to_audio.py` with `--keep-chunks` plus progress/ETA on a multi-chunk input, recorded for review — matching the EPIC validation standard.

**C5 — Per-task verification:** each task should carry a compile check (`py_compile text_to_audio.py`) plus a relevant run/dry-run verification, as EPIC-002 tasks did.

**C6 — Commit tag:** `[v0.3.0][vg_e003][TASK-0NN]` per DISPATCH-20260613-004.

**C7 — EPIC-003 detail file:** the dispatch required populating `artifacts/Planning/PR_Voice_Gen/epics/EPIC-003_text_to_audio_enhancements.md`; at the reviewed commit (`e40b8f3`) it is still empty. Confirm it is committed and pushed.

## Answer to Gemini's Implied Questions

- **Ordering (023 → 024 → 022 → 025):** good — ETA depends on progress tracking, so 023 before 024 is correct; keep-chunks (022) is independent and fine third; docs last.

## Acceptance Recommendation

**Accepted with Changes.** The breakdown is correctly scoped and well-ordered; create TASK-022–025 once the acceptance criteria are tightened per C1–C5, the commit tag is set (C6), and the EPIC-003 detail file is confirmed populated (C7). Gemini implementation begins only after the board tasks exist, per the DISPATCH-20260613-004 gates. No Product Owner decisions are outstanding for EPIC-003.
