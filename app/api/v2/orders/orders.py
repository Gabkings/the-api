
from flask_jwt_extended import (
     jwt_required, create_access_token,
    get_jwt_identity
)
from flask import Flask, request, jsonify
from flask_restful import Resource, reqparse
import psycopg2
from ..models.db import db
from ..users.users import UserRole


class Orders(Resource):
    roles = UserRole()
    @jwt_required
    def get(self):
        id = get_jwt_identity()
        self.roles.role(id)
        """get all orders"""
        try:
            conn = db()
            cur = conn.cursor()
            cur.execute("SELECT * from orders")
            orders = cur.fetchall()
            if not orders:
                return {"message": "No orders available"}
            else:
                return jsonify({"Orders": orders})
        except (Exception, psycopg2.DatabaseError) as error:
            cur.execute("rollback;")
            print(error)
            return {'Message': 'current transaction is aborted'}, 500


class Specific_order_detail(Resource):
    roles = UserRole()
    @jwt_required
    def get(self, order_id):
        id = get_jwt_identity()
        self.roles.role(id)
        try:
            conn = db()
            cur = conn.cursor()
            cur.execute("SELECT * from orders WHERE order_id = order_id")
            orders = cur.fetchone()
            if not orders:
                return {"message":"No orders available"}
            else:
                return {"Orders": order_list}
        except (Exception, psycopg2.DatabaseError) as error:
            cur.execute("rollback;")
            print(error)
            return {'Message': 'current transaction is aborted'}, 500

    roles = UserRole()
    @jwt_required
    def put(self, order_id):
        id = get_jwt_identity()
        self.roles.role(id)
        parser = reqparse.RequestParser(bundle_errors=True)
        parser.add_argument(
        'status',
        type=str,
        required=True,
        help="Order status is required required"
        )

        data = parser.parse_args()
        order_status = data['status']
        order_stats = ['New','Processing',' Cancelled','Complete']
        if not order_status:
            return {"Message":"Status can not be empty.Please enter a value"}
        elif order_status not in order_stats:
            return {"Message":"Status can either be New,Processing,Cancelled,Complete"}
        else:
            try:
                conn = db()
                cur = conn.cursor()
                order = cur.execute("SELECT * FROM orders WHERE order_id = %(order_id)s", {"order_id":order_id})
                if not order:
                    return {"Message":"The order you are trying to update does not exists"}
                updt = cur.execute(
                    "UPDATE orders SET status = %(status)s WHERE order_id = %(order_id)s",{'status':order_status,'order_id':order_id})
                conn.commit()
                return {"message": "Order status has been updated successfully"}, 201

            except (Exception, psycopg2.DatabaseError) as error:
                cur.execute("rollback;")
                print(error)
    
    
                return {'Message': 'current transaction is aborted'}, 500
    
    roles = UserRole()
    @jwt_required
    def delete(self, order_id):
        id = get_jwt_identity()
        self.roles.role(id)
        try:

            conn = db()
            cur = conn.cursor()
            order = cur.execute("SELECT * FROM orders WHERE order_id = order_id")
            if not order:
                return {"message":"That order does not exists"}
            updt = cur.execute("DELETE FROM orders WHERE order_id = order_id")
            conn.commit()
            return {"message": "Order status has been deleted successfully"}, 200

        except (Exception, psycopg2.DatabaseError) as error:
            cur.execute("rollback;")
            print(error)
            return {'Message': 'current transaction is aborted'}, 500
