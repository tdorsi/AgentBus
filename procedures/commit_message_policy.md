
### Standard Commit Format
# AgentBus rule:

---
All commits must contain:
[Release][Epic/Branch][Task]

All squash merges must contain:
[Release][Epic]

All release merges must contain:
[Release][RELEASE]
---

That gives you traceability from **release → epic → task → commit** with nothing more than Git history. 

---
[v0.3.0][vg_e001][TASK-011] Create shared utility module
---

Examples:

---
[v0.3.0][vg_e001][TASK-011] Create voice_gen_utils module

[v0.3.0][vg_e001][TASK-012] Implement shared TOML configuration

[v0.3.0][vg_e001][TASK-013] Replace hardcoded voice presets

[v0.3.0][vg_e001][TASK-014] Remove hardcoded default paths
---

---

For branch-specific work:

---
[v0.3.0][vg_e002][TASK-015] Add overwrite protection

[v0.3.0][vg_e002][TASK-016] Improve logging and interrupt handling

[v0.3.0][vg_e003][TASK-018] Add chunk preservation option
---

---

## Squash Merge Standard

When an Epic branch is merged back into the integration branch:

### Format

---
[v0.3.0][vg_e001] Merge EPIC-001 Shared Configuration Framework
---

### Body

---
Release:
v0.3.0

Epic:
EPIC-001 Shared Configuration Framework

Merged Branch:
vg_e001_shared_config

Tasks:
- TASK-011 Shared Utility Module
- TASK-012 Shared Configuration System
- TASK-013 Configurable Voice Presets
- TASK-014 Configurable Default Input Path

Summary:
Implemented shared configuration architecture used by both
voice_gen.py and text_to_audio.py.

Result:
- Shared utility module
- Shared TOML configuration
- Voice preset discovery
- Configurable paths

Approved By:
Thomas
---

---

## Release Merge Standard

When the release candidate is finalized:

---
[v0.3.0][RELEASE] Voice_Gen v0.3.0
---

Body:

---
Release:
v0.3.0

Included Epics:
- EPIC-001 Shared Configuration Framework
- EPIC-002 Voice_Gen Hardening
- EPIC-003 Text_to_Audio Enhancements

Included Tasks:
- TASK-011
- TASK-012
- TASK-013
- TASK-014
- TASK-015
- TASK-016
- TASK-017
- TASK-018
- TASK-019

Approved By:
Thomas

Release Date:
YYYY-MM-DD
---