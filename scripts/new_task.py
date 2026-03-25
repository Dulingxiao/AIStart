from __future__ import annotations

import argparse
from datetime import datetime
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Append a structured task entry to .ai/tasks/current.md"
    )
    parser.add_argument("--root", default=".", help="Project root path")
    parser.add_argument("--title", required=True, help="Task title")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    root = Path(args.root).resolve()
    current_tasks = root / ".ai/tasks/current.md"
    if not current_tasks.exists():
        raise FileNotFoundError(f"Missing task file: {current_tasks}")

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    entry = (
        f"\n## {args.title}\n"
        f"- Status: todo\n"
        f"- Created: {timestamp}\n"
        "- Notes: fill in constraints and verification before implementation.\n"
    )
    with current_tasks.open("a", encoding="utf-8") as handle:
        handle.write(entry)

    print(f"Appended task entry to {current_tasks}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
