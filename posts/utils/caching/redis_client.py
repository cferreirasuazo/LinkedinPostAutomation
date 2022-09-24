import redis


class RedisClient():
    def __init__(self):
        pool = redis.ConnectionPool(host='redis', port=6379, db=0)
        self.client = redis.Redis(connection_pool=pool)

    def is_connected(self):
        return self.client.ping()

    def set_value(self, key, value, time_ms=None):
        if time_ms :
            return self.client.setex(name = key, time = time_ms, value = value)
        return self.client.set(key, value)

    def get_value(self, key):
        value =  self.client.get(key)
        if not value:
            return None
        return value.decode("utf-8")
            