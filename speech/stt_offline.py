import json
from vosk import Model, KaldiRecognizer
from config.settings import SAMPLE_RATE


model = Model("model/vosk-model-small-en-us-0.15")
recognizer = KaldiRecognizer(model, SAMPLE_RATE)




def recognize(audio_data):
 if recognizer.AcceptWaveform(audio_data):
  result = json.loads(recognizer.Result())
  return result.get("text", "")
 return ""