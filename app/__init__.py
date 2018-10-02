from flask import Flask
from flask_restful import Api
from instance.config import app_config
from .api.v1.views.orders import OrderOpreations,DisplayOrders
from .api.v2.users.users import Users,Login
from .api.v2.meals.meals import Meals
from .api.v2.orders.orders import Orders
from .api.v2.models.db import init_db


def create_app(config_stage):
    Gabriel = Flask(__name__)
    Gabriel.config.from_object(app_config[config_stage])
    api = Api(Gabriel)
    init_db()
    api.add_resource(Users, '/api/v2/auth/signup')
    api.add_resource(Login, '/api/v2/auth/login')
    api.add_resource(Meals, '/api/v2/menu')
    api.add_resource(Orders, '/api/v2/orders')



    return Gabriel
