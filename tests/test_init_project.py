from __future__ import annotations

import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def test_init_project_generates_clean_named_copy(tmp_path: Path) -> None:
    output_dir = tmp_path / "generated"

    subprocess.run(
        [
            sys.executable,
            str(ROOT / "scripts/init_project.py"),
            "--name",
            "demo-project",
            "--output-dir",
            str(output_dir),
        ],
        check=True,
        capture_output=True,
        text=True,
    )

    generated_root = output_dir / "demo-project"
    assert generated_root.exists()
    assert (generated_root / ".ai/project/mission.md").exists()
    assert (generated_root / "AGENTS.md").exists()
    assert (generated_root / "CLAUDE.md").exists()
    assert (generated_root / "codex-prompt.md").exists()

    readme = (generated_root / "README.md").read_text(encoding="utf-8")
    mission = (generated_root / ".ai/project/mission.md").read_text(encoding="utf-8")
    assert "demo-project" in readme
    assert "demo-project" in mission
    assert "AIStart" not in readme

    assert not (generated_root / ".git").exists()
    assert not (generated_root / ".venv").exists()
    assert not (generated_root / ".pytest_cache").exists()
    assert not (generated_root / "node_modules").exists()
    assert not (generated_root / "__pycache__").exists()
