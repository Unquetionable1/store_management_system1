from classes.products import Product
from classes.orders import Orders
from classes.customers import Customer


class StoreManagement:
    @staticmethod
    def run():
        while True:
            choice = input("""
            1. Add Product
            2. Update Product
            3. Delete Product
            4. List Products
            5. Add Customer
            6. Delete Customer
            7. List Customers
            8. Add Orders
            9. Delete Orders
            10. List Orders
            11. Exit

            Enter your choice: """)
            if choice == '1':
                Product.add()
            elif choice == '2':
                Product.update()
            elif choice == '3':
                Product.delete()
            elif choice == '4':
                Product.list_all()
            elif choice == '5':
                Customer.add()
            elif choice == '6':
                Customer.delete()
            elif choice == '7':
                Customer.list_all()
            elif choice == '8':
                Orders.add()
            elif choice == '9':
                Orders.delete()
            elif choice == '10':
                Orders.list_all()
            elif choice == '11':
                print("Exiting store management system.")
                break
            else:
                print("Invalid choice. Please enter a valid option.")


if __name__ == '__main__':
    store_management = StoreManagement()
    store_management.run()
