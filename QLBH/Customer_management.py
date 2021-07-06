from Entities import Customer
import uuid


class CustomerManagement:

    @staticmethod
    def get_customers():
        customers = []
        try:
            file = open('customer.txt', 'r')
            for line in file:
                customer_id, name, phone = line.split(';')
                customers.append(Customer(uuid.UUID(customer_id), name, phone))
        finally:
            file.close()
        return customers

    @staticmethod
    def add_customer():
        customer = Customer()
        customer.customer_id = uuid.uuid4()
        customer.name = input("Customer name: ")
        customer.phone = input("Phone: ")

        customer_file = None
        try:
            customer_file = open("customer.txt", "a")
            customer_file.write(customer.__str__())
            print("Add customer successfully")
        except:
            print("Open customer.txt failed")
        finally:
            customer_file.close()

        return customer

# CustomerManagement.add_customer()
