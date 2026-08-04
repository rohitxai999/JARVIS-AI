from app.voice.speech_to_text import SpeechToText
from app.voice.text_to_speech import TextToSpeech


class VoiceManager:

    def __init__(self):

        self.stt = SpeechToText()
        self.tts = TextToSpeech()


    def listen(self):

        text = self.stt.listen()

        print("USER:", text)

        return text


    def speak(self, text):

        self.tts.speak(text)


    def conversation_test(self):

        user_text = self.listen()

        response = (
            "Hello. I heard you say: "
            + user_text
        )

        self.speak(response)