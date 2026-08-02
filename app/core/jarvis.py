from app.services.llm_service import LLMService
from app.config.settings import ASSISTANT_NAME

from app.core.memory_manager import MemoryManager
from app.tools.tool_manager import ToolManager


class Jarvis:

    def __init__(self):

        self.llm = LLMService()

        # Day 3 additions
        self.memory = MemoryManager()
        self.tools = ToolManager()


    def chat(self, message: str) -> str:

        if not message.strip():
            return "Please enter a message."


        # Save user message
        self.memory.add_conversation(
            "user",
            message
        )


        response = None


        # Simple tool detection

        lower_message = message.lower()


        if "time" in lower_message:

            tool = self.tools.get_tool(
                "datetime"
            )

            response = (
                f"The current time is "
                f"{tool.current_time()}"
            )


        elif "date" in lower_message:

            tool = self.tools.get_tool(
                "datetime"
            )

            response = (
                f"Today's date is "
                f"{tool.current_date()}"
            )


        elif "cpu" in lower_message:

            tool = self.tools.get_tool(
                "system"
            )

            response = (
                f"CPU usage is "
                f"{tool.cpu_usage()}%"
            )


        # If no tool is used, use AI

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