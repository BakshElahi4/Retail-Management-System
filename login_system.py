import os
import time
class LoginSystem:
    def __init__(self):
        self.admin_credentials = {"username": "admin", "password": "admin123"}
        self.user_credentials = {}  
    def sign_up(self, user_type):
        """
        Function to handle sign-up for Admin or User
        """
        if user_type == 'admin':
            username = input("Enter admin username: ")
            password = input("Enter admin password: ")
            self.admin_credentials["username"] = username
            self.admin_credentials["password"] = password
            print("Admin registration successful!")
            time.sleep(2)
            

        elif user_type == 'user':
            username = input("Enter username to register: ")
            password = input("Enter password to register: ")
            if username not in self.user_credentials:
                self.user_credentials[username] = password
                print("User registration successful!")
                time.sleep(2)
            else:
                print("Username already exists. Please choose another one.")
                time.sleep(2)

    def sign_in(self, user_type):
        """
        Function to handle login for Admin or User
        """
        if user_type == 'admin':
            username = input("Enter admin username: ")
            password = input("Enter admin password: ")
            if username == self.admin_credentials["username"] and password == self.admin_credentials["password"]:
                print("Admin login successful!")
                time.sleep(2)
                return True
            else:
                print("Invalid admin credentials!")
                time.sleep(2)
                return False
        elif user_type == 'user':
            username = input("Enter username: ")
            password = input("Enter password: ")
            if username in self.user_credentials and self.user_credentials[username] == password:
                print("User login successful!")
                time.sleep(2)
                return True
            else:
                print("Invalid user credentials!")
                time.sleep(2)
                return False
        return False
