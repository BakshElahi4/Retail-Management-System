from queue import Queue
import keyboard
import os
class Admin:
    def __init__(self, username, password):
        self.username = username
        self.password = password
    
    def login(self):
        print("\n---- Admin Login ----")
        user = input("Enter username: ")
        passw = input("Enter password: ")
        
        if user == self.username and passw == self.password:
            print("Login successful!")
            time.sleep(2)
            return True
        else:
            print("Invalid credentials! Try again.")
            time.sleep(2)
            return False


class AdminPanel:
    def __init__(self, shop):
        self.shop = shop
        self.admin = Admin(username="admin", password="admin123")  

    def display_menu(self):
        print("\n********** Admin Panel **********")
        print("1. Manage Products")
        print("2. View All Orders")
        print("3. Update Stock")
        print("4. Process Orders")  
        print("0. Log out")

    def manage_products(self):
        print("\n---- Manage Products ----")
        print("1. Add Product")
        print("2. Remove Product")
        print("3. Update Product Details")
        print("4. View All Products")
        print("0. Back")
        choice = int(input("Choose an option: "))
        
        if choice == 1:
            self.add_product()
        elif choice == 2:
            self.remove_product()
        elif choice == 3:
            self.update_product()
        elif choice == 4:
            self.view_all_products()
        elif choice == 0:
            return
        else:
            print("Invalid choice. Try again.")

    def add_product(self):
        name = input("Enter product name: ")
        price = float(input("Enter product price: "))
        stock = int(input("Enter initial stock quantity: "))
        self.shop.add_product(name, price, stock)

    def remove_product(self):
        product_id = int(input("Enter product ID to remove: "))
        self.shop.remove_product(product_id)

    def update_product(self):
        product_id = int(input("Enter product ID to update: "))
        new_name = input("Enter new product name: ")
        new_price = float(input("Enter new product price: "))
        self.shop.update_product(product_id, new_name, new_price)

    def update_stock(self):
        product_id = int(input("Enter product ID to update stock: "))
        new_stock = int(input("Enter new stock quantity: "))
        self.shop.update_stock(product_id, new_stock)

    def view_all_products(self):
        print("\n--- All Products ---")
        self.shop.display_products()

    def view_orders(self):
        """View all orders in the system."""
        print("\n---- View All Orders ----")
        self.shop.get_all_orders()  

    def process_orders(self):
        """Process all orders in the queue."""
        print("\n---- Process Orders ----")
        self.shop.process_orders()  
