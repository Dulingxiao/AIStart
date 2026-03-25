from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BRIDGE_FILES = ["AGENTS.md", "CLAUDE.md", "codex-prompt.md"]
REQUIRED_ANCHORS = [
    ".ai/project/mission.md",
    ".ai/project/scope.md",
    ".ai/project/non-goals.md",
    ".ai/context/technical-constraints.md",
    ".ai/memory/stable-facts.md",
    ".ai/memory/anti-drift.md",
    ".ai/tasks/current.md",
]


def test_bridge_files_reference_canonical_context() -> None:
    for name in BRIDGE_FILES:
        path = ROOT / name
        assert path.exists(), f"Missing bridge file: {name}"
        text = path.read_text(encoding="utf-8")
        for anchor in REQUIRED_ANCHORS:
            assert anchor in text, f"{name} missing canonical anchor: {anchor}"
