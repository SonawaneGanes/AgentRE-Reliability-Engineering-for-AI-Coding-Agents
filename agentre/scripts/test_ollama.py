from agentre.llm.ollama import OllamaProvider


def main():
    provider = OllamaProvider(
        model="gemma3:4b",
    )

    prompt = """
You are AgentRE.

Explain in 3 sentences why testing AI-generated code
is important.
"""

    print("\nAgentRE → Ollama\n")
    print(provider.generate(prompt))


if __name__ == "__main__":
    main()


    