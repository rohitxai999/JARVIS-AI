import pyttsx3


class TextToSpeech:

    def __init__(self):
        self.engine = pyttsx3.init()

        voices = self.engine.getProperty("voices")

        if voices:
            self.engine.setProperty("voice", voices[0].id)

        self.engine.setProperty("rate", 170)

    def speak(self, text):
        if not text:
            return

        self.engine.say(text)
        self.engine.runAndWait()


def speak(text):
    """
    Backward-compatible module-level speech function.

    Keeps older JARVIS voice tests and scripts working while
    the main architecture uses the TextToSpeech class.
    """

    if not text:
        return

    tts = TextToSpeech()
    tts.speak(text)