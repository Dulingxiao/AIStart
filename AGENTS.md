# AGENTS

This repository uses `.ai/` as the canonical context source for all coding agents.

## Canonical read order

Always read these files in order before making meaningful changes:
1. `.ai/project/mission.md`
2. `.ai/project/scope.md`
3. `.ai/project/non-goals.md`
4. `.ai/context/technical-constraints.md`
5. `.ai/memory/stable-facts.md`
6. `.ai/memory/anti-drift.md`
7. `.ai/tasks/current.md`

## Working discipline

- `.ai/` is the only canonical source of project truth.
- Root bridge files summarize access rules only; they must not duplicate full project context.
- After meaningful work, update `.ai/tasks/current.md` and add or refresh an iteration record under `.ai/iterations/`.
- When architecture or process contracts change, add or update an ADR under `.ai/decisions/`.
