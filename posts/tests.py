from django.test import TestCase
from posts.models import Post
# Create your tests here.


class TestPost(TestCase):
    def test_update_post_method(self):
        data = {
            "text": "Steve Spector",
            "publish_date": "2022-10-21T22:30:00Z",
            "to_publish": True,
            "was_published": False,
            "post_url": "",
            "task_id": "__first_task_id"
        }

        post = Post.objects.create(**data)
        update_data = {
            "id": post.id,
            "to_publish": False,
            "was_published": True,
            "post_url": "__post_url__",
            "task_id": "__second_task_id"
        }
        update_post = Post.objects.update_post(update_data)
        self.assertEqual(update_post.to_publish, update_data.get("to_publish"))
        self.assertEqual(update_post.was_published,
                         update_data.get("was_published"))
        self.assertEqual(update_post.post_url, update_data.get("post_url"))
        self.assertEqual(update_post.text, data.get("text"))
        self.assertEqual(update_post.task_id, update_data.get("task_id"))
