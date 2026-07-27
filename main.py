from app.core.jarvis import Jarvis


def main():

    jarvis = Jarvis()

    jarvis.welcome()

    while True:

        user_input = input("You: ").strip()

        if user_input.lower() in ["exit", "quit", "bye"]:
            print("\nJARVIS: Goodbye! Have a great day.")
            break

        if not user_input:
            continue

        try:

            response = jarvis.chat(user_input)

            print(f"\nJARVIS: {response}\n")

        except Exception as e:

            print(f"\nError: {e}\n")


if __name__ == "__main__":
    main()