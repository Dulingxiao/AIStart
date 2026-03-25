from __future__ import annotations

import shutil
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def prepare_scaffold_copy(tmp_path: Path) -> Path:
    target = tmp_path / "project-copy"
    target.mkdir()
    shutil.copytree(ROOT / ".ai", target / ".ai")
    return target


def run_script(*args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, *args],
        check=True,
        capture_output=True,
        text=True,
    )


def test_new_task_appends_structured_entry(tmp_path: Path) -> None:
    project_root = prepare_scaffold_copy(tmp_path)
    current_tasks = project_root / ".ai/tasks/current.md"
    before = current_tasks.read_text(encoding="utf-8")

    run_script(
        str(ROOT / "scripts/new_task.py"),
        "--root",
        str(project_root),
        "--title",
        "Wire up health checks",
    )

    after = current_tasks.read_text(encoding="utf-8")
    assert "Wire up health checks" in after
    assert "Status: todo" in after
    assert len(after) > len(before)


def test_new_adr_creates_numbered_file(tmp_path: Path) -> None:
    project_root = prepare_scaffold_copy(tmp_path)

    run_script(
        str(ROOT / "scripts/new_adr.py"),
        "--root",
        str(project_root),
        "--title",
        "Use bridge files as thin adapters",
    )

    adr_files = sorted((project_root / ".ai/decisions").glob("*.md"))
    created = [path for path in adr_files if path.name != "README.md"]
    assert len(created) == 1
    assert created[0].name.startswith("0001-")
    assert "Use bridge files as thin adapters" in created[0].read_text(encoding="utf-8")


def test_log_iteration_creates_dated_markdown_file(tmp_path: Path) -> None:
    project_root = prepare_scaffold_copy(tmp_path)
    before = {
        path.name
        for path in (project_root / ".ai/iterations").glob("*.md")
        if path.name != "README.md"
    }

    run_script(
        str(ROOT / "scripts/log_iteration.py"),
        "--root",
        str(project_root),
        "--title",
        "Bootstrap scaffold foundation",
        "--summary",
        "Created the first reusable AIStart repository skeleton.",
    )

    iteration_files = sorted((project_root / ".ai/iterations").glob("*.md"))
    created = [
        path
        for path in iteration_files
        if path.name != "README.md" and path.name not in before
    ]
    assert len(created) == 1
    assert "Bootstrap scaffold foundation" in created[0].read_text(encoding="utf-8")


def test_drift_check_prints_core_alignment_checklist(tmp_path: Path) -> None:
    project_root = prepare_scaffold_copy(tmp_path)

    result = run_script(
        str(ROOT / "scripts/drift_check.py"),
        "--root",
        str(project_root),
    )

    assert "mission.md" in result.stdout
    assert "scope.md" in result.stdout
    assert "non-goals.md" in result.stdout
