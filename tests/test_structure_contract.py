from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

REQUIRED_PATHS = [
    ROOT / ".ai/project/mission.md",
    ROOT / ".ai/project/scope.md",
    ROOT / ".ai/project/non-goals.md",
    ROOT / ".ai/project/success-criteria.md",
    ROOT / ".ai/project/current-phase.md",
    ROOT / ".ai/context/technical-constraints.md",
    ROOT / ".ai/memory/stable-facts.md",
    ROOT / ".ai/memory/anti-drift.md",
    ROOT / ".ai/tasks/current.md",
    ROOT / "README.md",
    ROOT / "pyproject.toml",
]

WEB_AND_SHARED_PATHS = [
    ROOT / "apps/web/package.json",
    ROOT / "apps/web/tsconfig.json",
    ROOT / "apps/web/next.config.ts",
    ROOT / "apps/web/next-env.d.ts",
    ROOT / "apps/web/app/layout.tsx",
    ROOT / "apps/web/app/page.tsx",
    ROOT / "apps/web/app/api/health/route.ts",
    ROOT / "apps/web/app/globals.css",
    ROOT / "packages/shared-types/package.json",
    ROOT / "packages/shared-types/tsconfig.json",
    ROOT / "packages/shared-types/src/index.ts",
    ROOT / "packages/config/README.md",
    ROOT / "infra/README.md",
    ROOT / "docs/architecture/overview.md",
]


def test_required_scaffold_files_exist() -> None:
    missing = [str(path) for path in REQUIRED_PATHS if not path.exists()]
    assert not missing, f"Missing scaffold paths: {missing}"


def test_web_and_shared_scaffold_files_exist() -> None:
    missing = [str(path) for path in WEB_AND_SHARED_PATHS if not path.exists()]
    assert not missing, f"Missing web/shared scaffold paths: {missing}"
