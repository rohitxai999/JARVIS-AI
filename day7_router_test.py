from app.core.command_router import CommandRouter
from app.tools.tool_manager import ToolManager


router = CommandRouter(ToolManager())

commands = [
    "What time is it?",
    "What's today's date?",
    "How much CPU am I using?",
    "How much RAM am I using?",
    "How is my computer?",
    "Calculate 25 + 15",
    "Tell me something random"
]

for command in commands:
    print("=" * 60)
    print("USER:", command)
    print("JARVIS:", router.route(command))
