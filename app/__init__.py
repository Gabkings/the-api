from flask import Flask
from flask_restful import Api
from config import app_config
from app.api.v1.orders import OrderOpreations,DisplayOrders

def create_app(config_stage):
    Gabriel = Flask(__name__)
    Gabriel.config.from_object(app_config[config_stage])
    api = Api(Gabriel)
    api.add_resource(OrderOpreations, '/api/v1/orders/<int:id>')
    api.add_resource(DisplayOrders, '/api/v1/orders')


    return Gabriel