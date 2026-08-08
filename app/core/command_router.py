from typing import Optional


class CommandRouter:
    """
    Routes user commands to the appropriate JARVIS tool.
    """

    def __init__(self, tool_manager):
        self.tools = tool_manager

    def route(self, message: str) -> Optional[str]:
        """
        Analyze the user's message and execute the
        appropriate tool when a known command is detected.
        """

        lower_message = message.lower().strip()

        if "time" in lower_message:
            tool = self.tools.get_tool("datetime")

            return (
                f"The current time is "
                f"{tool.current_time()}"
            )

        if "date" in lower_message:
            tool = self.tools.get_tool("datetime")

            return (
                f"Today's date is "
                f"{tool.current_date()}"
            )

        if "cpu" in lower_message:
            tool = self.tools.get_tool("system")

            return (
                f"CPU usage is "
                f"{tool.cpu_usage()}%"
            )

        return None