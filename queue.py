class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        return None

    def peek(self):
        return self.items[0] if not self.is_empty() else None

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def display(self):
        if self.is_empty():
            print("No orders in the queue!")
        else:
            print("\n--- Current Orders in Queue ---")
            for index, order in enumerate(self.items, 1):
                print(f"{index}. Order ID: {order['order_id']}, Customer: {order['name']}, Product: {order['product_name']}, Quantity: {order['quantity']}")
