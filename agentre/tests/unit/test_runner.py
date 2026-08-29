from agentre.evaluation.runner import CodeRunner


def test_successful_code():
    runner = CodeRunner()

    result = runner.run(
        """
print("hello")
"""
    )

    assert result.passed is True
    assert result.exit_code == 0
    assert "hello" in result.stdout


def test_failed_code():
    runner = CodeRunner()

    result = runner.run(
        """
raise ValueError("intentional failure")
"""
    )

    assert result.passed is False
    assert result.exit_code != 0
    assert "ValueError" in result.stderr


def test_timeout():
    runner = CodeRunner(timeout=1)

    result = runner.run(
        """
import time
time.sleep(5)
"""
    )

    assert result.passed is False
    assert result.error == "Execution timed out"