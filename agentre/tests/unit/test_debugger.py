from unittest.mock import Mock

from agentre.agents.debugger import DebuggerAgent


def test_debugger_agent_fixes_code():
    mock_llm = Mock()

    mock_llm.generate.return_value = (
        "def divide(a, b):\n"
        "    return a / b"
    )

    agent = DebuggerAgent(llm=mock_llm) # type: ignore

    broken_code = (
        "def divide(a, b):\n"
        "    return a // b"
    )

    error = "Expected 2.5 but received 2"

    result = agent.run( # type: ignore
        broken_code,
        error,
    )

    assert result.success is True
    assert "return a / b" in result.output

    mock_llm.generate.assert_called_once()
