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


def test_required_scaffold_files_exist() -> None:
    missing = [str(path) for path in REQUIRED_PATHS if not path.exists()]
    assert not missing, f"Missing scaffold paths: {missing}"
