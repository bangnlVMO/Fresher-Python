from uuid import UUID
import datetime


class Product:
    def __init__(self, product_id: int = None, name: str = '', brand: str = '', product_type: str = '', price: str = ''):
        self.__product_id = product_id
        self.__name = name
        self.__brand = brand
        self.__product_type = product_type  # Thiet bi dien tu, do gia dung
        self.__price = price

    @property
    def product_id(self):
        return self.__product_id

    @product_id.setter
    def product_id(self, product_id: int):
        self.__product_id = product_id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def brand(self):
        return self.__brand

    @brand.setter
    def brand(self, brand: str):
        self.__brand = brand

    @property
    def product_type(self):
        return self.__product_type

    @product_type.setter
    def product_type(self, product_type: str):
        self.__product_type = product_type

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price: float):
        self.__price = price

    def __str__(self):
        return "{};{};{};{};{}\n".format(self.product_id, self.name, self.brand, self.product_type, self.price)


class Customer:
    def __init__(self, customer_id: UUID = None, name: str = '', phone: str = ''):
        self.__customer_id = customer_id
        self.__name = name
        self.__phone = phone

    @property
    def customer_id(self):
        return self.__customer_id

    @customer_id.setter
    def customer_id(self, customer_id: int):
        self.__customer_id = customer_id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, phone: str):
        self.__phone = phone

    def __str__(self):
        return "{};{};{}\n".format(self.customer_id, self.name, self.phone)


class Order:
    def __init__(self, customer_id: UUID = None, product_id: int = None, date: datetime = None, quantity: int = None, total: float = None):
        self.__customer_id = customer_id
        self.__product_id = product_id
        self.__quantity = quantity
        self.__date = date
        self.__total = total

    @property
    def customer_id(self):
        return self.__customer_id

    @customer_id.setter
    def customer_id(self, customer):
        self.__customer_id = customer

    @property
    def product_id(self):
        return self.__product_id

    @product_id.setter
    def product_id(self, product):
        self.__product_id = product

    @property
    def quantity(self):
        return self.__quantity

    @quantity.setter
    def quantity(self, quantity):
        self.__quantity = quantity

    @property
    def total(self):
        return self.__total

    @total.setter
    def total(self, total):
        self.__total = total

    @property
    def date(self):
        return self.__date

    @date.setter
    def date(self, date):
        self.__date = date

    def __str__(self):
        return "{};{};{};{};{}\n".format(self.customer_id,
                                         self.product_id,
                                         self.quantity,
                                         self.total,
                                         self.date)