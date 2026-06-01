# Procedures

Procedures define how agents interact with AgentBus.

AgentBus is no longer only a set of markdown files. It is a Git-backed coordination system. That means agents must follow consistent operating steps when checking for updates, claiming work, responding to reviews, and reporting status.

## Source of Truth

`origin/main` is the source of truth for shared AgentBus state.

Before reading tasks, messages, reviews, or decisions, agents must synchronize with `origin/main` unless they are intentionally working offline.

## Core Procedures

- `agent_startup.md` - steps to follow when beginning an AgentBus session.
- `check_for_updates.md` - required behavior when asked to check for updates.
- `task_claiming.md` - how to claim and update tasks.
- `review_response.md` - how to respond to reviews and requested changes.

## Review Workflow

`tasks/review.md` is the review queue. Formal review artifacts live in `reviews/` and should use `reviews/review_template.md`.

Review artifacts that affect task acceptance, follow-up planning, or governance history should be committed and pushed to `origin/main`. Agents must synchronize before concluding that a review artifact, review directory, or procedure file is missing.

## Failure Rule

If an agent cannot safely synchronize, it must stop and report the condition instead of guessing from stale local files.
