from __future__ import annotations

import argparse
from pathlib import Path


REQUIRED_FILES = [
    ".ai/project/mission.md",
    ".ai/project/scope.md",
    ".ai/project/non-goals.md",
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Print a lightweight anti-drift checklist")
    parser.add_argument("--root", default=".", help="Project root path")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    root = Path(args.root).resolve()
    resolved = [root / relative for relative in REQUIRED_FILES]
    missing = [str(path) for path in resolved if not path.exists()]
    if missing:
        raise FileNotFoundError(f"Missing drift-check inputs: {missing}")

    lines = [
        "AIStart drift check",
        "- Review mission.md before widening scope.",
        "- Review scope.md before adding new subsystems.",
        "- Review non-goals.md before sneaking in V2 ideas.",
        "- Confirm bridge files still point back to canonical context.",
        "- Confirm current task and iteration logs reflect the latest work.",
    ]
    print("\n".join(lines))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
