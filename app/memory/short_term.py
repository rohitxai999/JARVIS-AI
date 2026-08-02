from collections import deque


class ShortTermMemory:
    def __init__(self, max_messages=20):
        self.memory = deque(maxlen=max_messages)

    def add_message(self, role, content):
        message = {
            "role": role,
            "content": content
        }

        self.memory.append(message)

    def get_history(self):
        return list(self.memory)

    def clear(self):
        self.memory.clear()

    def get_last_message(self):
        if len(self.memory) > 0:
            return self.memory[-1]

        return None