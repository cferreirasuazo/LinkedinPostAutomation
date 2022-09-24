import resource
from django.test import TestCase
from accounts.models import CoreUser
from posts.models import Post
from unittest import skipIf

from datetime import datetime, timedelta
import time
import json
from posts.tests.posts_list import multiple_posts

from rest_framework.test import APITestCase
# Create your tests here.

from django.urls import reverse

class TestUserSession(APITestCase):
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


    # def test_user_session(self):

    #     for post in multiple_posts:
    #         create_post_request = self.client.post(self.api_post_url, post, format="json")
    #         self.assertEqual(create_post_request.status_code, 201)
    #         post_response = create_post_request.json()
    #         self.assertEqual(post_response.get("text"), post.get("text"))
        
    #     get_all_posts = self.client.get(self.api_post_url)
    #     self.assertEqual(get_all_posts.status_code, 200)
    #     get_all_posts_response = get_all_posts.json()
    #     self.assertEqual(len(get_all_posts_response), len(multiple_posts))







# Test register
# test login
# test create multiple post with multiple status and dates
# retrieve multiple posts
# test make sure a date is not valid
# test InvalidLinkedinTokenException
# test InvalidateDate

# test delete post with its schedule task

# OJO !!!  Revisar ese maco de que hay posts duplicados !!!

# Test user session
#
# 1 - Register
# 2 - Login
# 3 - Schedule 4 posts
# 4 - get posts
# 4 - change status of post to be schedule
# 5 - remove schedule of post
# 6 -
#
#
#
