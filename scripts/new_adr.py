from __future__ import annotations

import argparse
import re
from pathlib import Path


def slugify(value: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")
    return slug or "decision"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Create a new ADR file in .ai/decisions")
    parser.add_argument("--root", default=".", help="Project root path")
    parser.add_argument("--title", required=True, help="ADR title")
    return parser.parse_args()


def next_number(decisions_dir: Path) -> int:
    numbers: list[int] = []
    for path in decisions_dir.glob("*.md"):
        if path.name == "README.md":
            continue
        prefix = path.stem.split("-", 1)[0]
        if prefix.isdigit():
            numbers.append(int(prefix))
    return max(numbers, default=0) + 1


def main() -> int:
    args = parse_args()
    root = Path(args.root).resolve()
    decisions_dir = root / ".ai/decisions"
    if not decisions_dir.exists():
        raise FileNotFoundError(f"Missing decisions directory: {decisions_dir}")

    number = next_number(decisions_dir)
    filename = f"{number:04d}-{slugify(args.title)}.md"
    target = decisions_dir / filename
    target.write_text(
        "\n".join(
            [
                f"# ADR {number:04d}: {args.title}",
                "",
                "- Status: proposed",
                "- Context:",
                "- Decision:",
                "- Consequences:",
                "",
            ]
        ),
        encoding="utf-8",
    )
    print(target)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
