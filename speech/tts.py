import pyttsx3

engine = pyttsx3.init()
engine.setProperty("rate", 170)    # speaking speed
engine.setProperty("volume", 1.0) # max volume

def speak(text):
    print("Assistant:", text)   # helps debugging
    engine.say(text)
    engine.runAndWait()
