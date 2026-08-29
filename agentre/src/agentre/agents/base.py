from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any


@dataclass
class AgentResult:
    """Result returned by an agent."""

    success: bool
    output: Any = None
    error: str | None = None


class BaseAgent(ABC):
    """Base interface for all AgentRE agents."""

    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def run(self, *args: Any, **kwargs: Any) -> AgentResult:
        """Execute the agent."""
        raise NotImplementedError