import os
import json
import unittest
from app import create_app


class TestReg(unittest.TestCase):
    def setUp(self):
        self.app = create_app(config_stage="testing")
        self.clientVar = self.app.test_client

    def test_view_orders(self):
        resVar = self.clientVar().get(
        '/api/v2/orders',
        content_type='application/json')
        res = json.loads(resVar.data.decode('utf-8'))
        self.assertEqual(resVar.status_code, 200)

    def test_view_spec_order(self):
        resVar = self.clientVar().get(
        '/api/v2/orders/1',
        content_type='application/json')
        print(resVar)
        res = json.loads(resVar.data.decode('utf-8'))
        self.assertEqual(resVar.status_code, 200)

    def test_update_spec_order(self):
        resVar = self.clientVar().put(
        '/api/v2/orders/1',
        content_type='application/json')
        res = json.loads(resVar.data.decode('utf-8'))
        self.assertEqual(resVar.status_code, 201)

    def test_delete_spec_order(self):
        resVar = self.clientVar().delete(
        '/api/v2/orders/1',
        content_type='application/json')
        res = json.loads(resVar.data.decode('utf-8'))
        self.assertEqual(resVar.status_code, 200)