"""LLM provider factory."""

import os
from .ollama import OllamaProvider

def get_provider():
    provider = os.getenv("LLM_PROVIDER", "ollama").lower()
    if provider == "ollama":
        return OllamaProvider()
    raise ValueError(f"Unsupported provider: {provider}")
