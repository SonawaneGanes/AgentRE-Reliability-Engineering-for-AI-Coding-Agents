from dataclasses import dataclass


@dataclass
class TestResult:
    """Result of executing generated code."""

    passed: bool
    exit_code: int
    stdout: str
    stderr: str
    duration: float
    error: str | None = None
    