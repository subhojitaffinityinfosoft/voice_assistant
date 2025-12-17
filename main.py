from speech.listener import start_stream, q
from speech.stt_offline import recognize
from brain.intent_router import route
from speech.tts import speak
from config.settings import SAMPLE_RATE

print("Assistant started")
speak("Assistant is ready")

print("Press ENTER to speak")
input()

with start_stream(SAMPLE_RATE):
    while True:
        data = q.get()
        text = recognize(data)

        if text:
            print("You said:", text)
            route(text)
