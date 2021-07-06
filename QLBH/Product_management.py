from Entities import Product
from Utils import Validation


class ProductManagement:

    @staticmethod
    def get_products():
        products = []
        try:
            file = open('product.txt', 'r')
            for line in file:
                product_id, name, brand, product_type, price = line.split(';')
                products.append(Product(int(product_id), name, brand, product_type, float(price)))
        finally:
            file.close()
        return products

    @staticmethod
    def check_duplicate_product_id(product_id):
        ids = [product.product_id for product in ProductManagement.get_products()]
        if product_id in ids:
            return True
        return False

    @staticmethod
    def add_product():
        product = Product()
        product.product_id = Validation.input_int("Product ID: ")
        product.name = input("Product name: ")
        product.brand = input("Brand: ")

        choice = None
        while choice != 1 and choice != 2:
            print("Please choose type of product: ")
            print("1. Electronic device")
            print("2. Housewares")
            choice = Validation.input_int("Choice: ")
            if choice == 1:
                product.product_type = "Electronic device"
            if choice == 2:
                product.product_type = "Housewares"

        product.price = Validation.input_float("Product price: ")
        while product.price < 0:
            print("Price > 0")
            product.price = Validation.input_float("Product price: ")

        if ProductManagement.check_duplicate_product_id(product.product_id):
            print("Duplicate product ID!!!")
        else:
            product_file = None
            try:
                product_file = open("product.txt", "a")
                product_file.write(product.__str__())
                print("Add product successfully")
            except:
                print("Open product.txt failed")
            finally:
                product_file.close()

        return product

    @staticmethod
    def get_product_name(order):
        products = ProductManagement.get_products()
        for product in products:
            if product.product_id == order.product_id:
                return product.name
