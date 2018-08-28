import threading
import time
from functools import wraps
from typing import NewType, Tuple

import blinker

from app.event_broker import event_broker
from app.event import Event, EventType

EventKey = NewType('EventKey', bytes)
EventValue = NewType('EventValue', bytes)


def source(event: 'Event') -> None:
    event_msg = event.serialize()
    event_broker.lpush('dbtool:event', event_msg)


def subscribe(event: 'EventType'):
    def decorator(func):
        blinker.signal(event.value).connect(func)
        print(f'Event handler registered: [{func}] handle {event}')

        @wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)

        return wrapper

    return decorator


def run_event_handling_loop():
    event_handling_thread = threading.Thread(target=listen_event)
    event_handling_thread.start()
    return event_handling_thread


def listen_event() -> None:
    """
    * Get event from eternal event broker.(redis)
    * publish event using internal event signal. (blinker)
    """
    print("event polling start")
    while True:
        raw_event: Tuple[EventKey, EventValue] = event_broker.brpop("dbtool:event", timeout=3)

        if not raw_event:
            time.sleep(0.01)
            print("loop...")
            continue

        event_value = raw_event[1].decode()
        if event_value == 'quit':
            break

        event = Event.load(event_value)
        event.publish()
