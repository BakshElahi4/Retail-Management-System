from shop import Shop
from delivery import Delivery
from user import User, UserOperations
from order import Order
from utils import print_welcome_message, print_loading_message
from AVLTree import AVLTree  
from admin import AdminPanel  
from login_system import LoginSystem 
import os
import sys
import time
from colorama import Fore, Style, init

init(autoreset=True)

class ColorStream:
    def __init__(self, stream):
        self.stream = stream

    def write(self, text):
        self.stream.write(Fore.CYAN + text + Style.RESET_ALL)

    def flush(self):
        self.stream.flush()

sys.stdout = ColorStream(sys.stdout)

def main():
    """
    Main function to initialize and manage the e-commerce application.
    """
    print_welcome_message()
    print_loading_message()
    time.sleep(5)


    shop = Shop()
    delivery = Delivery()
    user = User()
    avl_tree = AVLTree() 
    
    admin_panel = AdminPanel(shop)

    login_system = LoginSystem()

    while True:
        os.system('cls')
        print("\n************************  Welcome to the Shop  ************************")
        print("1. Sign up as Admin")
        print("2. Sign up as User")
        print("3. Sign in as Admin")
        print("4. Sign in as User")
        print("0. EXIT")
        
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a valid option.")
            continue
        
        if choice == 1:
            login_system.sign_up('admin')

        elif choice == 2:
            login_system.sign_up('user')

        elif choice == 3:
            if login_system.sign_in('admin'):  
                while True:
                    os.system('cls')
                    admin_panel.display_menu()
                    try:
                        admin_choice = int(input("Choose an option: "))
                    except ValueError:
                        print("Invalid input. Please enter a valid option.")
                        continue
                    
                    if admin_choice == 1:
                        os.system('cls')
                        admin_panel.manage_products()
                    elif admin_choice == 2:
                        os.system('cls')
                        admin_panel.view_orders()
                    elif admin_choice == 3:
                        os.system('cls')
                        admin_panel.update_stock()
                    elif admin_choice == 4:
                        os.system('cls')
                        admin_panel.process_orders()
                    elif admin_choice == 0:
                        print("Logging out as Admin.")
                        break 
                    else:
                        print("Invalid choice. Try again.")
        
        elif choice == 4:
            if login_system.sign_in('user'):
                os.system('cls')  
                user_ops = UserOperations(shop, avl_tree, delivery)
                while True:
                    os.system('cls')
                    print("\n********** User Operations **********")
                    print("1. View Products")
                    print("2. Place Take-Away Order")
                    print("3. Place Home Delivery Order")
                    print("4. Get Order from Warehouse")
                    print("0. Logout")
                    
                    try:
                        user_choice = int(input("Enter your choice: "))
                    except ValueError:
                        print("Invalid input. Please enter a valid option.")
                        continue

                    if user_choice == 1:
                        os.system('cls')
                        user_ops.display_products()
                    elif user_choice == 2:
                        os.system('cls')
                        user_ops.place_takeaway_order()
                    elif user_choice == 3:
                        os.system('cls')
                        user_ops.place_home_delivery_order()
                    elif user_choice == 4:
                        os.system('cls')
                        user_ops.get_order_from_warehouse()
                    elif user_choice == 0:
                        print("Logging out as User.")
                        break
                    else:
                        print("Invalid choice. Please try again.")

        elif choice == 0:
            print("\nThank you for using our services! Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
