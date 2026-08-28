"""Shared workflow state."""

from dataclasses import dataclass, field

@dataclass
class AgentState:
    task: str = ""
    artifacts: dict = field(default_factory=dict)
    failures: list = field(default_factory=list)
    results: dict = field(default_factory=dict)
