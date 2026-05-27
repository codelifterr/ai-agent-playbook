from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class AgentPattern:
    name: str
    purpose: str
    steps: tuple[str, ...]


PATTERNS = {
    "research": AgentPattern(
        name="research",
        purpose="Collect sources and produce a concise brief.",
        steps=("clarify question", "collect sources", "compare evidence", "summarize with confidence"),
    ),
    "evaluation": AgentPattern(
        name="evaluation",
        purpose="Score an output against a rubric.",
        steps=("load rubric", "inspect output", "list issues", "suggest correction"),
    ),
    "automation": AgentPattern(
        name="automation",
        purpose="Automate repetitive work with verification.",
        steps=("map process", "identify tools", "run dry-run", "verify result"),
    ),
}


def get_pattern(name: str) -> AgentPattern:
    key = name.lower().strip()
    if key not in PATTERNS:
        raise ValueError(f"Unknown pattern: {name}. Available: {', '.join(PATTERNS)}")
    return PATTERNS[key]
