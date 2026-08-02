import os
import time

from elevenlabs.client import ElevenLabs
from dotenv import load_dotenv
from playsound import playsound


load_dotenv()


API_KEY = os.getenv("ELEVENLABS_API_KEY")


client = ElevenLabs(
    api_key=API_KEY
)


VOICE_ID = "2HuhvFHmwHXpWQepuKTb"


def speak(text):

    print("JARVIS:", text)

    try:

        if not API_KEY:
            print("ERROR: ElevenLabs API key missing")
            return


        print("Generating voice...")


        audio = client.text_to_speech.convert(
            voice_id=VOICE_ID,
            model_id="eleven_multilingual_v2",
            output_format="mp3_44100_128",
            text=text
        )


        # Create unique filename

        os.makedirs(
            "output",
            exist_ok=True
        )


        filename = (
            f"output/jarvis_voice_{int(time.time())}.mp3"
        )


        with open(filename, "wb") as f:

            for chunk in audio:
                f.write(chunk)


        print("Audio created:", filename)


        print("Playing voice...")

        playsound(filename)


        print("Voice completed")


        # Remove file after playing

        try:
            os.remove(filename)

        except:
            pass


    except Exception as e:

        print("VOICE ERROR:")
        print(e)