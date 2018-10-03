from flask_restful import Resource, reqparse
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
import re
import psycopg2
import psycopg2.extras
import datetime


# local imports
from ..models.db import db


class Users(Resource):
    """Class for Register and getting users"""
    parser = reqparse.RequestParser()

    parser.add_argument(
        'username',
        type=str,
        required=True,
        help="Username required"
    )
    parser.add_argument(
        'email',
        type=str,
        required=True,
        help="Email is required"
    )
    parser.add_argument(
        'password',
        type=str,
        required=True,
        help="Password is required"
    )
    parser.add_argument(
        'confirm password',
        type=str,
        required=True,
        help="Confirm password is required"
    )

    def post(self):
        """Creating a new user new user"""

        data = Users.parser.parse_args()

        email = data["email"]
        password = data["password"]
        confirm_password = data["confirm password"]

        if not email:
            return {'Message': 'Email field is required'}, 400
        if not password:
            return {'Message': 'Password field is required'}, 400

        while True:
            """Validating the email and password to match the specified creteria"""
            if not re.match(r"(^[a-zA-Z0-9_.-]+@[a-zA-Z-]+\.[a-zA-Z-]+$)", email):
                '''An valid email should have @ symbol and a dot before the @ symbol'''
                return {"Message": "Enter a valid email address"}, 400
            elif re.search('[a-z]', password) is None:
                '''password must atleast one small letter'''
                return {"Message": "Password should have atleast one small letter"}, 400
            elif re.search('[0-9]', password) is None:
                '''password must have atleast a number between 1 - 9'''
                return {"Message": "Password should have atleast one number in it"}, 400
            elif re.search('[A-Z]', password) is None:
                '''password must atleast one capital letter'''
                return {"Message": "Password should have atleast one capital letter"}, 400
            elif len(password) < 5:
                '''password lenth must be greater than 5 characters'''
                return {"Message": "Password should have atleast 5 characters long"}, 400
            elif password != confirm_password:
                return {"Message": "Passwords did not match"}, 400
            else:
                try:
                    conn = db()
                    cur = conn.cursor()

                    # check if user email exist
                    cur.execute("SELECT * FROM users WHERE email = %(email)s",
                                {'email': data["email"]})

                    if cur.fetchone() is not None:
                        return {'Message': 'User already exists'}, 400

                    # hash password
                    hashed_password = generate_password_hash(
                        data['password'], method='sha256')

                    cur.execute("INSERT INTO users (email, username, password) VALUES (%(email)s, %(username)s, %(password)s);", {
                        'email': data['email'], 'username': data['username'],'password': hashed_password})

                    conn.commit()

                    return {'Message': 'New user created'}, 201
                except (Exception, psycopg2.DatabaseError) as error:
                    cur.execute("rollback;")
                    print(error)
                    return {'Message': 'current transaction is aborted'}, 500


class Login(Resource):
    """docstring for Login"""

    parser = reqparse.RequestParser()

    parser.add_argument(
        'email',
        type=str,
        required=True,
        help="Make sure email is entered"
    )
    parser.add_argument(
        'password',
        type=str,
        required=True,
        help="Make sure password is entered"
    )

    def post(self):

        data = Login.parser.parse_args()
        password = data["password"]
        user_email = data["email"]
        valid_email = re.compile(
            r"(^[a-zA-Z0-9_.-]+@[a-zA-Z-]+\.[a-zA-Z-]+$)")

        if not user_email:
            return {'Message': 'Email field is required'}, 400
        if not password:
            return {'Message': 'Password field is required'}, 400

        while True:
            '''Validate user emails and password'''
            if not (re.match(valid_email, user_email)):
                return {"Message": "Make sure your email is valid"}, 400
            elif re.search('[a-z]', password) is None:
                return {"Message": "Password should have atleast one small letter in it"}, 400
            elif re.search('[0-9]', password) is None:
                return {"Message": "Password should have atleast one number in it"}, 400
            elif re.search('[A-Z]', password) is None:
                return {"Message": "Password should have atleast one capital letter in it"}, 400
            else:
                try:
                    conn = db()
                    cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

                    cur.execute("SELECT * FROM users WHERE email = %(email)s ",
                                {'email': user_email})
                    res = cur.fetchone()

                    if res is None:
                        return {'Message': 'User email does not exist'}, 404
                    else:
                        checked_password = check_password_hash(
                            res['password'], password)

                        if checked_password == True:
                            token = jwt.encode({'id': res['id'], 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60)}, 'secret')
                            return {'token': token.decode('UTF-8')}, 200

                        return {'Message': 'Invalid credentials'}, 400
                except (Exception, psycopg2.DatabaseError) as error:
                    cur.execute("rollback;")
                    print(error)
                    return {'Message': 'current transaction is aborted'}, 500