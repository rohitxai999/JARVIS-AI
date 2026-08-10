from typing import Optional

from app.intelligence.intent_engine import IntentEngine
from app.intelligence.intent_types import IntentType


class CommandRouter:
    """
    Routes structured JARVIS intents to the appropriate tools.
    """

    def __init__(self, tool_manager):
        self.tools = tool_manager
        self.intent_engine = IntentEngine()

    def route(self, message: str) -> Optional[str]:
        """
        Analyze the user's message and execute the
        appropriate tool based on the detected intent.
        """

        result = self.intent_engine.analyze(message)

        if not result.is_confident():
            return None

        if result.intent == IntentType.GET_TIME:
            tool = self.tools.get_tool("datetime")

            return (
                f"The current time is "
                f"{tool.current_time()}"
            )

        if result.intent == IntentType.GET_DATE:
            tool = self.tools.get_tool("datetime")

            return (
                f"Today's date is "
                f"{tool.current_date()}"
            )

        if result.intent == IntentType.CPU_USAGE:
            tool = self.tools.get_tool("system")

            return (
                f"CPU usage is "
                f"{tool.cpu_usage()}%"
            )

        if result.intent == IntentType.MEMORY_USAGE:
            tool = self.tools.get_tool("system")

            return (
                f"Memory usage is "
                f"{tool.memory_usage()}%"
            )

        if result.intent == IntentType.SYSTEM_STATUS:
            tool = self.tools.get_tool("system")

            cpu = tool.cpu_usage()
            memory = tool.memory_usage()

            return (
                f"System status: CPU usage is {cpu}% "
                f"and memory usage is {memory}%."
            )

        if result.intent == IntentType.CALCULATE:
            tool = self.tools.get_tool("calculator")

            expression = result.parameters.get("expression")

            if not expression:
                return "I couldn't determine the calculation."

            return str(tool.calculate(expression))

        return None