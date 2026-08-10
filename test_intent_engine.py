from app.intelligence.intent_engine import IntentEngine


def main():
    engine = IntentEngine()

    test_commands = [
        "What time is it?",
        "Tell me the current time",
        "What's today's date?",
        "Calculate 25 + 15",
        "How much is 100 / 4",
        "How much CPU am I using?",
        "How much RAM am I using?",
        "How is my computer?",
        "Hello Jarvis",
        "Tell me something random",
    ]

    for command in test_commands:
        result = engine.analyze(command)

        print("=" * 60)
        print(f"Command    : {command}")
        print(f"Intent     : {result.intent}")
        print(f"Confidence : {result.confidence}")
        print(f"Parameters : {result.parameters}")


if __name__ == "__main__":
    main()
