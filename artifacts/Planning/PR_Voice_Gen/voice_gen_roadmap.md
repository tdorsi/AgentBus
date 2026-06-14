# Voice_Gen Roadmap

Project: Voice_Gen

Current Baseline:
voice-gen_0.2.0

Target Release:
v0.3.0

---

# Vision

Create a maintainable and extensible voice generation platform that supports:

* Voice creation
* Voice inference
* Shared configuration
* Multiple voice personas
* Consistent operational behavior
* Future batch processing

---

# Roadmap Overview

## Phase 1

EPIC-001 Shared Configuration Framework

Purpose:

Create the shared foundation required by all future enhancements.

Branch:

vg_e001_shared_config

Status:

Planned

Dependencies:

None

---

## Phase 2

EPIC-002 Voice_Gen Hardening

Owner: Codex CLI (reviewer Claude CLI)

Branch:

vg_e002_voice_gen_hardening

Status:

In progress (TASK-016, TASK-018 accepted; TASK-019/020/021 pending; TASK-017 dropped)

Depends On:

EPIC-001

---

EPIC-003 Text_to_Audio Enhancements

Owner: Gemini CLI (reviewer Claude CLI)

Branch:

vg_e003_text_to_audio_enhancements

Status:

Activated 2026-06-13 — combined scope. Per Thomas, EPIC-004 Progress Reporting is folded into EPIC-003 (per-chunk WAV preservation + progress/ETA reporting). EPIC-005 remains deferred.

Depends On:

EPIC-001

---

## Phase 3

Integration and Release Candidate Validation

Merge:

* EPIC-002
* EPIC-003

Into:

vg_e001_shared_config

Target:

Voice_Gen v0.3.0 RC

---

## Phase 4

EPIC-004 Progress Reporting

Branch:

(none — folded into EPIC-003)

Status:

Folded into EPIC-003 (Thomas, 2026-06-13). Progress/ETA reporting now ships within EPIC-003 on `vg_e003_text_to_audio_enhancements` as part of v0.3.0. This standalone phase is retired.

Depends On:

EPIC-001 (via EPIC-003)

---

## Phase 5

EPIC-005 Batch Input Processing

Branch:

vg_e005_batch_input

Status:

Deferred — not in v0.3.0 scope (Thomas, 2026-06-13). Planned for a later release.

Depends On:

EPIC-003 (was EPIC-004, which is now folded into EPIC-003)