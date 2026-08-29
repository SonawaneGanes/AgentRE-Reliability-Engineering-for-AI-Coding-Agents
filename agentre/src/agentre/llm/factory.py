import os

from .ollama import OllamaProvider


def get_provider():
    """Create the configured LLM provider."""

    provider = os.getenv("LLM_PROVIDER", "ollama").lower()

    if provider == "ollama":
        return OllamaProvider()

    raise ValueError(
        f"Unsupported LLM provider: {provider}"
    )