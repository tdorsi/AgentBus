# REVIEW-028

Reviewer: Claude CLI
Date: 2026-06-21
Related Task: TASK-031 (Cut Voice_Gen v0.3.0 Release — release branch + annotated tag + advance `main`, from accepted RC `5ed908f`)
Artifact: Release topology on origin (DISPATCH-20260621-003, Codex CLI): branch `voice-gen_0.3.0`, tag `v0.3.0`, `main` merge `ab6dd2a`. Verified from `D:\Development\Sandbox\Voice_Gen_claude` after `git fetch --tags --prune`.
Status: Accepted

## Summary

TASK-031 cuts the v0.3.0 release from the accepted RC `5ed908f` (the Phase 3 assembly of EPIC-001 + EPIC-003 + EPIC-002). I verified the full release topology — release branch, annotated tag, and the merge advancing `main` — and confirmed all three point at trees byte-identical to the accepted RC, that no unmerged work was lost in the authorized branch pruning, and that the release compiles on the `main` tip. No feature code was modified. Accepted.

## Verification (from my `Voice_Gen_claude` worktree, after `fetch --tags --prune`)

**1. Release branch** ✓ — `origin/voice-gen_0.3.0` → `5ed908f` (the accepted RC).

**2. Annotated tag** ✓ — `v0.3.0` is a real annotated tag object (type `tag`, tagger `tdorsi`, message `Voice_Gen v0.3.0`) and peels to commit `5ed908f`.

**3. Production branch** ✓ — `origin/main` → `ab6dd2a` `[v0.3.0][RELEASE] Merge voice-gen_0.3.0 into main`, a `--no-ff` merge with parents `2eb1d32` (prior main, v0.1.0) + `5ed908f` (the release commit).

**4. Trees match the accepted RC** ✓ — all three diffs empty:
- `git diff 5ed908f origin/main` — empty (production tree == RC).
- `git diff 5ed908f origin/voice-gen_0.3.0` — empty (release branch == RC).
- `git diff v0.3.0 5ed908f` — empty (tagged tree == RC).
The released code is exactly the RC I accepted in REVIEW-027.

**5. No unmerged work lost in pruning** ✓ — the RC and every accepted epic/session tip are ancestors of `origin/main`: `5ed908f`, `ffc7b5e` (EPIC-003 RC), `793a80b` (EPIC-003 stack), `6529caa` (EPIC-002 TASK-021), `19372bb` (EPIC-002 TASK-020), `a83550f` (EPIC-001 base) — all reachable from `main`. The pruned `vg_e002_*` / `vg_e003_*` / per-agent session branches were therefore fully merged; nothing was discarded.

**6. Prior releases retained** ✓ — `origin/voice-gen_0.2.0` branch and the `v0.1.0` tag are intact. Retained remote heads: `main`, `vg_e001_shared_config`, `voice-gen_0.2.0`, `voice-gen_0.3.0`.

**7. Compile on the release** ✓ — `python -m py_compile voice_gen.py voice_gen_utils.py voice_gen_config.py text_to_audio.py` clean at the `origin/main` tip (moss-tts env).

## Observations (non-blocking)

1. `vg_e001_shared_config` remains on origin pointing at `5ed908f` (identical to the release). Harmless; it can be pruned at the team's discretion now that the release branch carries the same commit.
2. There is no `v0.2.0` tag (only a `voice-gen_0.2.0` branch) — pre-existing repo state, outside TASK-031's scope; noted only for completeness.
3. The two recorded environment follow-ups for Thomas remain open and non-blocking for the release (per the 2026-06-21 PO decision, EVENT-20260621-004): onnxruntime BFC Arena OOM on very long single runs; model-warmup-inflated initial ETA.

## Acceptance Recommendation

**Accepted.** The v0.3.0 release is cut correctly: `voice-gen_0.3.0` and annotated tag `v0.3.0` both at the accepted RC `5ed908f`, `main` advanced via a clean release merge to the same tree, no unmerged work lost in pruning, prior releases retained, and the release compiles. **Voice_Gen v0.3.0 is released.** EPIC-001/002/003 are complete, runtime-validated, integrated, and shipped; my review queue is empty.
