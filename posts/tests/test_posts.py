from audioop import mul
from django.test import TestCase
from posts.models import Post
from posts.models import CoreUser
from posts.tests.posts_list import multiple_posts


class TestPost(TestCase):
    def setUp(self):
        user_data = {
            "password": "lolo2020",
            "email": "john.doe@mail.com",
            "first_name": "John",
            "last_name": "Doe"
        }
        self.user = CoreUser.objects.create(**user_data)


    def test_update_post_method(self):
        data = {
            "text": "Steve Spector",
            "publish_date": "2022-11-21T22:30:00Z",
            "to_publish": True,
            "was_published": False,
            "post_url": "",
            "user_id": self.user.id
        }

        post = Post.objects.create(**data)
        update_data = {
            "to_publish": False,
            "was_published": True,
            "post_url": "__post_url__",
            "task_id": "__second_task_id",
            "user_id": self.user.id
        }
        update_post = Post.objects.update_post(post, update_data)
        self.assertEqual(update_post.to_publish, update_data.get("to_publish"))
        self.assertEqual(update_post.was_published,
                         update_data.get("was_published"))
        self.assertEqual(update_post.post_url, update_data.get("post_url"))
        self.assertEqual(update_post.text, data.get("text"))
        self.assertEqual(update_post.task_id, update_data.get("task_id"))

    def test_remove_schedule_task(self):
        data = {
            "text": "Steve Spector",
            "publish_date": "2022-11-21T22:30:00Z",
            "to_publish": True,
            "was_published": False,
            "post_url": "",
            "task_id": "",
            "user_id": self.user.id
        }

        post = Post.objects.create(**data)
        self.assertEqual(post.text, data.get("text"))
        self.assertEqual(post.publish_date, data.get("publish_date"))
        Post.objects.delete_post(post.id)
        self.assertRaises(Post.DoesNotExist, Post.objects.get, id=post.id)
 
