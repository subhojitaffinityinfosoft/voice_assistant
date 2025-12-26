import speech_recognition as sr

recognizer: sr.Recognizer = sr.Recognizer()

def recognize_from_mic() -> str:
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        audio: sr.AudioData = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)  # type: ignore[attr-defined]
        return text.lower()
    except sr.UnknownValueError:
        return ""
    except sr.RequestError:
        return ""
