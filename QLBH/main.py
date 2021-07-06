from Utils import Validation
from Customer_management import CustomerManagement
from Product_management import ProductManagement
from Order_management import OrderManagement

if __name__ == "__main__":
    while True:
        print("1.Add customer")
        print("2.Add product")
        print("3.Add order")
        print("4.Report")
        print("5.Sort order by customer name")
        print("6.Sort order by date")
        print("7. Exit")
        choice = Validation.input_int("Your choice: ")
        if choice == 1:
            CustomerManagement.add_customer()
        elif choice == 2:
            ProductManagement.add_product()
        elif choice == 3:
            OrderManagement.add_order()
        elif choice == 4:
            OrderManagement.customer_report()
        elif choice == 5:
            OrderManagement.sort_order_by_customer_name()
        elif choice == 6:
            OrderManagement.sort_order_by_date()
        else:
            break