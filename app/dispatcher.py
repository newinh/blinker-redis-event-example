import threading
import time
from contextlib import contextmanager
from typing import NewType, Tuple
from functools import wraps
from enum import Enum
import json

import blinker

from app.event_broker import event_broker

EventKey = NewType('EventKey', bytes)
EventValue = NewType('EventValue', bytes)


class EventType(Enum):
    NOTICE_DELETED = 'NOTICE_DELETE'
    NOTICE_MODIFIED = 'NOTICE_MODIFIED'


class Event(object):

    def __init__(self, event_type: EventType, data: dict):
        self.type = event_type
        self.data = data

    @classmethod
    def load(cls, serialized):
        type_ = EventType(serialized['type'])
        return cls(type_, serialized['data'])

    def serialize(self):
        obj = vars(self)
        obj['type'] = self.type.value
        return json.dumps(obj)


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

        serialized_event = json.loads(event_msg[1].decode())
        event = Event.load(serialized_event)

        if event.type == EventType.NOTICE_DELETED:
            notice_id = event.data.get('notice_id')
            Dispatcher.signal(event.type.value).send("i'm sender", notice_id=notice_id)


class Dispatcher(object):
    signal = blinker.signal

    @staticmethod
    def source(event: Event) -> None:
        event_msg = event.serialize()
        event_broker.lpush('dbtool:event', event_msg)

    @classmethod
    def register(cls, event: EventType):
        def decorator(func):
            cls.signal(event.value).connect(func)
            print(f'Event handler registered: [{func}] handle {event}')

            @wraps(func)
            def wrapper(*args, **kwargs):
                return func(*args, **kwargs)

            return wrapper

        return decorator
