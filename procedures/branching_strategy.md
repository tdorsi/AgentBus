# AgentBus Branching Strategy

## Purpose

This document defines the branching model used for Voice_Gen and future AgentBus-managed development projects.

The goal is to support parallel work by multiple agents while preserving a stable integration path and clear ownership boundaries.

---

# Core Principles

## 1. Branches Follow Epics

Branches are created from approved roadmap Epics rather than individual tasks.

Tasks are implementation units.

Branches are integration units.

This reduces branch sprawl and allows related work to be tested together.

---

## 2. One Integration Branch Per Release

Each planned release receives a dedicated integration branch.

Example:

```text
voice-gen_0.2.0
    ↓
vg_e001_shared_config
```

The integration branch becomes the target for all Epic work associated with that release.

---

## 3. Epic Dependencies Define Branch Hierarchy

Epic branches must follow dependency order.

Do not create child branches from the production branch if they depend on another Epic.

Example:

```text
voice-gen_0.2.0
    ↓
vg_e001_shared_config
    ↓
    ├── vg_e002_voice_gen_hardening
    └── vg_e003_text_to_audio_enhancements
```

Both Epic 2 and Epic 3 depend on Epic 1 and therefore branch from Epic 1.

---

# Voice_Gen v0.3.0 Roadmap

## Phase 1

### EPIC-001 Shared Configuration Framework

Branch:

```text
vg_e001_shared_config
```

Includes:

* Shared utility module
* Shared configuration file
* Configurable voice presets
* Configurable default input path

Completion of EPIC-001 establishes the foundation for all subsequent work.

---

## Phase 2

### EPIC-002 Voice_Gen Hardening

Branch:

```text
vg_e002_voice_gen_hardening
```

Parent:

```text
vg_e001_shared_config
```

Includes:

* Overwrite protection
* Logging improvements
* KeyboardInterrupt handling
* Dependency logging fixes
* Dry-run mode

---

### EPIC-003 Text_to_Audio Enhancements

Branch:

```text
vg_e003_text_to_audio_enhancements
```

Parent:

```text
vg_e001_shared_config
```

Includes:

* Per-chunk WAV preservation
* Default output directory improvements

---

## Phase 3

After EPIC-002 and EPIC-003 are complete:

```text
vg_e002_voice_gen_hardening
    ↓
merge

vg_e003_text_to_audio_enhancements
    ↓
merge

vg_e001_shared_config
```

Integration testing is then performed against:

```text
vg_e001_shared_config
```

This branch becomes the v0.3.0 release candidate.

---

## Phase 4

### EPIC-004 Progress Reporting

Branch:

```text
vg_e004_progress_reporting
```

Parent:

```text
vg_e001_shared_config
```

Includes:

* Progress tracking
* Status reporting
* ETA calculations

---

## Phase 5

### EPIC-005 Batch Input Processing

Branch:

```text
vg_e005_batch_input
```

Parent:

```text
vg_e001_shared_config
```

Includes:

* Batch text processing
* Multi-file execution
* Batch workflow management

---

# Agent Responsibilities

## Product Owner (Thomas)

* Approves roadmap
* Approves Epic completion
* Approves release readiness

## Senior Analyst / PM (Quill)

* Maintains roadmap
* Validates Epic dependencies
* Reviews integration readiness
* Coordinates acceptance criteria

## Development Team (Claude CLI, Codex CLI)

* Implement Epic work
* Maintain branch hygiene
* Submit work for review
* Resolve merge conflicts within assigned Epic scope

---

# Merge Rules

## Required Before Merge

* Acceptance criteria satisfied
* Tests completed
* Review completed
* Changes committed and pushed
* No unresolved blockers

## Merge Direction

Feature work always merges upward.

Example:

```text
vg_e002_voice_gen_hardening
    ↓
vg_e001_shared_config
```

Do not merge integration branches into feature branches.

---

# Source of Truth

The Git repository is the authoritative source of code state.

AgentBus remains the authoritative source for:

* Tasks
* Reviews
* Decisions
* Procedures
* Project governance

Both systems must remain synchronized through commits, reviews, and documented decisions.