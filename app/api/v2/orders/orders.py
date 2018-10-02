from flask import Flask, request,jsonify
from flask_restful import Resource,reqparse
import psycopg2
from ..models.db import db

class Orders(Resource):
    def get(self):
        """get all orders"""
        try:
            conn = db()
            cur = conn.cursor()
            cur.execute("SELECT * from orders")
            orders = cur.fetchall()
            if orders is None:
                return {"message":"No orders available"}
            else:
                return {"Orders": orders}
        except (Exception, psycopg2.DatabaseError) as error:
            cur.execute("rollback;")
            print(error)
            return {'Message': 'current transaction is aborted'}, 500