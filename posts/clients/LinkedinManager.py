import os
from linkedin import linkedin


class LinkedinManager:
    def __init__(self):
        self.APPLICATON_KEY = os.environ.get('LINKEDIN_APPLICATON_KEY')
        self.APPLICATON_SECRET = os.environ.get("LINKEDIN_APPLICATON_SECRET")
        self.RETURN_URL = 'http://localhost:8000'
        self.PERMISSIONS = ['w_member_social', 'r_emailaddress', 'r_liteprofile']
        self.authentication = linkedin.LinkedInAuthentication(
            self.APPLICATON_KEY,
            self.APPLICATON_SECRET,
            self.RETURN_URL,
            self.PERMISSIONS
        )

    def get_oauth_url(self):
        return str(self.authentication.authorization_url)

    def set_authorization_code(self,code):
        self.authentication.authorization_code = code

    def get_access_token(self):
        result = self.authentication.get_access_token()
        access_token = {
            "access_token": result.access_token,
            "expires_in": result.expires_in
        }
        return access_token

