from app.agents.task import Task, TaskStatus


class TaskVerifier:
    """
    Verifies whether an executed JARVIS task completed successfully.
    """

    def verify(self, task: Task) -> bool:
        if task.status != TaskStatus.COMPLETED:
            return False

        if not task.steps:
            return False

        return all(
            step.status == TaskStatus.COMPLETED
            for step in task.steps
        )