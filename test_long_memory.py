from app.memory.long_term import LongTermMemory


memory = LongTermMemory()


memory.remember(
    "name",
    "Rohit"
)


print(
    memory.recall("name")
)