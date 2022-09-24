from urllib import request, response
import requests
import json
from enum import Enum


USER_PROFILE = "https://api.linkedin.com/v2/me"
SHARE_POST = "https://api.linkedin.com/v2/ugcPosts"
DELETE_RESOURCE = "https://api.linkedin.com/v2/shares/{share_id}"


def replace_share_id(share_id):
    str = "{share_id}"
    delete_url = DELETE_RESOURCE.replace(str,share_id)
    return delete_url


class LinkedinApiClient():
    def __init__(self, client_token):
        self.headers = self.make_headers(client_token)

    def make_headers(self, client_token):
        headers = {
            'Authorization': 'Bearer ' + client_token,
            'Content-Type': 'application/json',
            "X-Restli-Protocol-Version": "2.0.0"
        }

        return headers

    def delete_resource(self, resource_id):
        delete_url = ""
        response = requests.delete(delete_url, headers=self.headers)

    def make_post_body(self, user_id, text):
        body = {
            "author": "urn:li:person:" + user_id,
            "lifecycleState": "PUBLISHED",
            "specificContent": {
                "com.linkedin.ugc.ShareContent": {
                    "shareCommentary": {
                        "text": text
                    },
                    "shareMediaCategory": "NONE"
                }
            },
            "visibility": {
                "com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"
            }
        }

        return body

    def get_request(self, url):
        response = requests.get(url, headers=self.headers)
        return response

    def get_profile(self):
        response = self.get_request(USER_PROFILE)
        return response


    def get_user_id(self):
        response = self.get_profile()
        content = response.json()
        return content.get("id")

    def share_post(self, text):
        user_id = self.get_user_id()
        body = self.make_post_body(user_id, text)
        response = requests.post(SHARE_POST, data= json.dumps(body), headers=self.headers)
        return response


