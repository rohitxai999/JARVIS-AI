import sounddevice as sd
from scipy.io.wavfile import write
import numpy as np
import speech_recognition as sr


class SpeechToText:

    def __init__(self):
        self.recognizer = sr.Recognizer()


    def record_audio(
        self,
        filename="voice.wav",
        duration=5,
        samplerate=16000
    ):

        print("🎤 Listening...")

        audio = sd.rec(
            int(duration * samplerate),
            samplerate=samplerate,
            channels=1,
            dtype="int16"
        )

        sd.wait()

        write(
            filename,
            samplerate,
            audio
        )

        print("Recording complete")


    def listen(self):

        filename = "voice.wav"

        self.record_audio(filename)

        with sr.AudioFile(filename) as source:
            audio = self.recognizer.record(source)

        try:
            text = self.recognizer.recognize_google(
                audio,
                language="en-IN"
            )

            return text

        except Exception as e:
            print(e)
            return "Sorry, I could not understand."