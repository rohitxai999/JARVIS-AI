from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Dict, List, Optional


class TaskStatus(str, Enum):
    PENDING = "pending"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"
    CANCELLED = "cancelled"


@dataclass
class TaskStep:
    name: str
    tool: str
    action: str
    parameters: Dict[str, Any] = field(default_factory=dict)
    result: Optional[Any] = None
    status: TaskStatus = TaskStatus.PENDING


@dataclass
class Task:
    goal: str
    steps: List[TaskStep] = field(default_factory=list)
    status: TaskStatus = TaskStatus.PENDING
    result: Optional[Any] = None
    error: Optional[str] = None

    def add_step(self, step: TaskStep) -> None:
        self.steps.append(step)

    def is_completed(self) -> bool:
        return self.status == TaskStatus.COMPLETED

    def is_failed(self) -> bool:
        return self.status == TaskStatus.FAILED