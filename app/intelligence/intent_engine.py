import re

from app.intelligence.intent_result import IntentResult
from app.intelligence.intent_types import IntentType


class IntentEngine:
    """
    Lightweight deterministic intent engine for JARVIS.

    This is the first layer of JARVIS intelligence.
    It converts natural-language commands into structured intents.
    """

    def analyze(self, text: str) -> IntentResult:
        if not text or not text.strip():
            return IntentResult(
                intent=IntentType.UNKNOWN,
                confidence=0.0,
                original_text=text,
            )

        normalized = self._normalize(text)

        # Time
        if self._matches(
            normalized,
            [
                r"\bwhat time is it\b",
                r"\bwhat(?:'s| is) the time\b",
                r"\bcurrent time\b",
                r"\btell me the time\b",
                r"\btime right now\b",
            ],
        ):
            return IntentResult(
                intent=IntentType.GET_TIME,
                confidence=0.98,
                original_text=text,
            )

        # Date
        if self._matches(
            normalized,
            [
                r"\bwhat(?:'s| is)? the date\b",
                r"\bcurrent date\b",
                r"\btoday'?s date\b",
                r"\bwhat day is it\b",
            ],
        ):
            return IntentResult(
                intent=IntentType.GET_DATE,
                confidence=0.98,
                original_text=text,
            )

        # Calculation
        if self._matches(
            normalized,
            [
                r"\bcalculate\b",
                r"\bsolve\b",
                r"\bwhat is \d",
                r"\bhow much is \d",
            ],
        ):
            expression = self._extract_expression(normalized)

            return IntentResult(
                intent=IntentType.CALCULATE,
                confidence=0.94,
                parameters={"expression": expression},
                original_text=text,
            )

        # CPU
        if self._matches(
            normalized,
            [
                r"\bcpu\b",
                r"\bprocessor usage\b",
                r"\bprocessor utilization\b",
            ],
        ):
            return IntentResult(
                intent=IntentType.CPU_USAGE,
                confidence=0.95,
                original_text=text,
            )

        # Memory / RAM
        if self._matches(
            normalized,
            [
                r"\bram\b",
                r"\bmemory usage\b",
                r"\bmemory utilization\b",
            ],
        ):
            return IntentResult(
                intent=IntentType.MEMORY_USAGE,
                confidence=0.95,
                original_text=text,
            )

        # General system status
        if self._matches(
            normalized,
            [
                r"\bsystem status\b",
                r"\bsystem health\b",
                r"\bcomputer status\b",
                r"\bhow is my computer\b",
            ],
        ):
            return IntentResult(
                intent=IntentType.SYSTEM_STATUS,
                confidence=0.93,
                original_text=text,
            )

        # Conversation
        if self._matches(
            normalized,
            [
                r"\bhello\b",
                r"\bhi jarvis\b",
                r"\bhey jarvis\b",
                r"\bhow are you\b",
                r"\bwho are you\b",
            ],
        ):
            return IntentResult(
                intent=IntentType.GENERAL_CONVERSATION,
                confidence=0.90,
                original_text=text,
            )

        return IntentResult(
            intent=IntentType.UNKNOWN,
            confidence=0.0,
            original_text=text,
        )

    @staticmethod
    def _normalize(text: str) -> str:
        text = text.lower().strip()
        text = re.sub(r"\s+", " ", text)
        return text

    @staticmethod
    def _matches(text: str, patterns: list[str]) -> bool:
        return any(re.search(pattern, text) for pattern in patterns)

    @staticmethod
    def _extract_expression(text: str) -> str:
        expression = re.sub(
            r"^(calculate|solve|what is|how much is)\s*",
            "",
            text,
        ).strip()

        return expression
