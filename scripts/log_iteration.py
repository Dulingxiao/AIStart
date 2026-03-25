from __future__ import annotations

import argparse
import re
from datetime import datetime
from pathlib import Path


def slugify(value: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")
    return slug or "iteration"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Create a dated iteration log")
    parser.add_argument("--root", default=".", help="Project root path")
    parser.add_argument("--title", required=True, help="Iteration title")
    parser.add_argument("--summary", required=True, help="One-line summary")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    root = Path(args.root).resolve()
    iterations_dir = root / ".ai/iterations"
    if not iterations_dir.exists():
        raise FileNotFoundError(f"Missing iterations directory: {iterations_dir}")

    timestamp = datetime.now()
    filename = f"{timestamp.strftime('%Y-%m-%d-%H%M%S')}-{slugify(args.title)}.md"
    target = iterations_dir / filename
    target.write_text(
        "\n".join(
            [
                f"# {args.title}",
                "",
                f"- Timestamp: {timestamp.isoformat(timespec='minutes')}",
                f"- Summary: {args.summary}",
                "- Verification:",
                "- Follow-ups:",
                "",
            ]
        ),
        encoding="utf-8",
    )
    print(target)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
