import atexit

from threading import Thread

from app.event_broker import event_broker
from app import app
from app.dispatcher import run_event_handling_loop

event_thread = run_event_handling_loop()


def close_running_thread(t: Thread):
    event_broker.rpush('dbtool:evet', 'quit')
    t.join()


atexit.register(close_running_thread, event_thread)


app.run(host='0.0.0.0', port=5000)