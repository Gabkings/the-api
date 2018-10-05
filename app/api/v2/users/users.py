from flask import Flask, jsonify, request, abort
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)
from flask_restful import Resource, reqparse
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
import re
import psycopg2
import psycopg2.extras
import datetime


# local imports
from ..models.db import db


class UserRole():
    
    def role(self, user_id):
        """Get user role"""
        con = db()
        cur = con.cursor()
        
        # check if user email exist 
        cur.execute( "SELECT type FROM users WHERE email = %(email)s", {'email': user_id})
        user = cur.fetchall()
        print (user_id)
        if user[0][0] != "Admin":
            abort(401, "You are not admin: You are can't access that root")


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
        try:
            if data['username'] == "":
                return {"Message":"Username cannot be empty"}
            elif data['email'] == "":
                return {"message":"Email cannot be empty"}
            elif data['password'] == "":
                return {"Message":"Password cannot be empty"}
            elif data['confirm password'] == "":
                return {"message":"Confirm password cannot be empty"} 
        except(Exception):
            print("Something is wrong with the")

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
                        'email': data['email'], 'username': data['username'], 'password': hashed_password})

                    conn.commit()

                    return {'Message': 'New user created'}, 201
                except (Exception, psycopg2.DatabaseError) as error:
                    cur.execute("rollback;")
                    print(error)
                    return {'Message': 'current transaction is aborted'}, 500
    roles = UserRole()
    @jwt_required
    def get(self):
        id = get_jwt_identity()
        self.roles.role(id)
        """get all users"""
        try:
            conn = db()
            cur = conn.cursor()
            cur.execute("SELECT * from users")
            orders = cur.fetchall()
            if not orders:
                return {"message": "No users registered"}
            else:
                return jsonify({"Userss": orders})
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
                    cur = conn.cursor(
                        cursor_factory=psycopg2.extras.RealDictCursor)

                    cur.execute("SELECT * FROM users WHERE email = %(email)s ",
                                {'email': user_email})
                    res = cur.fetchone()

                    if res is None:
                        return {'Message': 'User email does not exist'}, 404
                    else:
                        checked_password = check_password_hash(
                            res['password'], password)

                        print(checked_password)
                        if checked_password == True:
                            token = create_access_token(identity=res['email'])
                            return {"message":"login succeeded", "access_token":token}, 200
                        return {'Message': 'Invalid credentials'}, 400
                except (Exception, psycopg2.DatabaseError) as error:
                    cur.execute("rollback;")
                    print(error)
                    return {'Message': 'current transaction is aborted'}, 500
                    


class Updates_users_status(Resource):
    """docstring for Updates_users_status" def __init__(self, arg):
        super(Updates_users_status,.__init__()
        self.arg = arg"""

    roles = UserRole()
    @jwt_required
    def get(self,user_id): 
        id = get_jwt_identity()
        self.roles.role(id)
        try:
            conn = db()
            cur = conn.cursor()
            cur.execute("SELECT * from users WHERE id =  %(id)s", {'id': user_id})
            user = cur.fetchone()
            if not user:
                return {"message":"There are no currently users available"}
            return {"Orders": user}
        except (Exception, psycopg2.DatabaseError) as error:
            cur.execute("rollback;")
            print(error)
            return {'Message': 'current transaction is aborted'}, 500
    roles = UserRole()
    @jwt_required
    def put(self,user_id):
        id = get_jwt_identity()
        self.roles.role(id)
        user_id = get_jwt_identity()
        UserRole().role(user_id)
        try:
            conn = db()
            cur = conn.cursor()
            cur.execute(
                "UPDATE users SET type = 'Admin' WHERE email =  %(email)s", {'email': user_id})
            conn.commit()
            return {"message": "User has been promoted  successfully"}, 201

        except (Exception, psycopg2.DatabaseError) as error:
            cur.execute("rollback;")
            print(error)
            return {'Message': 'current transaction is aborted'}, 500
    roles = UserRole()
    @jwt_required
    def delete(self,user_id):
        id = get_jwt_identity()
        self.roles.role(id)
        user_id = get_jwt_identity()
        UserRole().role(user_id)
        try:

            conn = db()
            cur = conn.cursor()
            user = cur.execute("SELECT * FROM users WHERE email = %(email)s",{"email":user_id})
            if not user:
                return {"Message":"The user does not exists"}
            updt = cur.execute("DELETE FROM users WHERE email = %(email)s",{"email":user_id})
            conn.commit()
            return {"message": "User has been deleted successfully"}, 200

        except (Exception, psycopg2.DatabaseError) as error:
            cur.execute("rollback;")
            print(error)
            return {'Message': 'current transaction is aborted'}, 500
