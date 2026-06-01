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

Branch:

vg_e002_voice_gen_hardening

Status:

Planned

Depends On:

EPIC-001

---

EPIC-003 Text_to_Audio Enhancements

Branch:

vg_e003_text_to_audio_enhancements

Status:

Planned

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

vg_e004_progress_reporting

Status:

Planned

Depends On:

v0.3.0 RC validation

---

## Phase 5

EPIC-005 Batch Input Processing

Branch:

vg_e005_batch_input

Status:

Planned

Depends On:

EPIC-004