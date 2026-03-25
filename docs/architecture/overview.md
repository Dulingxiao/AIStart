# AIStart Architecture Overview

AIStart V1 has four layers:
- `.ai/` for canonical project truth
- root bridge files for AI tool entrypoints
- `apps/` and `packages/` for minimal code scaffolding
- `scripts/` for bootstrap and governance helpers

## Layer responsibilities

### 1. Canonical context

`.ai/project`, `.ai/context`, `.ai/memory`, `.ai/tasks`, `.ai/decisions`, and `.ai/iterations`
hold the durable project rules and current working state.

### 2. Tool bridge layer

`AGENTS.md`, `CLAUDE.md`, and `codex-prompt.md` only tell tools how to read the project.
They must never evolve into a second source of truth.

### 3. Minimal code scaffold

`apps/api` and `apps/web` prove the scaffold can host a fullstack project from day one.
`packages/shared-types` is the smallest shared boundary between backend and frontend.

### 4. Governance and bootstrap

`scripts/new_task.py`, `scripts/new_adr.py`, `scripts/log_iteration.py`, `scripts/drift_check.py`,
and `scripts/init_project.py` keep the repository usable as a repeatable starter rather than a one-off demo.

## Initialization flow

1. Use `scripts/init_project.py` to generate a clean named copy
2. Read the bridge files, which point back to `.ai/`
3. Update mission, scope, and current task for the new project
4. Start implementation inside `apps/` without breaking the canonical context contract

The repository intentionally stays light. It should explain the rules of the project before it tries to automate everything.
