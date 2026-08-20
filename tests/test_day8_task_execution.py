from app.agents.executor import TaskExecutor
from app.agents.task import TaskStatus
from app.agents.verifier import TaskVerifier
from app.planner.task_planner import TaskPlanner


def test_system_status_task():

    planner = TaskPlanner()
    executor = TaskExecutor()
    verifier = TaskVerifier()

    task = planner.create_plan(
        "Check the system status including CPU and memory"
    )

    assert len(task.steps) == 2
    assert task.steps[0].tool == "system"
    assert task.steps[1].tool == "system"

    task = executor.execute(task)

    assert task.status == TaskStatus.COMPLETED
    assert verifier.verify(task) is True

    assert task.steps[0].result is not None
    assert task.steps[1].result is not None


def test_multi_step_task():

    planner = TaskPlanner()
    executor = TaskExecutor()
    verifier = TaskVerifier()

    task = planner.create_plan(
        "Check CPU, memory, current time and date"
    )

    assert len(task.steps) == 4

    assert task.steps[0].tool == "system"
    assert task.steps[0].action == "cpu_usage"

    assert task.steps[1].tool == "system"
    assert task.steps[1].action == "memory_usage"

    assert task.steps[2].tool == "datetime"
    assert task.steps[2].action == "current_time"

    assert task.steps[3].tool == "datetime"
    assert task.steps[3].action == "current_date"

    task = executor.execute(task)

    assert task.status == TaskStatus.COMPLETED
    assert verifier.verify(task) is True

    for step in task.steps:
        assert step.status == TaskStatus.COMPLETED
        assert step.result is not None