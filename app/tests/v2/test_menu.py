import os 
import json
import unittest
from app import create_app


class TestReg(unittest.TestCase):
    def setUp(self):
        self.app = create_app(config_stage="testing")
        self.clientVar = self.app.test_client



    def test_register(self):
        user = {
        "username":"122gabriel",
        "email":"gs@gmail.com",
        "password":"asdAAA12",
        "confirm password":"asdAAA12"
        }
        resVar = self.clientVar().post(
            '/api/v2/auth/signup',
            data=json.dumps(user),
            content_type= 'application/json'
        )
        resp = json.loads(resVar.data.decode('utf-8'))
        self.assertEqual(resp['Message'],'New user created')
        self.assertEqual(resVar.status_code,201)

    def get_token(self):
        user_data = {
        "email":"gs@gmail.com",
        "password":"asdAAA12"
        }
        resp = self.clientVar().post(
            '/api/v2/auth/login',
            data=json.dumps(user_data),
            content_type='application/json'
            )
        response = json.loads(resp.data.decode('utf-8'))['token']
        return response
    def user_post_a_meal(self):
        meal = {
        "name": "Ugali",
        "price": 22.00,
        "description": "Hot ugali"
        }
        resp = self.clientVar().post(
            '/api/v2/menu',
            data=json.dumps(meal),
            headers={
            "content-type":"application/json",
            "x-access-token": self.get_token()
            })
        response = json.loads(resp.data.decode('utf-8'))
        self.assertEqual(resp['Message'], 'Meal created successfully')
        self.assertEqual(resp.status_code, 201)

    def use_get_a_meal(self):
        resp = self.clientVar().get(
            '/api/v2/menu',
            data=json.dumps(meal),
            headers={
            "content-type":"application/json"
            })
        response = json.loads(resp.data.decode('utf-8'))
        self.assertEqual(resp.status_code,200)

    def test_exists_user(self):
        user = {
        "username":"gabriel",
        "email":"gabr@gmail.com",
        "password":"asdAAA12",
        "confirm password":"asdAAA12"
        }
        resVar = self.clientVar().post(
            '/api/v2/auth/signup',
            data=json.dumps(user),
            content_type= 'application/json'
        )
        resp = json.loads(resVar.data.decode('utf-8'))
        self.assertEqual(resp['Message'],'User already exists')
        self.assertEqual(resVar.status_code,400)

    def test_empty_email(self):
        user = {
        "username":"gabriel",
        "email":"",
        "password":"asdAAA12",
        "confirm password":"asdAAA12"
        }
        resVar = self.clientVar().post(
            '/api/v2/auth/signup',
            data=json.dumps(user),
            content_type= 'application/json'
        )
        resp = json.loads(resVar.data.decode('utf-8'))
        self.assertEqual(resp['Message'],'Email field is required')
        self.assertEqual(resVar.status_code,400)

    def test_password_dont_match(self):
        user = {
        "username":"qqwgabriel",
        "email":"gabrss@gmail.com",
        "password":"asdAAA12",
        "confirm password":"dAAA12"
        }
        resVar = self.clientVar().post(
            '/api/v2/auth/signup',
            data=json.dumps(user),
            content_type= 'application/json'
        )
        resp = json.loads(resVar.data.decode('utf-8'))
        self.assertEqual(resp['Message'],'Passwords did not match')
        self.assertEqual(resVar.status_code,400)

    def test_password_less_5(self):
        user = {
        "username":"qqwgabriel",
        "email":"gabrss@gmail.com",
        "password":"Aa12",
        "confirm password":"A12"
        }
        resVar = self.clientVar().post(
            '/api/v2/auth/signup',
            data=json.dumps(user),
            content_type= 'application/json'
        )
        resp = json.loads(resVar.data.decode('utf-8'))
        self.assertEqual(resp['Message'],'Password should have atleast 5 characters long')
        self.assertEqual(resVar.status_code,400)

    def test_password_small_letter(self):
        user = {
        "username":"qqwgabriel",
        "email":"gabrss@gmail.com",
        "password":"A12",
        "confirm password":"A12"
        }
        resVar = self.clientVar().post(
            '/api/v2/auth/signup',
            data=json.dumps(user),
            content_type= 'application/json'
        )
        resp = json.loads(resVar.data.decode('utf-8'))
        self.assertEqual(resp['Message'],'Password should have atleast one small letter')
        self.assertEqual(resVar.status_code,400)

    def test_password_capital_letter(self):
        user = {
        "username":"qqwgabriel",
        "email":"gabrss@gmail.com",
        "password":"qqw12",
        "confirm password":"qwqq12"
        }
        resVar = self.clientVar().post(
            '/api/v2/auth/signup',
            data=json.dumps(user),
            content_type= 'application/json'
        )
        resp = json.loads(resVar.data.decode('utf-8'))
        self.assertEqual(resp['Message'],'Password should have atleast one capital letter')
        self.assertEqual(resVar.status_code,400)

    def test_valid_email(self):
        user = {
        "username":"qqwgabriel",
        "email":"gabrgmacom",
        "password":"qqw12",
        "confirm password":"qq12"
        }
        resVar = self.clientVar().post(
            '/api/v2/auth/signup',
            data=json.dumps(user),
            content_type= 'application/json'
        )
        resp = json.loads(resVar.data.decode('utf-8'))
        self.assertEqual(resp['Message'],'Enter a valid email address')
        self.assertEqual(resVar.status_code,400)


    def test_exists_user(self):
        user = {
        "username":"gabriel",
        "email":"gabr@gmail.com",
        "password":"",
        "confirm password":"asdAAA12"
        }
        resVar = self.clientVar().post(
            '/api/v2/auth/signup',
            data=json.dumps(user),
            content_type= 'application/json'
        )
        resp = json.loads(resVar.data.decode('utf-8'))
        self.assertEqual(resp['Message'],'Password field is required')
        self.assertEqual(resVar.status_code,400)