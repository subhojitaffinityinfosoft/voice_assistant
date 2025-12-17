from speech.stt_offline import recognize_from_mic
from brain.intent_router import route
from speech.tts import speak

print("Assistant is running (no wake word for testing)...")

while True:
    text = recognize_from_mic()
    if text:
        print("Heard:", text)
        route(text)  # send all speech directly to intent router
