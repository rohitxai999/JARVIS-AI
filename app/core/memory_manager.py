from app.memory.short_term import ShortTermMemory
from app.memory.long_term import LongTermMemory


class MemoryManager:

    def __init__(self):

        self.short_term = ShortTermMemory()
        self.long_term = LongTermMemory()


    # Conversation memory

    def add_conversation(self, role, message):

        self.short_term.add_message(
            role,
            message
        )


    def get_conversation(self):

        return self.short_term.get_history()


    def clear_conversation(self):

        self.short_term.clear()


    # Permanent memory

    def remember(self, key, value):

        self.long_term.remember(
            key,
            value
        )


    def recall(self, key):

        return self.long_term.recall(
            key
        )


    def forget(self, key):

        self.long_term.forget(
            key
        )   