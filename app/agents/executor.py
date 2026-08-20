from app.agents.task import Task, TaskStatus
from app.tools.tool_manager import ToolManager


class TaskExecutor:
    """
    Executes planned JARVIS tasks through the existing ToolManager.
    """

    def __init__(self, tool_manager=None):
        self.tool_manager = tool_manager or ToolManager()

    def execute(self, task: Task) -> Task:
        if not task.steps:
            task.status = TaskStatus.FAILED
            task.error = task.error or "Task contains no executable steps."
            return task

        task.status = TaskStatus.RUNNING

        try:
            for step in task.steps:
                step.status = TaskStatus.RUNNING

                tool = self.tool_manager.get_tool(step.tool)

                if tool is None:
                    step.status = TaskStatus.FAILED
                    task.status = TaskStatus.FAILED
                    task.error = f"Tool not found: {step.tool}"
                    return task

                action = getattr(tool, step.action, None)

                if action is None:
                    step.status = TaskStatus.FAILED
                    task.status = TaskStatus.FAILED
                    task.error = (
                        f"Action '{step.action}' "
                        f"not found on tool '{step.tool}'."
                    )
                    return task

                step.result = action(**step.parameters)
                step.status = TaskStatus.COMPLETED

            task.status = TaskStatus.COMPLETED

            task.result = [
                {
                    "step": step.name,
                    "result": step.result,
                }
                for step in task.steps
            ]

            return task

        except Exception as exc:
            task.status = TaskStatus.FAILED
            task.error = str(exc)

            for step in task.steps:
                if step.status == TaskStatus.RUNNING:
                    step.status = TaskStatus.FAILED

            return task