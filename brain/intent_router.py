from speech.tts import speak

def route(text):
    if "who is virat kohli" in text:
        speak(
            "Virat Kohli is an Indian international cricketer "
            "and former captain of the Indian cricket team."
        )
        return

    if "open youtube" in text:
        speak("Opening YouTube")
        return

    speak("Sorry, I did not understand.")
