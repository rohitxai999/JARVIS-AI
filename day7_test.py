from app.intelligence.intent_engine import IntentEngine

engine = IntentEngine()

commands = [
    "What time is it?",
    "Tell me the current time",
    "What's today's date?",
    "Calculate 25 + 15",
    "How much is 100 / 4",
    "How much CPU am I using?",
    "How much RAM am I using?",
    "How is my computer?",
    "Hello Jarvis",
    "Tell me something random"
]

for command in commands:
    result = engine.analyze(command)

    print("=" * 60)
    print("Command    :", command)
    print("Intent     :", result.intent)
    print("Confidence :", result.confidence)
    print("Parameters :", result.parameters)
