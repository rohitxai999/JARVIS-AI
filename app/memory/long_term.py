import json
import os


class LongTermMemory:

    def __init__(self, file_path="data/memory.json"):
        self.file_path = file_path
        self.memory = self.load_memory()


    def load_memory(self):

        if os.path.exists(self.file_path):

            with open(self.file_path, "r") as file:
                return json.load(file)

        return {}


    def save_memory(self):

        os.makedirs(
            os.path.dirname(self.file_path),
            exist_ok=True
        )

        with open(self.file_path, "w") as file:
            json.dump(
                self.memory,
                file,
                indent=4
            )


    def remember(self, key, value):

        self.memory[key] = value
        self.save_memory()


    def recall(self, key):

        return self.memory.get(
            key,
            None
        )


    def forget(self, key):

        if key in self.memory:

            del self.memory[key]
            self.save_memory()