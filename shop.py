from queue import Queue
import keyboard
import os
import time
class Shop:
    def __init__(self):
        self.products = [
            {"id": 1, "name": "Sony FX30", "price": 45500, "stock": 10},
            {"id": 2, "name": "Sony FR7", "price": 175000, "stock": 5},
            {"id": 3, "name": "Canon EOS 90D", "price": 289000, "stock": 8},
            
        ]
        self.orders = []  
        self.product_id_counter = len(self.products)  
        self.order_id_counter = 1  

        self.order_queue = Queue()

    def display_products(self):
        print("\n--- Product List ---")
        for product in self.products:
            print(f"ID: {product['id']} - {product['name']} - ${product['price']} - Stock: {product['stock']}")
        
        time.sleep(5)    
        
        

    def add_product(self, name, price, stock=0):
        """Add a new product."""
        self.product_id_counter += 1 
        self.products.append({"id": self.product_id_counter, "name": name, "price": price, "stock": stock})
        print(f"Product {name} added successfully with ID {self.product_id_counter} and {stock} stock!")
        time.sleep(2)

    def remove_product(self, product_id):
        """Remove a product by its ID."""
        product = next((product for product in self.products if product['id'] == product_id), None)
        if product:
            self.products.remove(product)
            print(f"Product {product['name']} removed successfully!")
            time.sleep(2)
        else:
            print("Invalid Product ID!")
            time.sleep(2)
            
    def update_product(self, product_id, new_name, new_price):
        """Update product information."""
        product = next((product for product in self.products if product['id'] == product_id), None)
        if product:
            product["name"] = new_name
            product["price"] = new_price
            print("Product updated successfully!")
            time.sleep(2)
        else:
            print("Invalid Product ID!")
            time.sleep(2)

    def update_stock(self, product_id, new_stock):
        """Update stock for a product."""
        product = next((product for product in self.products if product['id'] == product_id), None)
        if product:
            product["stock"] = new_stock
            print(f"Stock for product {product['name']} updated successfully!")
            time.sleep(2)
        else:
            print("Invalid Product ID!")
            time.sleep(2)

    def place_order(self, customer_name, product_name, quantity, order_type):
        """Place a new order."""
        product = next((product for product in self.products if product["name"] == product_name), None)
        if not product:
            print("Product not found!")
            time.sleep(2)
            return
        if product["stock"] < quantity:
            print(f"Not enough stock for {product_name}. Available stock: {product['stock']}")
            time.sleep(2)
            return
        
        bill = product["price"] * quantity
        order = {
            "order_id": self.order_id_counter,
            "customer_name": customer_name,
            "product_name": product_name,
            "quantity": quantity,
            "bill": bill,
            "order_type": order_type  
        }
        

        self.order_queue.enqueue(order)

        self.orders.append(order)
        self.order_id_counter += 1  
        product["stock"] -= quantity  
        print(f"Order {order['order_id']} placed successfully for {customer_name}!")
        time.sleep(5)

    def get_all_orders(self):
        """Display all orders."""
        if not self.orders:
            print("No orders found.")
            time.sleep(2)
            return

        print("\n--- All Orders ---")
        print(f"{'Order ID':<10}{'Customer Name':<20}{'Product':<25}{'Quantity':<10}{'Total Bill':<15}{'Order Type':<15}")
        print("-" * 90)

        for order in self.orders:
            print(f"{order['order_id']:<10}{order['customer_name']:<20}{order['product_name']:<25}{order['quantity']:<10}{order['bill']:<15}{order['order_type']:<15}")
        print("-" * 90)
        
        time.sleep(5)

    def process_orders(self):
        """Process all orders in the queue."""
        if self.order_queue.is_empty():
            print("No orders to process!")
            time.sleep(2)
            return

        print("\n--- Processing Orders ---")
        print(f"{'Order ID':<10}{'Customer Name':<20}{'Product':<25}{'Quantity':<10}{'Total Bill':<15}{'Order Type':<15}")
        print("-" * 90)

        while not self.order_queue.is_empty():
            order = self.order_queue.dequeue()  
            print(f"{order['order_id']:<10}{order['customer_name']:<20}{order['product_name']:<25}{order['quantity']:<10}{order['bill']:<15}{order['order_type']:<15}")

        print("-" * 90)
        print("All orders processed successfully!")
        time.sleep(5)

    def get_product_by_id(self, product_id):
        """Get product by ID."""
        return next((p for p in self.products if p["id"] == product_id), None)
