from __future__ import annotations

import argparse
import shutil
from pathlib import Path


TRANSIENT_NAMES = {
    ".git",
    ".venv",
    ".pytest_cache",
    ".next",
    "node_modules",
    "__pycache__",
    "dist",
    "build",
}

TEXT_SUFFIXES = {
    ".lock",
    ".md",
    ".toml",
    ".py",
    ".json",
    ".ts",
    ".tsx",
    ".css",
    ".txt",
    ".yaml",
    ".yml",
}

TEXT_FILENAMES = {
    ".gitignore",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate a new project from the AIStart scaffold")
    parser.add_argument("--name", required=True, help="Generated project name")
    parser.add_argument("--output-dir", required=True, help="Parent directory for the generated project")
    return parser.parse_args()


def ignore_transient(_directory: str, names: list[str]) -> set[str]:
    return {name for name in names if name in TRANSIENT_NAMES}


def should_rewrite(path: Path) -> bool:
    return path.suffix in TEXT_SUFFIXES or path.name in TEXT_FILENAMES


def rewrite_placeholders(target_root: Path, project_name: str) -> None:
    replacements = {
        "AIStart": project_name,
        "aistart": project_name.lower(),
    }
    for path in target_root.rglob("*"):
        if not path.is_file() or not should_rewrite(path):
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        for source, replacement in replacements.items():
            text = text.replace(source, replacement)
        path.write_text(text, encoding="utf-8")


def main() -> int:
    args = parse_args()
    source_root = Path(__file__).resolve().parents[1]
    output_dir = Path(args.output_dir).resolve()
    target_root = output_dir / args.name

    if target_root.exists():
        raise FileExistsError(f"Target project already exists: {target_root}")

    output_dir.mkdir(parents=True, exist_ok=True)
    shutil.copytree(source_root, target_root, ignore=ignore_transient)
    rewrite_placeholders(target_root, args.name)

    print(target_root)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
