import os

import requests

from .base import LLMProvider


class OllamaProvider(LLMProvider):
    """Provider for a local Ollama server."""

    def __init__(
        self,
        base_url: str | None = None,
        model: str | None = None,
    ):
        self.base_url = (
            base_url
            or os.getenv(
                "OLLAMA_BASE_URL",
                "http://localhost:11434",
            )
        ).rstrip("/")

        self.model = model or os.getenv(
            "OLLAMA_MODEL",
            "gemma3:4b",
        )

    def generate(self, prompt: str) -> str:
        """Send a prompt to Ollama and return its response."""

        response = requests.post(
            f"{self.base_url}/api/generate",
            json={
                "model": self.model,
                "prompt": prompt,
                "stream": False,
            },
            timeout=120,
        )

        response.raise_for_status()

        return response.json()["response"]