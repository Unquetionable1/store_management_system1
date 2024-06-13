from tabulate import tabulate
import sqlite3

con = sqlite3.connect('db/store.db')
cur = con.cursor()


class Product:
    @staticmethod
    def add():
        name = input('Enter product name: ')
        price = int(input('Enter product price: '))
        quantity = int(input("Enter product quantity: "))
        cur.execute('INSERT INTO products (name, price, quantity) VALUES (?, ?, ?)',
                    (name, price, quantity))
        con.commit()
        print("Product added successfully.")

    @staticmethod
    def delete():
        Product.list_all()
        product_id = int(input('Enter product id to Delete: '))
        cur.execute('DELETE FROM products WHERE id = ?', (product_id,))
        con.commit()
        print('Product deleted successfully')

    @staticmethod
    def update():
        Product.list_all()
        product_id = int(input('Enter product id to update: '))
        name = input('Enter new product name: ')
        price = int(input('Enter new product price: '))
        quantity = int(input('Enter new product quantity: '))
        cur.execute('UPDATE products SET name = ?, price = ?, quantity = ? WHERE id = ?',
                    (name, price, quantity, product_id))
        con.commit()
        print('Product updated successfully.')

    @staticmethod
    def list_all():
        cur.execute('SELECT * FROM products')
        products = cur.fetchall()
        if products:
            for product in products:
                print(product)
            headers = ['ID', 'Name', 'Price ', 'Quantity ']
            print(tabulate(products, headers=headers, tablefmt='github'))
        else:
            print('No products found.')
