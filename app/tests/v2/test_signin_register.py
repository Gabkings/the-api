# import unittest
# import os
# import sys
# import json
# sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# from app import create_app
# from ..api.v2.models.db import test_db,init_db

# class Test_signin_register(unittest.TestCase):
#     def setUp(self):
#         self.app = create_app("testing")
#         self.client = self.app.test_client()
#         self.app_context = self.app.app_context()
#         self.con = test_db()
#         # self.cur = self.connection.cursor()
#         with self.app.app_context():
#             init_db()




#         self.create_user = json.dumps(dict(
#                 name="Gabriel222",
#                 email="gabworks23@gmail.com",
#                 password='mchelejpgAAA22'))        

#     def create_user(self):
#         res = self.client.post(
#         "/api/v2/auth/signup",
#         data=json.dumps(self.create_user),content_type="aplication/json")
#         self.assertEqual(res.status_code, 201)

#         # self.login = data=json.dumps(dict(email="gabworks23@gmail.com", password='Gabbs122'))
#         #         self.client = app.test_client()

#         # self.signupuser = self.client.post(
#         #    'api/v2/auth/signup',
#         #    data=self.register_user,
#         #    content_type='application/json')

#         # self.client.post(
#         #    '/v2/auth/login',
#         #    data=self.login,
#         #    content_type='application/json')

#     # def test_create_menu(self):
#     #   res= self.client.post("/api/v2/menu",
#     #   data= {"name":"Mchele","price":123,"description":"sweet mchele"},headers ={'x-access-token':'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MywiZXhwIjoxNTM4NTU3NzI4fQ.UOsqvoOcBCSDQT1UuuaAN74B6VzkioWluSKhz2vjiM4'})
#     #   self.assertEqual(res.status_code,201)
#     def test_registration(self):
#         with self.client():
#             response = self.register_user(username='tester',
#                                           email='test@gmail.com',
#                                           password='tesAAt1234',
#                                           confirm_password='tesAAt1234')
#             data = json.loads(response.data.decode())
#             self.assertIn('test@gmail.com', str(response.data))
#             # self.assertIsNotNone(User.find_by_email('test@gmail.com'))
#             # self.assertIsNotNone(User.find_by_id(1))
#             self.assertTrue(data['status'] == 'User Created')
#             self.assertTrue(data['message'] == u"User test@gmail.com successfully registered.")
#             self.assertFalse(data['message'] == u"User successfully registered")
#             self.assertTrue(response.content_type == 'application/json')
#             self.assertEqual(response.status_code, 201)
#             self.assertNotEqual(response.status_code, 200)







