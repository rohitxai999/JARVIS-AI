from app.agents.autonomous_task_manager import AutonomousTaskManager
from app.agents.task import TaskStatus


def test_autonomous_task_manager_system_status():

    manager = AutonomousTaskManager()

    task = manager.run(
        "Check the system status including CPU and memory"
    )

    assert task.status == TaskStatus.COMPLETED
    assert task.error is None

    assert len(task.steps) == 2

    assert task.steps[0].status == TaskStatus.COMPLETED
    assert task.steps[1].status == TaskStatus.COMPLETED

    assert task.steps[0].result is not None
    assert task.steps[1].result is not None


def test_autonomous_task_manager_empty_goal():

    manager = AutonomousTaskManager()

    task = manager.run("")

    assert task.status == TaskStatus.FAILED
    assert task.error == "Task goal cannot be empty."