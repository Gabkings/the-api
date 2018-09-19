from flask import Flask, request
from flask_restful import Resource
from app.model import Order, orders

class OrderOpreations(Resource):
    

    def get(self, id):
        order = Order().get_by_id(id)
        
        if order:
            return {"order": order.successive()}, 200

        return {"message":"Order not found"}, 404



class DisplayOrders(Resource):
    def post(self):
        data = request.get_json()
        order = Order(data['name'], data["price"],data['description'])
        orders.append(order)

        return {"message":"Food order has been created"}, 201

    def get(self):
        return {"orders":[order.successive() for order in orders]}
