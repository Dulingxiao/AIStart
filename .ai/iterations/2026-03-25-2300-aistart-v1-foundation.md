# AIStart v1 foundation

- Date: 2026-03-25
- Summary: Built the first reusable AIStart scaffold with canonical context, bridge files, minimal API/web code, governance scripts, and project bootstrap generation.

## What changed

- Added `.ai/` project/context/memory/task scaffolding and root bridge files
- Added a minimal FastAPI app and Next.js starter app
- Added governance scripts for tasks, ADRs, iterations, and drift checks
- Added `init_project.py` to generate named clean copies of the scaffold
- Expanded README and architecture docs so the scaffold can be used without reading implementation details first

## Verification

- `.venv/bin/python -m pytest -q` -> `9 passed`
- `python scripts/init_project.py --name demo-project --output-dir /tmp/...` -> generated scaffold with `.ai/`, bridge files, code scaffold, scripts, and tests
- FastAPI manual check returned `{'status': 'ok', 'project': 'AIStart'}`

## Follow-ups

- Dogfood the generated scaffold on the first real downstream project
- Decide whether to add shared lint / CI presets after real usage feedback
