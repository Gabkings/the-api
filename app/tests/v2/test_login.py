import os 
import json
import unittest
from app import create_app

class TestLogin(unittest.TestCase):
    def setUp(self):
        self.app = create_app(config_stage="testing")
        self.clientVar = self.app.test_client

    def test_login(self):
        user = {
        "password":"",
        "email":"gs@gmail.com"
        }
        resVar = self.clientVar().post(
            '/api/v2/auth/login',
            data=json.dumps(user),
            content_type= 'application/json'
        )
        resp = json.loads(resVar.data.decode('utf-8'))
        self.assertEqual(resp['Message'],'Password field is required')
        self.assertEqual(resVar.status_code,400)

    def test_login(self):
        user = {
        "email": "",
        "password":"gsllgmail.com"
        }
        resVar = self.clientVar().post(
            '/api/v2/auth/login',
            data=json.dumps(user),
            content_type= 'application/json'
        )
        resp = json.loads(resVar.data.decode('utf-8'))
        self.assertEqual(resp['Message'],'Email field is required')
        self.assertEqual(resVar.status_code,400)