# State Snapshot

Use this file for concise, human-readable snapshots of AgentBus operating state.

## SNAPSHOT-20260601-001

Date: 2026-06-01
Owner: Codex CLI
Related Task: TASK-006

### Source of Truth

`origin/main` is the source of truth. Local agents must fetch before reading local files as authoritative.

### Current Governance State

- Startup, task claiming, review response, and update-check procedures are tracked under `procedures/`.
- Agent task visibility is tracked in `state/agent_status.md`.
- Sync events are tracked in `state/sync_log.md`.
- Point-in-time state summaries are tracked in this file.

### Current Review State

- TASK-003 has Quill review: accepted with follow-ups.
- TASK-004 is submitted for review by Claude CLI.
- TASK-006 is submitted to Claude CLI for review after implementation.

## SNAPSHOT-20260601-002

Date: 2026-06-01
Owner: Codex CLI
Related Task: TASK-007

### Review Workflow State

- `reviews/README.md` exists.
- `reviews/review_template.md` exists.
- `reviews/REVIEW-001.md` exists.
- `reviews/REVIEW-002.md` exists locally and is being added to shared history.
- `tasks/review.md` is the review queue.
- Procedures now require stale-state findings to be revalidated after syncing with `origin/main`.

## SNAPSHOT-20260601-003

Date: 2026-06-01
Owner: Codex CLI
Related Task: TASK-008

### TTS Setup State

- Claude CLI Hannah server remains assigned to port 8765.
- Codex CLI Lori server is being configured for port 8766.
- MOSS-TTS server defaults must continue to load Hannah unless CLI args override them.
- Runtime acceptance depends on hook trust/reload and Thomas confirming Lori audio.

## SNAPSHOT-20260601-004

Date: 2026-06-01
Owner: Codex CLI
Related Task: EPIC-001 / TASK-011 through TASK-014

### Voice_Gen v0.3.0 Planning State

- Voice_Gen v0.3.0 planning documents are tracked under `artifacts/Planning/`.
- `procedures/branching_strategy.md` defines Epic branches and the `vg_e001_shared_config` branch for EPIC-001.
- EPIC-001 has been split into TASK-011 through TASK-014.
- TASK-011 is active with Codex CLI implementing and Claude CLI assigned to architecture review.

### Attention Items

- Thomas / Quill should confirm the TASK-011 through TASK-014 breakdown matches intended EPIC-001 scope.
- Claude CLI should review TASK-011 architecture notes once Codex posts them.

## SNAPSHOT-20260613-001

Date: 2026-06-13
Owner: Codex CLI
Related Task: TASK-015

### Watcher Governance State

- Thomas approved the Watcher Governance Proposal v1 and authorized TASK-015.
- The Watcher is a manually activated role, not a service.
- Watcher v1 is additive; existing task, review, and update procedures remain valid.
- Codex CLI owns implementation and Claude CLI owns review.
- `state/sprint_board.md` is Watcher-owned aggregate state derived from `tasks/*`.
- `watcher/dispatch_queue.md` and `watcher/event_log.md` are Watcher-owned operational state.

### Current Validation Cycle

- TASK-014 accepted review is used as the Review Accepted trigger.
- TASK-015 is dispatched to Codex CLI through `DISPATCH-20260613-001`.
- Events are recorded in `watcher/event_log.md`.
- The status-change broadcast is recorded as `MSG-20260613-003`.

## SNAPSHOT-20260613-002

Date: 2026-06-13
Owner: Watcher pass performed by Codex CLI
Related Task: TASK-015

### Watcher Review Closure State

- Claude CLI accepted TASK-015 in `reviews/REVIEW-010.md`.
- TASK-015 is done and recorded in `tasks/done.md`.
- `state/sprint_board.md` mirrors TASK-015 as Done.
- `watcher/event_log.md` records the accepted-review closure as EVENT-20260613-006.
- `comms/broadcast.md` records the completion status change as MSG-20260613-005.
- No dependent work was dispatched.

## SNAPSHOT-20260613-003

Date: 2026-06-13
Owner: Codex CLI
Related Task: EPIC-002

### EPIC-002 Planning State

- Stan dispatched EPIC-002 Voice_Gen Hardening to Codex CLI through DISPATCH-20260613-002.
- Codex created and pushed Voice_Gen branch `vg_e002_voice_gen_hardening` from `vg_e001_shared_config`.
- Codex posted the proposed TASK-016+ breakdown to Claude CLI in MSG-20260613-008.
- No implementation has started.
- Implementation remains gated until Claude reviews the breakdown and Stan creates TASK-016+ on the board.

## SNAPSHOT-20260613-004

Date: 2026-06-13
Owner: Codex CLI
Related Task: TASK-016

### TASK-016 State

- Stan created EPIC-002 tasks and cleared Codex to begin implementation under DISPATCH-20260613-003.
- Codex claimed TASK-016 first, per the required implementation order.
- Voice_Gen branch: `vg_e002_voice_gen_hardening`.
- Scope: fail-by-default overwrite protection, `--from-stage` resume carve-out, and logged `--force`.

## SNAPSHOT-20260613-003

Date: 2026-06-13
Owner: Watcher (Stan)
Related Task: EPIC-002

### Voice_Gen Development Resumed

- EPIC-001 (Shared Configuration Framework) is complete; v0.3.0 development has resumed.
- Thomas authorized EPIC-002 (Voice_Gen Hardening, Phase 2) with Codex CLI as owner and Claude CLI as reviewer.
- Branch `vg_e002_voice_gen_hardening` is to be created from `vg_e001_shared_config`.
- DISPATCH-20260613-002 assigns the claim/branch/breakdown work to Codex CLI; EVENT-20260613-007/008 record the activation and dispatch.

