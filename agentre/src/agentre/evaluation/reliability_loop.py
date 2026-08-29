from dataclasses import dataclass

from agentre.agents.coder import CoderAgent
from agentre.agents.debugger import DebuggerAgent
from agentre.evaluation.runner import CodeRunner


@dataclass
class ReliabilityResult:
    success: bool
    code: str
    attempts: int
    error: str | None = None


class ReliabilityLoop:
    """Generate, execute, debug, and re-test AI-generated code."""

    def __init__(
        self,
        coder: CoderAgent,
        debugger: DebuggerAgent,
        runner: CodeRunner,
        max_attempts: int = 3,
    ):
        self.coder = coder
        self.debugger = debugger
        self.runner = runner
        self.max_attempts = max_attempts

    def run(self, task: str) -> ReliabilityResult:
        """Run the generate → test → repair → retest loop."""

        code_result = self.coder.run(task)

        if not code_result.success:
            return ReliabilityResult(
                success=False,
                code="",
                attempts=0,
                error=code_result.error,
            )

        code = code_result.output
        last_error = None

        for attempt in range(1, self.max_attempts + 1):
            result = self.runner.run(code)

            if result.passed:
                return ReliabilityResult(
                    success=True,
                    code=code,
                    attempts=attempt,
                )

            last_error = result.error

            if attempt == self.max_attempts:
                break

            debug_result = self.debugger.run(
                code=code,
                error=result.error or "Unknown execution error",
            )

            if not debug_result.success:
                return ReliabilityResult(
                    success=False,
                    code=code,
                    attempts=attempt,
                    error=debug_result.error,
                )

            code = debug_result.output

        return ReliabilityResult(
            success=False,
            code=code,
            attempts=self.max_attempts,
            error=last_error,
        )