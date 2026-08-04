from app.voice.speech_to_text import SpeechToText


stt = SpeechToText()

text = stt.listen()

print("="*50)
print("You said:")
print(text)
print("="*50)