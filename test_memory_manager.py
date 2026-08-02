from app.core.memory_manager import MemoryManager


memory = MemoryManager()


memory.add_conversation(
    "user",
    "Hello JARVIS"
)

memory.add_conversation(
    "assistant",
    "Hello Rohit"
)


print("Conversation:")
print(memory.get_conversation())


print("----------------")


memory.remember(
    "favorite_editor",
    "VS Code"
)


print(
    "Preference:",
    memory.recall("favorite_editor")
)