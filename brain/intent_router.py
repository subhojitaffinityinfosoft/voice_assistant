from brain.offline_intents import handle
from brain.online_intents import online_intent

def route(text):
    """
    Decide whether command is offline or online AI search
    """
    text_lower = text.lower()
    offline_keywords = ["time", "hello", "hi", "light", "stop"]

    if any(k in text_lower for k in offline_keywords):
        handle(text)
    else:
        online_intent(text)  # Wikipedia voice search
