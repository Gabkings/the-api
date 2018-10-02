from flask import Flask, request,jsonify
from flask_restful import Resource,reqparse
import psycopg2
from ..models.db import db
from ..users.auth import check_auth

class Meals(Resource):
    def get(self):
        """get all orders"""
        try:
            conn = db()
            cur = conn.cursor()
            cur.execute("SELECT * from meals")
            meals = cur.fetchall()
            return jsonify({"Meals": meals}, 200)
        except (Exception, psycopg2.DatabaseError) as error:
            cur.execute("rollback;")
            print(error)
            return {'Message': 'current transaction is aborted'}, 500
        
    @check_auth
    def post(user, self):
        parser = reqparse.RequestParser(bundle_errors=True)

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
            help="price is required"
        )
        parser.add_argument(
            'description',
            type=str,
            required=True,
            help="passwprd is required"
        )

        data = parser.parse_args()
        name = data["name"]
        email = data["price"]
        password = data["description"]

        try:
            conn = db()
            cur = conn.cursor()

            cur.execute("SELECT * FROM meals WHERE name = %(name)s",
                        {'name': data['name']})

            # check if order exist
            if cur.fetchone() is not None:
                return {'Message': 'meal already exist'}
            cur.execute("INSERT INTO meals (name, price, description) VALUES (%(name)s, %(price)s, %(description)s);", {
                'name': data["name"], 'price': data["price"], 'description': data["description"]})
            conn.commit()
            return {'Message': 'Meal created successfully'}, 201
        except (Exception, psycopg2.DatabaseError) as error:
            cur.execute("rollback;")
            print(error)
            return {'Message': 'current transaction is aborted'}, 500