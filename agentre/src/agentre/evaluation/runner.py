import subprocess
import sys
import tempfile
import time
from pathlib import Path

from agentre.evaluation.result import TestResult


class CodeRunner:
    """Safely execute generated Python code with a timeout."""

    def __init__(self, timeout: int = 10):
        self.timeout = timeout

    def run(self, code: str) -> TestResult:
        """Execute Python code and capture its result."""

        start_time = time.perf_counter()

        with tempfile.TemporaryDirectory() as temp_dir:
            file_path = Path(temp_dir) / "generated_code.py"
            file_path.write_text(code, encoding="utf-8")

            try:
                process = subprocess.run(
                    [
                        sys.executable,
                        str(file_path),
                    ],
                    capture_output=True,
                    text=True,
                    timeout=self.timeout,
                )

                duration = time.perf_counter() - start_time

                return TestResult(
                    passed=process.returncode == 0,
                    exit_code=process.returncode,
                    stdout=process.stdout,
                    stderr=process.stderr,
                    duration=duration,
                )

            except subprocess.TimeoutExpired as exc:
                duration = time.perf_counter() - start_time

                return TestResult(
                    passed=False,
                    exit_code=-1,
                    stdout=exc.stdout or "", # type: ignore
                    stderr=exc.stderr or "", # type: ignore
                    duration=duration,
                    error="Execution timed out",
                )

            except Exception as exc:
                duration = time.perf_counter() - start_time

                return TestResult(
                    passed=False,
                    exit_code=-1,
                    stdout="",
                    stderr="",
                    duration=duration,
                    error=str(exc),
                )
            