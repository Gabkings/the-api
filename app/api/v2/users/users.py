from flask import Flask, request
from flask_restful import Resource,reqparse
import psycopg2
from ..models.db import db
import jwt
import datetime



class Users(Resource):
    def get(self):
        """get all orders"""
        try:
            conn = db()
            cur = conn.cursor()
            cur.execute("SELECT * from users")
            users = cur.fetchall()
            user_list = []
            user_list.append(users)
            print(user_list)
            print(users)

            return {"Users": user_list}
        except (Exception, psycopg2.DatabaseError) as error:
            cur.execute("rollback;")
            print(error)
            return {'Message': 'current transaction is aborted'}, 500
        
    def post(self):
        parser = reqparse.RequestParser(bundle_errors=True)

        parser.add_argument(
            'name',
            type=str,
            required=True,
            help="name is required"
        )
        parser.add_argument(
            'email',
            type=str,
            required=True,
            help="email is required"
        )
        parser.add_argument(
            'password',
            type=str,
            required=True,
            help="passwprd is required"
        )
        parser.add_argument(
            'type',
            type=str,
            required=True,
            help="Type is required"
        )
        data = parser.parse_args()
        name = data["name"]
        email = data["email"]
        password = data["password"]
        u_type = data["type"]

        try:
            conn = db()
            cur = conn.cursor()

            cur.execute("SELECT * FROM users WHERE username = %(name)s",
                        {'name': data['name']})

            # check if order exist
            if cur.fetchone() is not None:
                return {'Message': 'Users already exist'}
            cur.execute("INSERT INTO users (username, email, password, type) VALUES (%(username)s, %(email)s, %(password)s, %(type)s);", {
                'username': data["name"], 'email': data["email"], 'password': data["password"], 'type': data['type']})
            conn.commit()
            return {'Message': 'User created successfully'}, 201
        except (Exception, psycopg2.DatabaseError) as error:
            cur.execute("rollback;")
            print(error)
            return {'Message': 'current transaction is aborted'}, 500
class Login(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument(
            'username',
            type=str,
            required=True,
            help="username is required"
        )
        parser.add_argument(
            'password',
            type=str,
            required=True,
            help="password is required"
        )  

        data = parser.parse_args()
        name = data["username"]
        password = data["password"]

        try:
            conn = db()
            cur = conn.cursor()

            cur.execute("SELECT * FROM users WHERE username = %(name)s AND password = %(password)s",
                        {'name': data['username'],'password': data['password']})

            # check if order exist
            usr = cur.fetchone()
            if usr is None:
                return {'Message': 'Users does not exist'}
            else:
                token = jwt.encode({'id': usr[0], 'exp': datetime.datetime.utcnow(
                ) + datetime.timedelta(minutes=30)}, 'secret')
                return {'token': token.decode('UTF-8')}
            return {'Message': 'User loged in'}, 201
        except (Exception, psycopg2.DatabaseError) as error:
            cur.execute("rollback;")
            print(error)
            return {'Message': 'current transaction is aborted'}, 500

