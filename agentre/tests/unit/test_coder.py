from unittest.mock import Mock

from agentre.agents.coder import CoderAgent


def test_coder_agent_generates_code():
    mock_llm = Mock()

    mock_llm.generate.return_value = (
        "def add(a, b):\n"
        "    return a + b"
    )

    agent = CoderAgent(llm=mock_llm)

    result = agent.run(
        "Create a function called add that adds two numbers."
    )

    assert result.success is True
    assert "def add" in result.output

     

    
