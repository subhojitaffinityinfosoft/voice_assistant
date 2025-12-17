import sounddevice as sd
import queue


q = queue.Queue()




def callback(indata, frames, time, status):
    q.put(bytes(indata))




def start_stream(sample_rate):
 return sd.RawInputStream(
samplerate=sample_rate,
blocksize=8000,
dtype='int16',
channels=1,
callback=callback
)