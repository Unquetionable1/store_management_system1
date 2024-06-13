from tabulate import tabulate
import re
import sqlite3

con = sqlite3.connect('db/store.db')
cur = con.cursor()

class Customer:
    @staticmethod
    def add():
        """Add a new customer"""

        name = input("Enter customer name: ")
        while True:
            email = input("Enter customer email: ")
            email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
            if not re.match(email_regex, email):
                print("Invalid email format. Please try again.")
            else:
                break
        cur.execute('INSERT INTO customers (name, email) VALUES (?, ?)', (name, email))
        con.commit()
        print("Customer added successfully.")

    @staticmethod
    def delete():
        Customer.list_all()
        Customer_id = int(input('Enter customer id to Delete: '))
        cur.execute('DELETE FROM customers WHERE id = ?', (Customer_id,))
        con.commit()
        print('Customer deleted successfully')

    @staticmethod
    def list_all():
        cur.execute('SELECT * FROM customers')
        customers = cur.fetchall()
        if customers:
            headers = ['ID', 'Name', 'Email ']
            print(tabulate(customers, headers=headers, tablefmt='github'))
        else:
            print('No Customers found.')