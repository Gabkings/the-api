import os
import json
import unittest
from app import create_app


class TestReg(unittest.TestCase):
    def setUp(self):
        self.app = create_app(config_stage="testing")
        self.clientVar = self.app.test_client

    def test_view_meals(self):
        resVar = self.clientVar().get(
        '/api/v2/menu',
        content_type='application/json')
        res = json.loads(resVar.data.decode('utf-8'))
        self.assertEqual(resVar.status_code, 200)

    def get_token(self):
        user_data = {
            "email": "gs@gmail.com",
            "password": "asdAAA12"
        }
        resp = self.clientVar().post(
            '/api/v2/auth/login',
            data=json.dumps(user_data),
            content_type='application/json'
        )
        print(resp)
        response = json.loads(resp.data.decode('utf-8'))['access_token']
        return response

    def test_view_meals(self):
        resVar = self.clientVar().get(
        '/api/v2/menu',
        content_type='application/json')
        res = json.loads(resVar.data.decode('utf-8'))
        self.assertEqual(resVar.status_code, 200)

    def user_post_a_meal(self):
        meal = {
            "name": "Ugali122",
            "price": 222.00,
            "description": "Hot ugali"
        }
        resp = self.clientVar().post(
            '/api/v2/menu',
            data=json.dumps(meal),
            headers={
                "content-type": "application/json",
                "Authorization": "Bearer" + self.get_token()
            })
        response = json.loads(resp.data.decode('utf-8'))
        self.assertEqual(resp['Message'], 'Meal created successfully')
        self.assertEqual(resp.status_code, 201)