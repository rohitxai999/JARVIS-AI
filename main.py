from app.core.jarvis import Jarvis

from app.voice.elevenlabs_voice import speak
from app.voice.listen import listen


def main():

    jarvis = Jarvis()

    jarvis.welcome()

    speak(
        "Hello Rohit, JARVIS voice system is online."
    )


    while True:

        print("\nChoose input mode:")
        print("1. Voice")
        print("2. Keyboard")

        mode = input("Mode: ").strip()


        if mode == "1":

            user_input = listen()


        else:

            user_input = input(
                "\nYou: "
            ).strip()


        if user_input.lower() in [
            "exit",
            "quit",
            "bye"
        ]:

            speak(
                "Goodbye Rohit. Have a great day."
            )

            print(
                "\nJARVIS: Goodbye! Have a great day."
            )

            break


        if not user_input:
            continue


        try:

            response = jarvis.chat(
                user_input
            )


            print(
                f"\nJARVIS: {response}\n"
            )


            speak(
                response
            )


        except Exception as e:

            print(
                f"\nError: {e}\n"
            )


if __name__ == "__main__":
    main()