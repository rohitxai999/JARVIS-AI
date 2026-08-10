from enum import Enum


class IntentType(str, Enum):
    """Supported JARVIS user intents."""

    GET_TIME = "get_time"
    GET_DATE = "get_date"

    CALCULATE = "calculate"

    SYSTEM_STATUS = "system_status"
    CPU_USAGE = "cpu_usage"
    MEMORY_USAGE = "memory_usage"

    GENERAL_CONVERSATION = "general_conversation"

    UNKNOWN = "unknown"