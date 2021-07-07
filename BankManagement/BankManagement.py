from Entities import Customer

if __name__ == "__main__":
    customer = Customer("Tran Thi B")
    print("Add saving account:")
    customer.add_account()
    print("Add checking account:")
    customer.add_account()
    customer.show_accounts()
