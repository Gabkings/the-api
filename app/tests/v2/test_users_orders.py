import os
import json
import unittest
from app import create_app


class TestReg(unittest.TestCase):
    def setUp(self):
        self.app = create_app(config_stage="testing")
        self.clientVar = self.app.test_client

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
        response = json.loads(resp.data.decode('utf-8'))['access_token']
        return response

    def test_view_orders(self):
        resVar = self.clientVar().get(
        '/api/v2/users/orders',
        headers={
            "content-type": "application/json",
            "Authorization":"Bearer "+self.get_token()
        })
        res = json.loads(resVar.data.decode('utf-8'))
        self.assertEqual(resVar.status_code, 401)

    def test_view_orders_1(self):
        resVar = self.clientVar().get(
        '/api/v2/users/orders',
        headers={
            "content-type": "application/json",
        })
        res = json.loads(resVar.data.decode('utf-8'))
        self.assertEqual(resVar.status_code, 401)

    def test_view_orders1(self):
        resVar = self.clientVar().get(
        '/api/v2/users/orders',
        headers={
            "content-type": "application/json",
            "Authorization": self.get_token()
        })
        res = json.loads(resVar.data.decode('utf-8'))
        self.assertEqual(resVar.status_code, 401)

    def test_post_an_order(self):
        order = {
        "user_id":1,
        "name":"Rice Beans",
        "price":1234,
        "address":"vois 123 rood"
        }
        resp = self.clientVar().post(
            '/api/v2/users/orders',
            data=json.dumps(order),
            headers={
                "content-type": "application/json",
                "x-access-token": self.get_token()
            })
        response = json.loads(resp.data.decode('utf-8'))
        self.assertEqual(resp['Message'], 'Order created successfully')
        self.assertEqual(resp.status_code, 201)