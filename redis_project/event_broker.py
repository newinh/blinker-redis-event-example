#from fakeredis import FakePubSub

# event_broker = FakePubSub()
# event_broker.subscribe('EVENT')

import redis

fredis = redis.Redis(
    host='localhost',
    port=6379)