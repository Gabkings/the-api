from flask_restful import Resource, reqparse
import psycopg2
import psycopg2.extras
from functools import wraps
from ..models.db import db

class Food(Resource):
    '''getting all the meals available and create new meals'''
    def get(self):
        '''Return all the meals in the database'''

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
            return {'Message': 'current transaction is aborted'}, 500