### Workflow Gates (EPIC-002)

1. Codex proposes the task breakdown when claiming.
2. Claude reviews the breakdown and posts notable concerns.
3. Watcher creates the resulting tasks (TASK-016+) on `state/sprint_board.md` after Claude's review.
4. Codex begins implementation once the tasks exist.

### Open With Thomas (not yet dispatched)

- EPIC-003 scope (thin after EPIC-001 absorbed items 4a/4c/4d).
- Parallel-execution model with one implementer (Codex) and one reviewer (Claude).
- Overall epic-scoping ownership.

## SNAPSHOT-20260613-004

Date: 2026-06-13
Owner: Watcher (Stan)
Related Task: EPIC-002 / TASK-016, TASK-018, TASK-019, TASK-020, TASK-021

### EPIC-002 Tasks Active

- Codex's EPIC-002 breakdown was reviewed by Claude (REVIEW-011, Accepted with Changes) and the adjusted task set is now on the board.
- Created: TASK-016 (Critical), TASK-018, TASK-019, TASK-021 (full) and TASK-020 (plumbing). TASK-017 dropped — handler-clear already delivered by EPIC-001.
- Thomas signed off the open scope questions in DECISION-20260613-004: TASK-016 ships fail-by-default overwrite protection + logged `--force` (no interference with `--from-stage` resume); TASK-021 uses `--dry-run`.
- DISPATCH-20260613-003 clears Codex to implement on `vg_e002_voice_gen_hardening` in suggested order; Claude reviews each task.
- Events: EVENT-20260613-009 through -012.

### Note (ID hygiene)

Two SNAPSHOT-20260613-003 entries exist above — one authored by a parallel Codex pass and one by Stan during the EPIC-002 activation. Both are retained per append-only policy; this snapshot (-004) is the current operating summary. Future snapshots continue from -004.

### Open With Thomas (not yet dispatched)

- EPIC-003 scope, owner, and parallel-execution model with the current single-implementer team.

## SNAPSHOT-20260613-005

Date: 2026-06-13
Owner: Watcher (Stan)
Related Task: EPIC-002 / TASK-016

### EPIC-002 In Flight

- TASK-016 (overwrite protection, Critical) is implemented and in review — Voice_Gen commit `9a52d61` on `vg_e002_voice_gen_hardening`. Board mirrors it as Review (EVENT-20260613-013).
- The EPIC-002 detail file is now populated.
- TASK-018/019/020/021 remain Ready under DISPATCH-20260613-003.
- Awaiting Claude CLI's TASK-016 review outcome (route to `comms/inbox_watcher.md`).

### Note (ID hygiene)

Earlier passes left duplicate SNAPSHOT-20260613-003 and -004 IDs (parallel Codex/Stan writes), retained per append-only policy. This `-005` is the current operating summary; future snapshots continue from `-005`.

### Open With Thomas (not yet dispatched)

- EPIC-003 scope, owner, and the parallel-execution model with the current single-implementer team.

## SNAPSHOT-20260613-006

Date: 2026-06-13
Owner: Watcher (Stan)
Related Task: EPIC-002 / TASK-016

### EPIC-002 Progress: 1 of 5 accepted

- TASK-016 (overwrite protection, Critical) **accepted** by Claude CLI (REVIEW-012); mirrored to Done on the board and recorded in `tasks/done.md`. Event EVENT-20260613-014.
- TASK-017 dropped (delivered by EPIC-001).
- TASK-018 (KeyboardInterrupt) is next per the suggested order and is Ready; TASK-019/020/021 remain Ready under DISPATCH-20260613-003.
- No new dispatch needed; DISPATCH-20260613-003 covers the remaining tasks.

### Open With Thomas (not yet dispatched)

- EPIC-003 scope, owner, and the parallel-execution model with the current single-implementer team.

## SNAPSHOT-20260613-007

Date: 2026-06-13
Owner: Watcher (Stan)
Related Task: EPIC-002 / TASK-018

### EPIC-002 Progress: TASK-018 in review

- TASK-016 (overwrite protection, Critical) remains Done / accepted.
- TASK-018 (graceful KeyboardInterrupt) is implemented and in review — Voice_Gen commit `c2d62e8` on `vg_e002_voice_gen_hardening`. Board mirrors it as Review (EVENT-20260613-015).
- TASK-019/020/021 remain Ready under DISPATCH-20260613-003.
- Awaiting Claude CLI's TASK-018 review outcome (route to `comms/inbox_watcher.md`).

### Open With Thomas (not yet dispatched)

- EPIC-003 scope, owner, and the parallel-execution model with the current single-implementer team.

## SNAPSHOT-20260613-008

Date: 2026-06-13
Owner: Watcher (Stan)
Related Task: EPIC-002 / TASK-018

### EPIC-002 Progress: 2 of 5 accepted

- TASK-018 (graceful KeyboardInterrupt) **accepted** by Claude CLI (REVIEW-013); mirrored to Done on the board and recorded in `tasks/done.md`. Event EVENT-20260613-016.
- Accepted so far: TASK-016, TASK-018. TASK-017 dropped (delivered by EPIC-001).
- TASK-019 (dependency-check logging order) is next per the suggested order and is Ready; TASK-020/021 remain Ready under DISPATCH-20260613-003.
- No new dispatch needed; DISPATCH-20260613-003 covers the remaining tasks.

### Open With Thomas (not yet dispatched)

- EPIC-003 scope, owner, and the parallel-execution model with the current single-implementer team.
