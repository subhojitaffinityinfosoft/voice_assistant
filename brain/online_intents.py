import wikipedia
from speech.tts import speak

def online_intent(text):
    """
    Use Wikipedia to answer general questions like 'Who is Virat Kohli?'
    """
    try:
        summary = wikipedia.summary(text, sentences=2)
        speak(summary)
    except wikipedia.DisambiguationError as e:
        speak("Multiple options found. Please be more specific.")
    except wikipedia.PageError:
        speak("Sorry, I could not find information on that.")
    except Exception:
        speak("Sorry, something went wrong while searching.")
