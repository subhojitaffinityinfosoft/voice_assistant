import sounddevice as sd
import queue

q = queue.Queue()

def callback(indata, frames, time, status):
    if status:
        print(status)
    q.put(indata.copy())

def start_stream(sample_rate, device):
    return sd.InputStream(
        samplerate=sample_rate,
        device=device,
        channels=1,
        dtype="int16",
        callback=callback
    )
