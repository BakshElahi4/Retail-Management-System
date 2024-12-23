class Order:
    def __init__(self, order_id, name, product, quantity, bill, order_type):
        self.order_id = order_id
        self.name = name
        self.product = product
        self.quantity = quantity
        self.bill = bill
        self.order_type = order_type

    def display_order(self):
        print(f"Order ID: {self.order_id}")
        print(f"Customer Name: {self.name}")
        print(f"Product: {self.product}")
        print(f"Quantity: {self.quantity}")
        print(f"Total Bill: {self.bill}")
        print(f"Order type: {self.order_type}")
