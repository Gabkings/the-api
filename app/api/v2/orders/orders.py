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
                return jsonify({"Orders": orders})
        except (Exception, psycopg2.DatabaseError) as error:
            cur.execute("rollback;")
            print(error)
            return {'Message': 'current transaction is aborted'}, 500

class Specific_order_detail(Resource):
    def get(self,order_id):
        try:
            conn = db()
            cur = conn.cursor()
            cur.execute("SELECT * from orders WHERE order_id = order_id")
            orders = cur.fetchone()
            order_list = []
            order_list.append(orders)
            if len(order_list) < 1:
                return {"message":"No orders available"}
            else:
                return jsonify({"Orders": order_list})
        except (Exception, psycopg2.DatabaseError) as error:
            cur.execute("rollback;")
            print(error)
            return {'Message': 'current transaction is aborted'}, 500
        
    def put(self,order_id):
        try:
            conn = db()
            cur = conn.cursor()
            updt = cur.execute("UPDATE orders SET status = 'Completed' WHERE order_id = order_id;")
            conn.commit()
            return {"message":"Order status has been updated successfully"}

        except (Exception, psycopg2.DatabaseError) as error:
            cur.execute("rollback;")
            print(error)
            return {'Message': 'current transaction is aborted'}, 500
    def delete(self,order_id):
        try:

            conn = db()
            cur = conn.cursor()
            updt = cur.execute("DELETE FROM orders WHERE order_id = order_id")
            conn.commit()
            return {"message":"Order status has been updated successfully"}

        except (Exception, psycopg2.DatabaseError) as error:
            cur.execute("rollback;")
            print(error)
            return {'Message': 'current transaction is aborted'}, 500