class Node:
    def __init__(self, name, quantity, product_name, bill, order_id, order_type):
        self.name = name
        self.quantity = quantity
        self.product_name = product_name
        self.bill = bill
        self.order_id = order_id
        self.order_type = order_type
        self.height = 1  
        self.left = None
        self.right = None


class AVLTree:
    def __init__(self):
        self.root = None

    
    def height(self, node):
        if not node:
            return 0
        return node.height


    def balance_factor(self, node):
        if not node:
            return 0
        return self.height(node.left) - self.height(node.right)

    
    def right_rotate(self, y):
        x = y.left
        T2 = x.right


        x.right = y
        y.left = T2

        
        y.height = max(self.height(y.left), self.height(y.right)) + 1
        x.height = max(self.height(x.left), self.height(x.right)) + 1

        
        return x

    
    def left_rotate(self, x):
        y = x.right
        T2 = y.left

        
        y.left = x
        x.right = T2

        
        x.height = max(self.height(x.left), self.height(x.right)) + 1
        y.height = max(self.height(y.left), self.height(y.right)) + 1

        
        return y

    
    def insert(self, root, name, quantity, product_name, bill, order_id, order_type):
        
        if not root:
            return Node(name, quantity, product_name, bill, order_id, order_type)

        if order_id < root.order_id:
            root.left = self.insert(root.left, name, quantity, product_name, bill, order_id, order_type)
        else:
            root.right = self.insert(root.right, name, quantity, product_name, bill, order_id, order_type)


        root.height = 1 + max(self.height(root.left), self.height(root.right))


        balance = self.balance_factor(root)


        if balance > 1 and order_id < root.left.order_id:
            return self.right_rotate(root)


        if balance < -1 and order_id > root.right.order_id:
            return self.left_rotate(root)


        if balance > 1 and order_id > root.left.order_id:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)


        if balance < -1 and order_id < root.right.order_id:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)


        return root


    def add_order(self, name, quantity, product_name, bill, order_id, order_type):
        self.root = self.insert(self.root, name, quantity, product_name, bill, order_id, order_type)

    def inorder(self, root, order_type=None):
        """In-order traversal of the AVL tree to print orders, filtered by order type."""
        if not root:
            return
        

        self.inorder(root.left, order_type)
        

        if not order_type or root.order_type == order_type:
            print(f"Order ID: {root.order_id}, Name: {root.name}, Product: {root.product_name}, Quantity: {root.quantity}, Bill: {root.bill}, Order Type: {root.order_type}")
        

        self.inorder(root.right, order_type)


    def search(self, root, order_id):

        if root is None or root.order_id == order_id:
            return root


        if order_id < root.order_id:
            return self.search(root.left, order_id)


        return self.search(root.right, order_id)


    def get_all_orders(self):
        """In-order traversal to fetch all orders in sorted order by Order ID."""
        orders = []
        self._inorder_traversal(self.root, orders)
        return orders

    def _inorder_traversal(self, node, orders, order_type=None):
        """Helper method to perform in-order traversal and collect data."""
        if node:

            self._inorder_traversal(node.left, orders, order_type)
            

            if not order_type or node.data.order_type == order_type:
                orders.append(node.data) 
            

            self._inorder_traversal(node.right, orders, order_type)


    def get_order_by_id(self, order_id):
        return self.search(self.root, order_id)

