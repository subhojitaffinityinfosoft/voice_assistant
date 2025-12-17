# brain/intent_router.py
from speech.tts import speak
import wikipedia

def route(command):
    command = command.lower()
    if "who is" in command:
        try:
            person = command.replace("who is", "").strip()
            result = wikipedia.summary(person, sentences=2)
            speak(result)
        except Exception as e:
            speak("Sorry, I could not find that.")
    else:
        speak("I can only answer 'who is' questions for now.")
