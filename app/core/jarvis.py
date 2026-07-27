from app.services.llm_service import LLMService
from app.config.settings import ASSISTANT_NAME


class Jarvis:

    def __init__(self):
        self.llm = LLMService()

    def chat(self, message: str) -> str:

        if not message.strip():
            return "Please enter a message."

        return self.llm.generate_response(message)

    def welcome(self):

        print("=" * 50)
        print(f"        {ASSISTANT_NAME} AI v1.0")
        print("=" * 50)
        print()

        print(f"{ASSISTANT_NAME}: Hello! I'm {ASSISTANT_NAME}.")
        print("Type 'exit', 'quit', or 'bye' to end the conversation.")
        print()