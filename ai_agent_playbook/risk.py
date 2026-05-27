from __future__ import annotations

from enum import Enum


class RiskLevel(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"


def risk_gate(level: RiskLevel, action: str) -> str:
    """Return the required control for an agent action."""
    if level == RiskLevel.HIGH:
        return f"Human approval required before: {action}"
    if level == RiskLevel.MEDIUM:
        return f"Dry-run and verify before: {action}"
    return f"Safe to run with logging: {action}"
