orders = []

class Order:

    order_id = 1
    def __init__(self,name=None,price=None,description=None, status="Pending"):
        self.name=name
        self.price=price
        self.description=description
        self.id=Order.order_id
        self.status=status
        

        Order.order_id += 1

    def successive(self):
        return dict(
            id=self.id,
            name=self.name,
            price=self.price,
            description=self.description,
            status=self.status
        )

    def get_by_id(self, order_id):
        for order in orders:
            if order.id == order_id:
                return order