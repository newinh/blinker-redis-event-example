import redis

event_broker = redis.Redis(host='localhost', port=6379)
