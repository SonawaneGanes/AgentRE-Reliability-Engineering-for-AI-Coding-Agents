from agentre.agents.base import AgentResult, BaseAgent


class ExampleAgent(BaseAgent):
    def run(self, task: str) -> AgentResult:
        return AgentResult(
            success=True,
            output=f"Completed: {task}",
        )


def test_agent_result():
    result = AgentResult(
        success=True,
        output="hello",
    )

    assert result.success is True
    assert result.output == "hello"


def test_base_agent():
    agent = ExampleAgent("example")

    result = agent.run("test task")

    assert result.success is True
    assert result.output == "Completed: test task"

    
