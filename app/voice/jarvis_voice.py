from app.voice.text_to_speech import speak
from app.voice.microphone import record_audio


def start_voice():

    speak(
        "Hello Rohit, JARVIS is online."
    )


    while True:

        command = input(
            "Type command: "
        )


        if "hello" in command.lower():

            speak(
                "Hello sir, how can I help you?"
            )


        elif "stop" in command.lower():

            speak(
                "Goodbye sir."
            )

            break


        else:

            speak(
                "I am still learning this command."
            )