import unittest
import os
import json
from app import create_app


class Test_signin_register(unittest.TestCase):
    def setUP(self):
        self.app = create_app("testing")
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()

        self.create_user = json.dumps(dict(
                name="Gabriel222",
                email="gabworks23@gmail.com",
                password='mchelejpg'))
        self.login = data=json.dumps(dict(username="Gabriel222", password='mchelejpg'))
                self.client = app.test_client()

        self.signupuser = self.client.post(
           'api/v2/auth/signup',
           data=self.register_user,
           content_type='application/json')

        self.client.post(
           '/v2/auth/login',
           data=self.login,
           content_type='application/json')

    def test_create_user(self):






