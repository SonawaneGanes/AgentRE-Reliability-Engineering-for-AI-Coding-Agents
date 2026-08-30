from agentre.agents.coder import CoderAgent
from agentre.agents.debugger import DebuggerAgent
from agentre.evaluation.reliability_loop import ReliabilityLoop
from agentre.evaluation.runner import CodeRunner
from agentre.llm.ollama import OllamaProvider


def main():
    print("=" * 60)
    print("AgentRE - Reliability Engineering Demo")
    print("=" * 60)

    llm = OllamaProvider(
        model="gemma3:4b",
    )

    coder = CoderAgent(llm=llm)
    debugger = DebuggerAgent(llm=llm)
    runner = CodeRunner(timeout=10)

    loop = ReliabilityLoop(
        coder=coder,
        debugger=debugger,
        runner=runner,
        max_attempts=3,
    )

    task = """
Write a Python program that calculates the average of a list
of numbers.

The program should:
1. Define a function called calculate_average(numbers).
2. Return the average.
3. Handle an empty list safely.
4. Include a small example that calls the function.
"""

    print("\nTask:")
    print(task)

    print("\nRunning AgentRE reliability loop...\n")

    result = loop.run(task)

    print("=" * 60)
    print("FINAL RESULT")
    print("=" * 60)

    print(f"Success : {result.success}")
    print(f"Attempts: {result.attempts}")

    if result.error:
        print(f"Error   : {result.error}")

    print("\nFinal code:")
    print("-" * 60)
    print(result.code)
    print("-" * 60)


if __name__ == "__main__":
    main()
    
