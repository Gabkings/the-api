orders = []

class Order:
    '''this carries all the details of order and initializing them'''

    order_id = 1
    def __init__(self,name=None,price=None,description=None, status="Pending",andress=None,username=None,user_id=None):
        self.name=name
        self.price=price
        self.description=description
        self.id=Order.order_id
        self.status=status
        self.andress=andress
        self.username=username
        self.user_id = user_id
        

        Order.order_id += 1

    def collect_order_details(self):
        return dict(
            id=self.id,
            name=self.name,
            price=self.price,
            description=self.description,
            status=self.status,
            u_address=self.andress,
            username=self.username,
            user_id = self.user_id
        )

    def get_by_id(self, order_id):
        for order in orders:
            if order.id == order_id:
                return order

    def get_by_name(self, name):
        #print(orders)
        for ordr in orders:
            if ordr.name == name:
                return True
            return False        