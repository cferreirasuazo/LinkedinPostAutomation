# from django.test import TestCase
# from posts.clients.LinkedinApiClient import LinkedinApiClient

# class TestLinkedinApiClient(TestCase):
#     def setUp(self):
#         self.LocalizedFirstName = "Cristhian Antonio"
#         token = "AQUWW05rac1IvWHXKn00GuTPTR2BzqIatCCK-CNyI1Z8kX3k5JduQ3743LaElP_qt9oOcr3ZVhdEGuWxp12m5FbgtOTAUdaoPNFCdHHPLG_kHib8zu0rz6Yg9I7ZrvPeLwQr9VbaAg0cWCyVHbVQxBrOgTYBgu2qTTtq3KEM4v1sXJvYqHjQr3LDaR279xUl5F1yQAeHpNkV4YjBm6pJXMbf5PiXi8h-WY6EFQQptjU4ApGSRTbXuX-oV88GNsPyzfd7suoPJANe0JbVdvcRvC2yyXIuFqY7Ppz_TP3YLZGd7wWOxB23lUPbUD1-8Bmb8jdDppuerQ_XqitiWzmhahmDAlhC6A"
#         self.api_client = LinkedinApiClient(client_token=token)
#         self.text = "Lorem adipiscing elitmattis, enim commodo fringilla nullam velit habitasse. Ut nunc facilisi nullam dictum senectus maecenas sociis augue, tempor blandit velit dapibus bibendum phasellus habitasse ridiculus hac, turpis cubilia eleifend sollicitudin ornare luctus neque. Sagittis vehicula praesent duis justo bibendum quam posuere, nunc dui in vulputate sed vestibulum."

#     def test_get_user(self):
#         response = self.api_client.get_profile()
#         content = response.json()
#         self.assertEqual(self.LocalizedFirstName, content.get("localizedFirstName"))
#         self.assertEqual(response.status_code, 200)

#     def test_publish_post(self):
#         response = self.api_client.share_post(self.text)
#         print(response.json())
#         self.assertEqual(response.status_code, 201)