from flask import Flask, request
from flask_restful import Resource,reqparse
import psycopg2
from ..models.db import db

class Categories(Resource):
    def get(self):
        """get all orders"""
        try:
            conn = db()
            cur = conn.cursor()
            cur.execute("SELECT * from categories")
            category = cur.fetchall()
            cart_list = []
            cart_list.append(users)
            return {"Users": cart_list}
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
        data = parser.parse_args()
        name = data["name"]
        try:
            conn = db()
            cur = conn.cursor()

            cur.execute("SELECT * FROM categories WHERE username = %(name)s",
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

