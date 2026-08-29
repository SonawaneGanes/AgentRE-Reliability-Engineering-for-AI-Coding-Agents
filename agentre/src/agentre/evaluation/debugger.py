from agentre.agents.base import AgentResult, BaseAgent
from agentre.llm.ollama import OllamaProvider


class DebuggerAgent(BaseAgent):
    """Agent responsible for analyzing and fixing failed code."""

    def __init__(self, llm: OllamaProvider | None = None):
        super().__init__("debugger")
        self.llm = llm or OllamaProvider()

    def run(self, code: str, error: str) -> AgentResult:
        """Analyze a failure and generate corrected code."""

        prompt = f"""
You are a senior Python debugging engineer.

The following Python code failed during execution.

--- CODE ---
{code}
--- END CODE ---

--- ERROR ---
{error}
--- END ERROR ---

Your task:
1. Identify the root cause of the failure.
2. Fix the code.
3. Return ONLY the complete corrected Python code.
4. Do not use Markdown code fences.
5. Do not provide explanations.
"""

        try:
            fixed_code = self.llm.generate(prompt)

            return AgentResult(
                success=True,
                output=fixed_code.strip(),
            )

        except Exception as exc:
            return AgentResult(
                success=False,
                error=str(exc),
            )