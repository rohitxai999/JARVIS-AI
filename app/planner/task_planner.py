from app.agents.task import Task, TaskStep


class TaskPlanner:
    """
    Converts a high-level JARVIS goal into executable task steps.

    Day 8 implementation uses deterministic planning.
    The architecture is designed to support an LLM-based
    planner in a future phase.
    """

    def create_plan(self, goal: str) -> Task:

        goal = goal.strip()

        task = Task(goal=goal)

        if not goal:
            task.error = "Task goal cannot be empty."
            return task

        lowered = goal.lower()

        # CPU
        if "cpu" in lowered:
            task.add_step(
                TaskStep(
                    name="Check CPU usage",
                    tool="system",
                    action="cpu_usage",
                )
            )

        # Memory / RAM
        if "memory" in lowered or "ram" in lowered:
            task.add_step(
                TaskStep(
                    name="Check memory usage",
                    tool="system",
                    action="memory_usage",
                )
            )

        # Time
        if "time" in lowered:
            task.add_step(
                TaskStep(
                    name="Get current time",
                    tool="datetime",
                    action="current_time",
                )
            )

        # Date
        if "date" in lowered:
            task.add_step(
                TaskStep(
                    name="Get current date",
                    tool="datetime",
                    action="current_date",
                )
            )

        # Explicit system status
        if (
            "system status" in lowered
            and not task.steps
        ):
            task.add_step(
                TaskStep(
                    name="Check CPU usage",
                    tool="system",
                    action="cpu_usage",
                )
            )

            task.add_step(
                TaskStep(
                    name="Check memory usage",
                    tool="system",
                    action="memory_usage",
                )
            )

        if not task.steps:
            task.error = (
                "No executable plan could be created."
            )

        return task