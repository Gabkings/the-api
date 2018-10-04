from flask import Flask, request,jsonify
from flask_restful import Resource, reqparse
import psycopg2
from ..models.db import db
from .auth import check_auth
import jwt
from functools import wraps
class User_orders(Resource):
    @check_auth
    def get(user,self):
        """get all orders"""
        try:
            conn = db()
            cur = conn.cursor()
            cur.execute("SELECT * from orders")
            orders = cur.fetchall()
            order_list = []
            order_list.append(orders)
            return jsonify({"Orders": order_list})
        except (Exception, psycopg2.DatabaseError) as error:
            cur.execute("rollback;")
            print(error)
            return {'Message': 'current transaction is aborted'}, 500

    @check_auth
    def post(user,self):
        parser = reqparse.RequestParser(bundle_errors=True)

        parser.add_argument(
            'user_id',
            type=int,
            required=True,
            help="user id is required"
        )
        parser.add_argument(
            'name',
            type=str,
            required=True,
            help="name is required"
        )
        parser.add_argument(
            'price',
            type=float,
            required=True,
            help="passwprd is required"
        )
        parser.add_argument(
            'address',
            type=str,
            required=True,
            help="address is required"
        )

        data = parser.parse_args()
        user_id = data["user_id"]
        name = data["name"]
        price = data["price"]
        address = data["address"]

        try:
            conn = db()
            cur = conn.cursor()

            cur.execute("SELECT * FROM orders WHERE name = %(name)s",
                        {'name': data['name']})

            # check if order exist
            if cur.fetchone() is not None:
                return {'Message': 'order already exist'}
            cur.execute("INSERT INTO orders (user_id, name, price, address) VALUES (%(user_id)s, %(name)s, %(price)s, %(address)s);", {
                'user_id': data["user_id"], 'name': data["name"], 'price': data["price"],'address':data['address']})
            conn.commit()
            return {'Message': 'Order created successfully'}, 201
        except (Exception, psycopg2.DatabaseError) as error:
            cur.execute("rollback;")
            print(error)
            return {'Message': 'current transaction is aborted'}, 500

