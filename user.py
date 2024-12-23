from queue import Queue 
import keyboard
import os
import time
class User:
    def __init__(self):
        self.users = {}  

    def register_user(self, user_id, password):
        if user_id in self.users:
            print("User ID already exists! Please choose another one.")
            time.sleep(2)
        else:
            self.users[user_id] = password
            print(f"User {user_id} registered successfully!")
            time.sleep(2)

    def login(self, user_id, password):
        if self.users.get(user_id) == password:
            print(f"Welcome back, {user_id}!")
            time.sleep(2)
            return True
        else:
            print("Invalid credentials!")
            time.sleep(2)
            return False


class UserOperations:
    def __init__(self, shop, avl_tree, delivery):
        self.shop = shop
        self.avl_tree = avl_tree
        self.delivery = delivery

    def display_products(self):
        self.shop.display_products()

    def place_takeaway_order(self):
        name = input("Enter your name: ")
        self.shop.display_products()
        product_id = int(input("Enter the product ID: "))
        quantity = int(input("Enter the quantity: "))
        order_id = int(input("Enter order ID: "))
        order_type = "takeaway"

        product = self.shop.get_product_by_id(product_id)
        if product:
            if quantity <= product["stock"]:
                bill = quantity * product["price"]
                product["stock"] -= quantity
                self.avl_tree.add_order(name, quantity, product["name"], bill, order_id, order_type="takeaway")
                self.shop.place_order(name, product["name"], quantity, order_type)
                print(f"Order placed successfully! Order ID: {order_id}, Total Bill: {bill}")
                time.sleep(3)
            else:
                print(f"Insufficient stock for {product['name']}. Available: {product['stock']}")
                time.sleep(2)
        else:
            print("Invalid product ID!")
            time.sleep(2)

    def place_home_delivery_order(self):
        city_map = {"1": "Islamabad", "2": "Lahore", "3": "Karachi", "7": "Abottabad"}
        print("\nAvailable Cities:")
        for code, city in city_map.items():
            print(f"{code}. {city}")

        city_code = input("Enter city code: ")
        if city_code in city_map:
            city_name = city_map[city_code]
            areas = self.delivery.further_area(int(city_code))
            if areas:
                print("\nAvailable Areas:")
                for idx, area in enumerate(areas, 1):
                    print(f"{idx}. {area}")
                area_idx = int(input("Select an area: "))
                if 1 <= area_idx <= len(areas):
                    delivery_area = areas[area_idx - 1]
                    print(f"Delivery Area Selected: {delivery_area}")

                    name = input("Enter your name: ")
                    self.shop.display_products()
                    product_id = int(input("Enter the product ID: "))
                    quantity = int(input("Enter the quantity: "))

                    delivery_charges = 20 * 15  
                    product = self.shop.get_product_by_id(product_id)

                    if product:
                        if quantity <= product["stock"]:
                            bill = quantity * product["price"] + delivery_charges
                            product["stock"] -= quantity
                            delivery_address = f"{delivery_area}, {city_name}"
                            self.avl_tree.add_order(
                                name, quantity, product["name"], bill, product_id, order_type="delivery"
                            )
                            self.shop.place_order(name, product["name"], quantity, order_type="home_delivery")
                            print(f"Order placed! Total (including delivery): {bill}. Delivered to: {delivery_address}")
                            time.sleep(3)
                            
                        else:
                            print(f"Insufficient stock for {product['name']}. Available: {product['stock']}")
                            time.sleep(2)
                    else:
                        print("Invalid product ID!")
                        time.sleep(2)
            else:
                print(f"No delivery areas available for {city_name}.")
                time.sleep(2)
        else:
            print("Invalid city code!")
            time.sleep(2)

    def get_order_from_warehouse(self):
        order_id = int(input("Enter the Order ID: "))
        order = self.avl_tree.search(self.avl_tree.root, order_id)
        if order:
            if order.order_type == "takeaway": 
                print("\n--- Order Details ---")
                print(f"Order ID       : {order.order_id}")
                print(f"Customer Name  : {order.name}")
                print(f"Product Name   : {order.product_name}")
                print(f"Quantity       : {order.quantity}")
                print(f"Total Bill     : {order.bill}")
                print(f"Order Type     : {order.order_type}")
                print("\nOrder is ready for collection from the warehouse.")
                time.sleep(4)
            else:
                print(f"Order with ID {order_id} is a home delivery order and cannot be collected from the warehouse.")
                time.sleep(3)
        else:
            print(f"Order ID {order_id} not found.")
            time.sleep(2)