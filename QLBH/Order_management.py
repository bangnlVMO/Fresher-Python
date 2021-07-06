import datetime
import uuid

from Entities import Order
from Customer_management import CustomerManagement
from Product_management import ProductManagement
from Utils import Validation


class OrderManagement:

    @staticmethod
    def get_orders():
        orders = []
        try:
            file = open('orders.txt', 'r')
            for line in file:
                customer_id, product_id, quantity, total, date = line.split(';')
                orders.append(Order(uuid.UUID(customer_id), int(product_id), date, int(quantity), float(total)))
        finally:
            file.close()
        return orders

    @staticmethod
    def add_order():
        check = True
        while check:
            customer = OrderManagement.find_customer()
            bought_product, amount = OrderManagement.buy_product()
            orders = OrderManagement.get_orders()

            count = 0
            total = 0

            for order in orders:
                if customer.customer_id == order.customer_id and datetime.date.today().__str__() == str(order.date).split()[0]:
                    count += order.quantity

            if count >= 5:
                total = amount*bought_product.price
            else:
                remain = 5 - count
                if amount <= remain:
                    total = amount*bought_product.price*0.5
                else:
                    total = remain*bought_product.price*0.5 + (amount - remain)*bought_product.price
            try:
                orders_file = open('orders.txt', 'a');
                orders_file.write(
                    Order(customer.customer_id, bought_product.product_id, datetime.datetime.now(), amount, total).__str__())
                print("Ordered successfully!!!")
            finally:
                orders_file.close()
            choice = input("Do you want to buy another product[y/n]?")
            if choice == 'n':
                check = False

    @staticmethod
    def find_customer():
        while True:
            customer_id = uuid.UUID(input("Customer ID: "))
            for customer in CustomerManagement.get_customers():
                if customer.customer_id == customer_id:
                    return customer
            print("Customer doesn't exist, type again!!!")

    @staticmethod
    def buy_product():
        bought_product = None
        while True:
            product_id = Validation.input_int("Product ID: ")
            for product in ProductManagement.get_products():
                if product.product_id == product_id:
                    amount = Validation.input_int("Amount: ")
                    bought_product = product
                    return bought_product, amount
            print("Product doesn't exist, type again!!!")

    @staticmethod
    def customer_report():
        orders = OrderManagement.get_orders()
        customer = OrderManagement.find_customer()
        for order in orders:
            if order.customer_id == customer.customer_id:
                print(order.__dict__)

    @staticmethod
    def get_customer_name(order):
        customers = CustomerManagement.get_customers()
        for customer in customers:
            if customer.customer_id == order.customer_id:
                return customer.name

    @staticmethod
    def get_order_date(order):
        return order.date

    @staticmethod
    def sort_order_by_customer_name():
        orders = OrderManagement.get_orders()
        orders.sort(key=OrderManagement.get_customer_name)
        for order in orders:
            print('{}-{}-{}-{}-{}-{}-{}'.format(order.customer_id, OrderManagement.get_customer_name(order),
                                                order.product_id, ProductManagement.get_product_name(order),
                                                order.quantity, order.total, order.date))

    @staticmethod
    def sort_order_by_date():
        orders = OrderManagement.get_orders()
        orders.sort(key=OrderManagement.get_order_date)
        for order in orders:
            print('{}-{}-{}-{}-{}-{}-{}'.format(order.customer_id, OrderManagement.get_customer_name(order),
                                                order.product_id, ProductManagement.get_product_name(order),
                                                order.quantity, order.total, order.date))

