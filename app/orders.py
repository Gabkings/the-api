# from flask import Flask, request
# from flask_restful import Resource
# from .models import Order, orders

# class OrderOpreations(Resource):
    

#     def get(self, id):
#         order = Order().get_by_id(id)
        
#         if order:
#             return {"order": order.successive()}, 200

#         return {"message":"Order not found"}, 404


#     def put(self, id):
#         order = Order().get_by_id(id)

#         if order:
#             order.status="approved"
#             return {"message":"status approved"}
#         return {"message":"Order not found"}, 404

#     def delete(self, id):
#         order = Order().get_by_id(id)

#         if order:
#             orders.remove(order)
#             return {"message":"order deleted successfully"},200
#         return {"message":"Order not found"}, 404

# class DisplayOrders(Resource):
#     def get(self):
#         return {"orders":[order.successive() for order in orders]}

#     def post(self):
#         data = request.get_json()
#         order = Order(data['name'], data["price"],data['description'])
#         orders.append(order)

#         return {"message":"Food order created"}, 201