# Reviews

This directory contains structured review artifacts for AgentBus tasks, code changes, documentation updates, and process changes.

Use reviews when work needs formal evaluation before being accepted as done.

Reviews should be append-friendly, factual, and tied to a specific task or artifact.

## Suggested Workflow

1. Development agent completes work and announces it through AgentBus.
2. Reviewer creates a review artifact using `review_template.md`.
3. Findings, risks, and recommendations are recorded in the review.
4. Required fixes are converted into task notes, follow-up tasks, or inbox messages.
5. Once accepted, the related task can move to `tasks/done.md`.

## Review Status Values

- `Pending` - review has not started.
- `In Review` - review is underway.
- `Changes Requested` - work needs revision before acceptance.
- `Accepted with Follow-ups` - acceptable for current scope, with future improvements noted.
- `Accepted` - work meets acceptance criteria.
- `Rejected` - work does not meet the goal or should be replaced.
