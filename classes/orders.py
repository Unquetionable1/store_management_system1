from tabulate import tabulate
from .customers import Customer
from .products import Product
from connection import con, cur

class Orders:
    @staticmethod
    def add():
        """Add a new order"""
        Customer.list_all()
        customer_id = int(input("Enter customer ID: "))
        Product.list_all()
        product_id = int(input("Enter product ID: "))
        quantity = int(input("Enter quantity: "))
        cur.execute('INSERT INTO orders (customer_id, product_id, quantity) VALUES (?, ?, ?)',
                    (customer_id, product_id, quantity))
        con.commit()
        print("Order added successfully.")

    @staticmethod
    def delete():
        Orders.list_all()
        order_id = int(input('Enter Order ID to delete: '))
        cur.execute('DELETE FROM orders WHERE id = ?', (order_id,))
        con.commit()
        print('Order deleted successfully')

    @staticmethod
    def list_all():
        sql = '''
            SELECT orders.id, customers.name, products.name, orders.quantity
            FROM orders
            JOIN customers ON orders.customer_id = customers.id
            JOIN products ON orders.product_id = products.id
        '''
        cur.execute(sql)
        orders = cur.fetchall()
        if orders:
            headers = ['Order ID', 'Customer Name', 'Product Name', 'Quantity']
            print(tabulate(orders, headers=headers, tablefmt='github'))
        else:
            print('No Orders found.')