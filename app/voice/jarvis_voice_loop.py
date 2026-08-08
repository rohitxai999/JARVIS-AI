from app.core.jarvis import Jarvis
from app.voice.voice_manager import VoiceManager


class JarvisVoiceLoop:

    def __init__(self):
        self.jarvis = Jarvis()
        self.voice = VoiceManager()

    def run(self):

        print("=" * 50)
        print("        JARVIS AI — VOICE MODE")
        print("=" * 50)
        print("Speak to JARVIS. Say 'exit' to stop.")
        print()

        while True:

            user_text = self.voice.listen()

            if not user_text:
                continue

            if user_text.lower().strip() in {
                "exit",
                "quit",
                "bye",
                "stop",
            }:
                self.voice.speak("Goodbye.")
                break

            response = self.jarvis.chat(user_text)

            print("JARVIS:", response)

            self.voice.speak(response)


if __name__ == "__main__":
    JarvisVoiceLoop().run()