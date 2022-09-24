from django.test import TestCase
from rest_framework.test import APITestCase
from django.urls import reverse
from accounts.models import CoreUser
from api.tests.posts_list import multiple_posts
# Create your tests here.



class TestAPIEndpoints(APITestCase):
    def setUp(self):
        self.user = {
            "password": "lolo2020",
            "email": "wayne@mail.com",
            "first_name": "Bruce",
            "last_name": "Wayne"
        }

        self.single_post = {
            "text": "Steve Spector",
            "publish_date": "2022-10-21T22:30:00Z",
            "to_publish": False,
            "was_published": False,
            "post_url": ""
        }

        self.user_login = {
            "email": "wayne@mail.com",
            "password": "lolo2020"
        }

        self.user_signup_url = reverse("signup-user")
        self.user_signin_url = reverse("signin-user")
        self.api_post_url = "/api/posts/"

    def test_register_login(self):
        user_signup_request = self.client.post(
            self.user_signup_url, self.user, format="json")
        signup_response = user_signup_request.json()
        self.assertEqual(user_signup_request.status_code, 201)
        self.assertEqual(signup_response.get(
            "email"), self.user.get("email"))
        signin_response = self.client.post(self.user_signin_url, data=self.user_login)
        self.assertEqual(signin_response.status_code, 200)
        user = signin_response.json()
        self.assertEqual(user.get("email"), self.user.get("email"))


    def test_get_user_posts(self):
        user = CoreUser.objects.create(**self.user)
        
        for post in multiple_posts:
            post["user"] = user.id
            create_post_request = self.client.post(self.api_post_url, post, format="json")
            self.assertEqual(create_post_request.status_code, 201)
            post_response = create_post_request.json()
            self.assertEqual(post_response.get("text"), post.get("text"))

        url = f'/api/users/{user.id}/posts'

        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, 200)