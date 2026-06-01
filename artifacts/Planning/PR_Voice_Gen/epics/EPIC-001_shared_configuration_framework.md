# EPIC-001 Shared Configuration Framework

Branch:

vg_e001_shared_config

Priority:

P1

Status:

Planned

Owner:

Thomas / Quill

Development:

Claude CLI + Codex CLI

---

# Objective

Establish a shared configuration and utility foundation for Voice_Gen and Text_to_Audio.

This Epic is the prerequisite for all future roadmap work.

---

# Features

## Feature 1.1 Shared Utility Module

Create:

voice_gen_utils.py

Responsibilities:

* logging helpers
* console formatting
* interactive prompts
* common utility functions

---

## Feature 1.2 Shared Configuration System

Create:

voice_gen.toml

Manage:

* MOSS_ROOT
* LOG_DIR
* VOICES_DIR
* DEFAULT_OUTPUT_DIR
* DEFAULT_INPUT_FILE

---

## Feature 1.3 Configurable Voice Presets

Replace hardcoded voice definitions.

Voice definitions become:

* configuration driven
* automatically discovered

---

## Feature 1.4 Configurable Default Input Path

Remove hardcoded development paths.

Read defaults from configuration.

---

# Acceptance Criteria

* Both applications use shared configuration.
* Both applications use shared utility functions.
* No hardcoded voice presets remain.
* No hardcoded default paths remain.
* Existing workflows continue functioning.