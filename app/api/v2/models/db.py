from contextlib import closing
# from flask import current_app
import psycopg2
import os
# from app import create_app

#local imports
from .tables import queries

def db():
    url = os.environ.get('DATABASE_URL')
    conn = psycopg2.connect(url)
    # print(db_url)
    # conn = psycopg2.connect(db_url)
    return conn





def init_db():

    try:
        connection = db()
        connection.autocommit = True

        # activate connection cursor
        cur = connection.cursor()
        for query in queries:
            cur.execute(query)
        connection.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print("Database not connected")
        print(error)

   
