# AgentBus Git Notes

AgentBus can be placed under Git version control to support history, rollback, and coordination with remote or cloud-based agents.

## Recommended approach

Start with a private repository.

Track:
- README.md
- sprint.md
- agent_rules.md
- task templates
- communication templates
- decision logs
- non-sensitive coordination files

Be cautious with:
- agent logs
- generated artifacts
- handoff notes
- runtime output
- copied code snippets
- local file paths
- API keys or credentials

## Why logs are ignored by default

Agent logs may accidentally contain sensitive information, secrets, private reasoning traces, local machine paths, or large noisy output. The default setup tracks the log template but ignores live working logs.

## Suggested initialization commands

Run manually only after reviewing the workspace:

```bash
cd /d D:\Development\AgentBus
git init
git status
git add .
git commit -m "Initialize AgentBus coordination workspace"
```

## Suggested remote setup

Use a private GitHub repository first.

Do not push:
- `.env` files
- credentials
- tokens
- runtime folders
- cache folders
- scratch folders
- generated artifacts unless reviewed

## Agent rule

Before any agent commits or pushes changes, it should:

- Run `git status`.
- Review changed files.
- Confirm no secrets or sensitive content are included.
- Write a brief summary of the intended commit.
- Ask for human approval before pushing to a remote.
