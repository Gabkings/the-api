# app/api/v2/resources/checkauth.py

from flask import request
import jwt
from functools import wraps


def check_auth(f):

    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']

        if not token:
            return {'message': 'Token is missing!'}, 401

        try:
            data = jwt.decode(token, 'secret')
            conn = db()
            cur = conn.cursor()

            current_user = cur.execute("SELECT * FROM users WHERE id = %(id)s ",
                                       {'id': data["id"]})
            print(current_user)

        except:
            return {'message': 'Token is invalid!'}, 401

        return f(current_user, *args, **kwargs)

    return decorated
