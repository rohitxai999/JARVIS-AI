from app.tools.tool_manager import ToolManager


tools = ToolManager()


print(
    tools.list_tools()
)


calculator = tools.get_tool(
    "calculator"
)


print(
    calculator.multiply(5, 10)
)


time_tool = tools.get_tool(
    "datetime"
)


print(
    time_tool.current_time()
)