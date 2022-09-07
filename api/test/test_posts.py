from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework import status

import json

class TestPosts(APITestCase):
    def test_get_posts(self):
        url = "/api/posts/"
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_post(self):
        data = {
            "text": "Steve Spector",
            "publish_date": "2022-10-21T22:30:00Z",
            "to_publish": True,
            "was_published": False,
            "post_url": ""
        }

        post_response = self.client.post("/api/posts/", data)
        post = json.loads(post_response.content)
        self.assertEqual(post_response.status_code, 201)
        self.assertEqual(post.get("text"), data.get("text"))
        self.assertEqual(post.get("to_publish"), data.get("to_publish"))
        self.assertEqual(post.get("was_published"), data.get("was_published"))
        self.assertEqual(post.get("post_url"), data.get("post_url"))
