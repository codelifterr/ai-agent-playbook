from __future__ import annotations

import argparse

from .patterns import get_pattern
from .risk import RiskLevel, risk_gate


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate a small AI-agent workflow plan.")
    parser.add_argument("goal")
    parser.add_argument("--pattern", default="research", choices=["research", "evaluation", "automation"])
    parser.add_argument("--risk", default="low", choices=[level.value for level in RiskLevel])
    args = parser.parse_args()

    pattern = get_pattern(args.pattern)
    print(f"Goal: {args.goal}")
    print(f"Pattern: {pattern.name} - {pattern.purpose}")
    for index, step in enumerate(pattern.steps, start=1):
        print(f"{index}. {step}")
    print(risk_gate(RiskLevel(args.risk), args.goal))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
