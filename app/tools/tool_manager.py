from app.tools.calculator import Calculator
from app.tools.datetime_tool import DateTimeTool
from app.tools.system_tool import SystemTool


class ToolManager:

    def __init__(self):

        self.tools = {
            "calculator": Calculator(),
            "datetime": DateTimeTool(),
            "system": SystemTool()
        }


    def get_tool(self, name):

        return self.tools.get(name)


    def list_tools(self):

        return list(self.tools.keys())