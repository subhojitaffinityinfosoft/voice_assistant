# test_stt.py
from speech.stt_offline import recognize_from_mic

print("Speak now...")
text = recognize_from_mic()
print("You said:", text)
