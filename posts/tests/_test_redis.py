# from django.test import TestCase
# from posts.utils.caching.redis_client import RedisClient
# import time

# class TestRedisClient(TestCase):
#     def setUp(self):
#         self.cache_client = RedisClient()

#     def test_redis_connection(self):
#         self.assertTrue(self.cache_client.is_connected())

#     def test_set_value(self):
#         key = "cristhian-123456"
#         value = "here-is-a-value-to-store"
#         self.cache_client.set_value(key, value)
#         value_stored = self.cache_client.get_value(key)
#         self.assertEqual(value, value_stored)

#     def test_expire_token(self):
#         key = "cristhian-123456"
#         value = "here-is-a-value-to-remove"
#         expire_time = 3
#         self.cache_client.set_value(key, value, expire_time)
#         time.sleep(expire_time + 5)
#         self.assertEqual(self.cache_client.get_value(key), None)

