from typing import Optional

from app.agents.executor import TaskExecutor
from app.agents.task import Task, TaskStatus
from app.agents.verifier import TaskVerifier
from app.planner.task_planner import TaskPlanner
from app.tools.tool_manager import ToolManager


class AutonomousTaskManager:
    """
    High-level autonomous task orchestration layer for JARVIS.

    Pipeline:

        Goal
          ↓
        Plan
          ↓
        Execute
          ↓
        Verify
          ↓
        Result
    """

    def __init__(self, tool_manager: Optional[ToolManager] = None):
        self.tool_manager = tool_manager or ToolManager()
        self.planner = TaskPlanner()
        self.executor = TaskExecutor(self.tool_manager)
        self.verifier = TaskVerifier()

    def run(self, goal: str) -> Task:
        """
        Plan, execute, and verify an autonomous task.
        """

        if not goal or not goal.strip():
            task = Task(
                goal=goal,
                status=TaskStatus.FAILED,
                error="Task goal cannot be empty.",
            )
            return task

        task = self.planner.create_plan(goal)

        if task.error:
            task.status = TaskStatus.FAILED
            return task

        task = self.executor.execute(task)

        if not self.verifier.verify(task):
            if task.status == TaskStatus.COMPLETED:
                task.status = TaskStatus.FAILED
                task.error = "Task verification failed."

        return task