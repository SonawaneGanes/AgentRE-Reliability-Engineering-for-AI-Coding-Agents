from agentre.agents.base import AgentResult, BaseAgent
from agentre.llm.ollama import OllamaProvider


class CoderAgent(BaseAgent):
    """Agent responsible for generating Python code."""

    def __init__(self, llm: OllamaProvider | None = None):
        super().__init__("coder")
        self.llm = llm or OllamaProvider()

    def run(self, task: str) -> AgentResult:
        prompt = f"""
You are a professional Python software engineer.

Generate a solution for the following programming task:

{task}

Requirements:
- Return only Python code.
- Do not use Markdown code fences.
- Write clean and readable code.
- Include necessary functions.
- Do not include explanations.
"""

        try:
            code = self.llm.generate(prompt).strip()

            if code.startswith("```"):
                lines = code.splitlines()

                if lines and lines[0].startswith("```"):
                    lines = lines[1:]

                if lines and lines[-1].strip() == "```":
                    lines = lines[:-1]

                code = "\n".join(lines).strip()

            return AgentResult(
                success=True,
                output=code.strip(),
            )

        except Exception as exc:
            return AgentResult(
                success=False,
                error=str(exc),
            )
        