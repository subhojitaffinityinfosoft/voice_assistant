import sys
import os
import time
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from speech.listener import start_stream, q
from speech.stt_offline import recognize
from brain.intent_router import route
from speech.tts import speak
from config.settings import SAMPLE_RATE

WAKE_WORD = "dracarys"  # Your chosen wake word
COMMAND_TIMEOUT = 10      # Seconds to wait for the next command after wake word

print("Assistant started. Say 'Dracarys' to activate.")

with start_stream(SAMPLE_RATE):
    while True:
        # Continuously listen
        data = q.get()
        text = recognize(data)

        if text:
            text_lower = text.lower()
            # Check for wake word
            if WAKE_WORD in text_lower:
                speak("Yes, how can I help you?")
                print("Wake word detected. Listening for command...")

                # Start timer for command listening
                start_time = time.time()
                command_text = ""

                while time.time() - start_time < COMMAND_TIMEOUT:
                    if not q.empty():
                        cmd_data = q.get()
                        command_text = recognize(cmd_data)
                        if command_text:
                            break

                if command_text:
                    print("You said:", command_text)
                    route(command_text)
                else:
                    speak("No command detected, going back to sleep.")
                    print("No command detected, listening for wake word again...")
