import threading
import time
from contextlib import contextmanager
from typing import NewType, Tuple
from functools import wraps
from enum import Enum

import blinker

from .event_broker import event_broker

EventKey = NewType('EventKey', bytes)
EventValue = NewType('EventValue', bytes)


class Event(Enum):
    NOTICE_DELETED = 'NOTICE_DELETE'
    NOTICE_MODIFIED = 'NOTICE_MODIFIED'


@contextmanager
def run_event_handling_loop():
    event_handling_thread = threading.Thread(target=event_polling)
    try:
        yield event_handling_thread.start()
    finally:
        pass
        event_handling_thread.join()


def event_polling() -> None:
    """
    * Get event from eternal event broker.(redis)
    * Source event using internal event signal. (blinker)
    """
    print("event polling start")
    while True:
        event_msg: Tuple(EventKey, EventValue) = event_broker.brpop("dbtool:event", timeout=3)
        if not event_msg:
            time.sleep(0.01)
            print("loop...")
            continue

        if event_msg[1].decode() == 'quit':
            return

        event = Event(event_msg[1].decode())

        if event:
            print(event)
            Dispatcher.signal(event.value).send("i'm sender")


class Dispatcher(object):
    signal = blinker.signal

    @staticmethod
    def source(event: Event) -> None:
        event_broker.lpush('dbtool:event', event.value)

    @classmethod
    def register(cls, event: Event):
        def decorator(func):
            cls.signal(event.value).connect(func)
            print(f'Event handler registered: [{func}] handle {event}')

            @wraps(func)
            def wrapper(*args, **kwargs):
                return func(*args, **kwargs)

            return wrapper

        return decorator
