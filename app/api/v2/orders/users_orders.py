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
