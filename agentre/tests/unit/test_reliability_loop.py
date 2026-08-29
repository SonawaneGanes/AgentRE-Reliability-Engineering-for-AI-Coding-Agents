from unittest.mock import Mock

from agentre.evaluation.reliability_loop import ReliabilityLoop


def test_reliability_loop_repairs_failed_code():
    coder = Mock()
    debugger = Mock()
    runner = Mock()

    coder.run.return_value = Mock(
        success=True,
        output="broken_code",
        error=None,
    )

    runner.run.side_effect = [
    Mock(
        passed=False,
        output=None,
        error="NameError: x is not defined",
    ),
    Mock(
        passed=True,
        output=None,
        error=None,
    ),
]

    debugger.run.return_value = Mock(
        success=True,
        output="fixed_code",
        error=None,
    )

    loop = ReliabilityLoop(
        coder=coder,
        debugger=debugger,
        runner=runner,
        max_attempts=3,
    )

    result = loop.run("Write a working Python program")

    assert result.success is True
    assert result.code == "fixed_code"
    assert result.attempts == 2

    coder.run.assert_called_once()
    debugger.run.assert_called_once()
    assert runner.run.call_count == 2