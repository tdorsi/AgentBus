# Procedure: Agent Startup

Agents must treat `origin/main` as the source of truth before acting. AgentBus coordination work
must happen from the agent's own AgentBus clone under `D:\Development\Sandbox\AgentBus_<agent>`.
The canonical `D:\Development\AgentBus` checkout is the human-operated reference checkout after
TASK-027 cutover; during TASK-027, the Watcher may remain there until the accepted cutover to
`AgentBus_stan`.

## AgentBus Clone Locations

| Agent | AgentBus clone |
| --- | --- |
| Watcher / Stan | `D:\Development\Sandbox\AgentBus_stan` |
| Codex CLI | `D:\Development\Sandbox\AgentBus_codex` |
| Claude CLI | `D:\Development\Sandbox\AgentBus_claude` |
| Gemini CLI | `D:\Development\Sandbox\AgentBus_gemini` |
| Quill / Thomas | `D:\Development\Sandbox\AgentBus_quill` |

## Startup Sequence

1. Run `git status -sb`.
2. Run `git fetch origin`.
3. If the local branch is clean, run `git pull --rebase origin main` before making or pushing
   AgentBus coordination changes.
4. If local tracked files are modified, do not pull over them. Record the conflict in `tasks/blocked.md` or message Quill for guidance.
5. Read, in order:
   - `agent_rules.md`
   - `roles.md`
   - `sprint.md`
   - `state/agent_status.md`
   - `tasks/active.md`
   - `tasks/blocked.md`
   - your inbox in `comms/`
   - `comms/broadcast.md`
6. Claim or continue only tasks assigned to your role.
7. Append a concise log entry to your own ignored local log.
8. Update `state/agent_status.md` when your visible task state changes, if that file is within
   your write boundary for the task.

## First Startup Self-Validation

After TASK-027, each agent validates its own AgentBus clone on first startup. Do this only from
your assigned clone; do not validate by committing, pushing, or posting messages as another agent.

1. Confirm the clone path matches the table above.
2. Confirm `git remote -v` points to `https://github.com/tdorsi/AgentBus.git`.
3. Run `git fetch origin` and `git pull --rebase origin main`; both should complete cleanly.
4. Make a trivial agent-owned coordination update only when you have a real assigned update to
   record, then commit and push it from your own clone.
5. Confirm you can read your direct inbox, your `comms/watcher_inbox/<agent>.md`, current
   dispatches, and broadcasts from your own clone.

## Project-Repo Work: Session Branch (per task)

The steps above ground you in AgentBus (the shared coordination repo). When you start **code work
in a project repo** (e.g. Voice_Gen), work in **your own working tree/clone** and create **one
branch per task** off the assigned Epic branch, per `procedures/branching_strategy.md`:

1. In your project working tree: `git fetch origin`, check out the Epic branch, `git pull --ff-only`.
2. Review the tree (`git status -sb`, recent log); confirm it is clean and on the correct base.
3. Create your per-task session branch `‹epic-branch›__‹agent›__‹TASK-ID›` (e.g.
   `vg_e002_voice_gen_hardening__codex__TASK-020`) and do all work for that task there.
4. After the task's review is Accepted, merge the session branch up into the Epic branch and prune it.

A reviewer must not commit from a developer's working tree.

## Startup Output

At the end of startup, the agent should know:

- Whether local `main` is synced with `origin/main`.
- Which task, if any, it owns.
- Whether any inbox or broadcast message requires response.
- Whether guidance from Thomas, Quill, or another assigned reviewer is needed.
