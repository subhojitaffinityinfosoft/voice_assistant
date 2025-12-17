from datetime import datetime
from speech.tts import speak




def handle(text):
    text = text.lower()


    if "time" in text:
        now = datetime.now().strftime("%H:%M")
        speak(f"The time is {now}")
        return


    if "hello" in text or "hi" in text:
        speak("Hello, I am your assistant")
        return


    if "light" in text:
        speak("Light control will be added later")
        return


    if "stop" in text:
        speak("Goodbye")
exit()


speak("Sorry, I did not understand")