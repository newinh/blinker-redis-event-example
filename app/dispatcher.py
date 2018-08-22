from functools import wraps

import blinker

from app.event_broker import event_broker

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from app.event import Event, EventType


class Dispatcher(object):
    signal = blinker.signal

    @staticmethod
    def source(event: 'Event') -> None:
        event_msg = event.serialize()
        event_broker.lpush('dbtool:event', event_msg)

    @classmethod
    def register(cls, event: 'EventType'):
        def decorator(func):
            cls.signal(event.value).connect(func)
            print(f'Event handler registered: [{func}] handle {event}')

            @wraps(func)
            def wrapper(*args, **kwargs):
                return func(*args, **kwargs)

            return wrapper

        return decorator
