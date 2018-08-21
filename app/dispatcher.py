
import threading
import time
# from .redis_publisher import event_broker
from .event_broker import fredis
from .notice import deleted_notice_event_broker, modified_notice_event_broker

from app.notice.repository import NoticeRepository

from blinker import signal


# register(handler)
signal('DELETED_NOTICE').connect(NoticeRepository.delete,)


def event_handling():

    print("event handling start")
    while True:
        # msg = event_broker.get_message(ignore_subscribe_messages=True)
        msg = fredis.brpop("dbtool:event")

        if msg:
            print(f"got message : {str(msg)}")

            if msg == b'test':
                deleted_notice_event_broker.send('DELETE NOTICE EVENT SOURCE')

        time.sleep(0.01)
        print("loop...")


threading.Thread(target=event_handling).start()

from enum import Enum

class EVENTS(Enum):
    NOTICE_DELTE = 0


from typing import TypeVar, Dict

EVENT = TypeVar()
import blinker.signal

class Dispatcher(object):


    signal = blinker.signal

    # TODO: Decorate Function
    def register(self, event_name):


        f = 0

        signal(event_name).connect(f)

        pass
