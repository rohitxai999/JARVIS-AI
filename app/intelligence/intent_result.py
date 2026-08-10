from dataclasses import dataclass, field
from typing import Any

from app.intelligence.intent_types import IntentType


@dataclass
class IntentResult:
    """Result produced by the JARVIS intent engine."""

    intent: IntentType
    confidence: float
    parameters: dict[str, Any] = field(default_factory=dict)
    original_text: str = ""

    def is_confident(self, threshold: float = 0.60) -> bool:
        return self.confidence >= threshold