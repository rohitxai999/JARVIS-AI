from app.memory.short_term import ShortTermMemory


memory = ShortTermMemory()

memory.add_message(
    "user",
    "Hello JARVIS"
)

memory.add_message(
    "assistant",
    "Hello Rohit"
)


print(memory.get_history())

print("----------------")

print(memory.get_last_message())