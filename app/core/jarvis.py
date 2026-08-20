from app.services.llm_service import LLMService
from app.config.settings import ASSISTANT_NAME

from app.core.memory_manager import MemoryManager
from app.core.command_router import CommandRouter
from app.tools.tool_manager import ToolManager
from app.agents.autonomous_task_manager import AutonomousTaskManager
from app.agents.task import TaskStatus


class Jarvis:

    def __init__(self):

        self.llm = LLMService()

        # Memory system
        self.memory = MemoryManager()

        # Tool system
        self.tools = ToolManager()

        # Existing Day 7 command router
        self.router = CommandRouter(self.tools)

        # Day 8: Autonomous task system
        self.autonomous_manager = AutonomousTaskManager(
            self.tools
        )

    def chat(self, message: str) -> str:

        if not message.strip():
            return "Please enter a message."

        # Save user message
        self.memory.add_conversation(
            "user",
            message
        )

        # Day 8:
        # Detect requests that should be handled as
        # autonomous multi-step tasks before the
        # single-command router.
        if self._should_use_autonomous_task(message):

            task = self.autonomous_manager.run(message)

            if task.status == TaskStatus.COMPLETED:
                response = self._format_task_result(task)
            else:
                response = None

        else:
            # Existing Day 7 command routing
            response = self.router.route(message)

        # AI fallback
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

    @staticmethod
    def _should_use_autonomous_task(message: str) -> bool:

        text = message.lower().strip()

        autonomous_phrases = [
            "check the system status",
            "check system status",
            "check cpu and memory",
            "check cpu and ram",
            "analyze the system",
            "analyze system",
        ]

        return any(
            phrase in text
            for phrase in autonomous_phrases
        )

    @staticmethod
    def _format_task_result(task) -> str:

        if not task.steps:
            return "Task completed successfully."

        results = []

        for step in task.steps:

            results.append(
                f"{step.name}: {step.result}"
            )

        return (
            "Task completed successfully. "
            + " ".join(results)
        )

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