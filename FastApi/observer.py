from typing import Dict, List
from fastapi import WebSocket


observers: Dict[str, List[WebSocket]] = {}

def add_observer(topic: str, websocket: WebSocket):
    if topic not in observers:
        observers[topic] = []
    observers[topic].append(websocket)
    print(f"Added observer for topic '{topic}'")

async def notify_observers(topic: str, message: str):
    if topic in observers:
        for observer in observers[topic]:
            try:
                await observer.send_text(message)
                print(f"Sent message '{message}' to topic '{topic}'")
            except Exception as e:
                print(f"Error sending message to observer: {e}")
                observers[topic].remove(observer)  
