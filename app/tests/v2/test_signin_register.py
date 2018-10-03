import unittest
import os
import json
from app import create_app
from ...api.v2.models.db import init_db_test

class Test_sign_up(unittest.TestCase):
    def setUp(self):
        self.app = create_app("testing")
        self.client = self.app.test_client()
        self.customer = {
          "username":"Gitonga",
          "email":"gabworks51@gmail.com",
          "password":"qwueuASS445",
          "confirm password":"qwueuASS445"
        }
        with self.app.app_context():
            self.db = init_db_test()

    def test_signup(self):
        response = self.client.post(
            '/api/v2/auth/signup', data=json.dumps(self.customer),
             content_type='application/json')
        self.assertEqual(response.status_code, 201)
    def test_sign(self):

