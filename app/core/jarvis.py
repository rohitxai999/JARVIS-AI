from app.services.llm_service import LLMService
from app.config.settings import ASSISTANT_NAME

from app.core.memory_manager import MemoryManager
from app.core.command_router import CommandRouter
from app.tools.tool_manager import ToolManager


class Jarvis:

    def __init__(self):

        self.llm = LLMService()

        # Memory system
        self.memory = MemoryManager()

        # Tool system
        self.tools = ToolManager()

        # Day 6: Command Router
        self.router = CommandRouter(self.tools)

    def chat(self, message: str) -> str:

        if not message.strip():
            return "Please enter a message."

        # Save user message
        self.memory.add_conversation(
            "user",
            message
        )

        # Day 6: Route command through CommandRouter
        response = self.router.route(message)

        # If no command/tool matched, use AI
        if response is None:

            response = self.llm.generate_response(
                message
            )

        # Save assistant response
        self.memory.add_conversation(
            "assistant",
            response
        )

        return response

    def welcome(self):

        print("=" * 50)
        print(f"        {ASSISTANT_NAME} AI v1.0")
        print("=" * 50)
        print()

        print(
            f"{ASSISTANT_NAME}: Hello! I'm {ASSISTANT_NAME}."
        )

        print(
            "Type 'exit', 'quit', or 'bye' to end the conversation."
        )

        print()