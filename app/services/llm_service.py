from groq import Groq
from openai import OpenAI

from app.config.settings import (
    GROQ_API_KEY,
    OPENAI_API_KEY,
    DEFAULT_PROVIDER,
)


class LLMService:
    """
    Handles communication with different LLM providers.
    """

    def __init__(self):
        self.provider = DEFAULT_PROVIDER

        self.groq_client = None
        self.openai_client = None

        if GROQ_API_KEY:
            self.groq_client = Groq(api_key=GROQ_API_KEY)

        if OPENAI_API_KEY:
            self.openai_client = OpenAI(api_key=OPENAI_API_KEY)

    def get_provider(self):
        return self.provider

    def set_provider(self, provider: str):
        provider = provider.lower()

        if provider not in ["groq", "openai"]:
            raise ValueError("Unsupported provider.")

        self.provider = provider

    def generate_response(self, prompt: str) -> str:

        if self.provider == "groq":

            if self.groq_client is None:
                raise ValueError("Groq API key not configured.")

            response = self.groq_client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {
                        "role": "system",
                        "content": (
                            "You are JARVIS, a professional AI assistant. "
                            "Be helpful, concise, and intelligent."
                        ),
                    },
                    {
                        "role": "user",
                        "content": prompt,
                    },
                ],
                temperature=0.7,
                max_tokens=1024,
            )

            return response.choices[0].message.content

        elif self.provider == "openai":

            if self.openai_client is None:
                raise ValueError("OpenAI API key not configured.")

            response = self.openai_client.chat.completions.create(
                model="gpt-4.1",
                messages=[
                    {
                        "role": "system",
                        "content": (
                            "You are JARVIS, a professional AI assistant."
                        ),
                    },
                    {
                        "role": "user",
                        "content": prompt,
                    },
                ],
            )

            return response.choices[0].message.content

        raise ValueError("Invalid provider.")