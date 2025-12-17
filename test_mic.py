import sounddevice as sd

print("Recording 3 seconds...")
audio = sd.rec(int(3 * 16000), samplerate=16000, channels=1, dtype="int16")
sd.wait()
print("Recording finished")
