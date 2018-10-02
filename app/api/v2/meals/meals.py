from flask_restful import Resource, reqparse
import psycopg2
import psycopg2.extras
from functools import wraps
from ..models.db import db
from ..users.auth import auth_func

class Food(Resource):
    '''getting all the meals available and create new meals'''
    parser = reqparse.RequestParser()

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
        help="Price is required"
    )
    parser.add_argument(
        'description',
        type=str,
        required=True,
        help="Description is required"
    )
    def get(self):
        '''Return all the meals in the food_detailbase'''

        try:
            conn = db()
            cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
            cur.execute("SELECT * from meals")
            food = cur.fetchall()

            if not food:
                return {"Food": "No availabe food for now"}, 404

            return {"Food": food}
        except (Exception, psycopg2.DatabaseError) as error:
            cur = conn.cursor()
            cur.execute("rollback;")
            print(error)
            return {'message': 'current transaction is aborted'}, 500

    @auth_func
    def post(user,self):
        """add a food item"""
        # if current_user["type"] != "admin":
        #     return {"message": "You are not permitted to view this endpoint"}

        food_detail = Food.parser.parse_args()
        item = food_detail["name"]
        price = food_detail["price"]
        description = food_detail["description"]

        if not item:
            return {'message': 'Food item field is required'}, 400
        if not price:
            return {'message': 'Price field is required'}, 400
        if not description:
            return {'message': 'Description field is required'}, 400

        try:
            conn = db()
            cur = conn.cursor()

            cur.execute("SELECT * FROM meals WHERE name = %(name)s",
                        {'name': food_detail['name']})
            row = cur.fetchone()
            #check if food exists
            if row :
                return {'message': 'Food already exist'}
            cur.execute("INSERT INTO meals (name, price, description) VALUES (%(name)s, %(price)s, %(description)s);", {
                'name': food_detail["name"], 'price': food_detail["price"], 'description': food_detail["description"]})
            conn.commit()
            return {'message': 'Food created successfully'}, 201
        except (Exception, psycopg2.DatabaseError) as error:
            cur.execute("rollback;")
            print(error)
            return {'message': 'current transaction is aborted'}, 500