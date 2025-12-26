from speech.stt_offline import recognize_from_mic
from brain.intent_router import route
from speech.tts import speak
from config.settings import ASSISTANT_NAME

print("Assistant is running. Say 'Dracarys' to wake me up...")

awake = False

while True:
    print("Listening...")
    text = recognize_from_mic()

    if not text:
        continue

    print("Heard:", text)

    # Wake word
    if not awake and ASSISTANT_NAME in text:
        awake = True
        speak("Yes?")
        continue

    # Command after wake word
    if awake:
        route(text)
        awake = False
