import os
from unittest.mock import MagicMock, patch

import pytest
import requests

from agentre.llm.ollama import OllamaProvider


class TestOllamaProvider:
    """Test suite for OllamaProvider."""

    def test_init_with_defaults(self):
        """Test initialization with default values."""
        with patch.dict(os.environ, {}, clear=True):
            provider = OllamaProvider()
            assert provider.base_url == "http://localhost:11434"
            assert provider.model == "gemma3:4b"

    def test_init_with_custom_values(self):
        """Test initialization with custom base_url and model."""
        provider = OllamaProvider(
            base_url="http://custom:8000",
            model="llama2:7b",
        )
        assert provider.base_url == "http://custom:8000"
        assert provider.model == "llama2:7b"

    def test_init_with_trailing_slash(self):
        """Test that trailing slash is removed from base_url."""
        provider = OllamaProvider(base_url="http://localhost:11434/")
        assert provider.base_url == "http://localhost:11434"

    def test_init_with_env_variables(self):
        """Test initialization with environment variables."""
        with patch.dict(
            os.environ,
            {
                "OLLAMA_BASE_URL": "http://remote:11434",
                "OLLAMA_MODEL": "neural-chat:7b",
            },
        ):
            provider = OllamaProvider()
            assert provider.base_url == "http://remote:11434"
            assert provider.model == "neural-chat:7b"

    def test_init_env_vars_overridden_by_params(self):
        """Test that constructor parameters override environment variables."""
        with patch.dict(
            os.environ,
            {
                "OLLAMA_BASE_URL": "http://remote:11434",
                "OLLAMA_MODEL": "neural-chat:7b",
            },
        ):
            provider = OllamaProvider(
                base_url="http://local:9999",
                model="custom:4b",
            )
            assert provider.base_url == "http://local:9999"
            assert provider.model == "custom:4b"

    @patch("agentre.llm.ollama.requests.post")
    def test_generate_success(self, mock_post):
        """Test successful response from generate method."""
        expected_response = "This is a generated response."
        mock_response = MagicMock()
        mock_response.json.return_value = {"response": expected_response}
        mock_post.return_value = mock_response

        provider = OllamaProvider()
        result = provider.generate("Hello, world!")

        assert result == expected_response
        mock_post.assert_called_once_with(
            "http://localhost:11434/api/generate",
            json={
                "model": "gemma3:4b",
                "prompt": "Hello, world!",
                "stream": False,
            },
            timeout=120,
        )

    @patch("agentre.llm.ollama.requests.post")
    def test_generate_with_custom_config(self, mock_post):
        """Test generate with custom base_url and model."""
        expected_response = "Custom response"
        mock_response = MagicMock()
        mock_response.json.return_value = {"response": expected_response}
        mock_post.return_value = mock_response

        provider = OllamaProvider(
            base_url="http://custom:8000",
            model="llama2:7b",
        )
        result = provider.generate("Test prompt")

        assert result == expected_response
        mock_post.assert_called_once_with(
            "http://custom:8000/api/generate",
            json={
                "model": "llama2:7b",
                "prompt": "Test prompt",
                "stream": False,
            },
            timeout=120,
        )

    @patch("agentre.llm.ollama.requests.post")
    def test_generate_http_error(self, mock_post):
        """Test handling of HTTP errors."""
        mock_post.side_effect = requests.exceptions.HTTPError(
            "Connection failed"
        )

        provider = OllamaProvider()
        with pytest.raises(requests.exceptions.HTTPError):
            provider.generate("Test prompt")

    @patch("agentre.llm.ollama.requests.post")
    def test_generate_timeout(self, mock_post):
        """Test handling of timeout errors."""
        mock_post.side_effect = requests.exceptions.Timeout(
            "Request timed out"
        )

        provider = OllamaProvider()
        with pytest.raises(requests.exceptions.Timeout):
            provider.generate("Test prompt")

    @patch("agentre.llm.ollama.requests.post")
    def test_generate_connection_error(self, mock_post):
        """Test handling of connection errors."""
        mock_post.side_effect = requests.exceptions.ConnectionError(
            "Could not connect to server"
        )

        provider = OllamaProvider()
        with pytest.raises(requests.exceptions.ConnectionError):
            provider.generate("Test prompt")

    @patch("agentre.llm.ollama.requests.post")
    def test_generate_invalid_json_response(self, mock_post):
        """Test handling of invalid JSON responses."""
        mock_response = MagicMock()
        mock_response.json.side_effect = ValueError("Invalid JSON")
        mock_post.return_value = mock_response

        provider = OllamaProvider()
        with pytest.raises(ValueError):
            provider.generate("Test prompt")

    @patch("agentre.llm.ollama.requests.post")
    def test_generate_missing_response_key(self, mock_post):
        """Test handling of missing 'response' key in JSON."""
        mock_response = MagicMock()
        mock_response.json.return_value = {"error": "No response"}
        mock_post.return_value = mock_response

        provider = OllamaProvider()
        with pytest.raises(KeyError):
            provider.generate("Test prompt")


def test_ollama_provider_configuration():
    provider = OllamaProvider(
        base_url="http://localhost:11434",
        model="gemma3:4b",
    )

    assert provider.base_url == "http://localhost:11434"
    assert provider.model == "gemma3:4b"
