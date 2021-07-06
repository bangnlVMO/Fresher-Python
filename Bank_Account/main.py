class BankAccount:
    def __init__(self, acc_name, acc_number, balance):
        self.acc_name = acc_name
        self.acc_number = acc_number
        self.balance = balance

    def deposit(self, value):
        self.balance += value

    def fee(self, value):
        if value*0.01 > 1000:
            return value*0.01
        else:
            return 1000

    def withdraw(self, value):
        if self.balance - value - self.fee(value) >= 0:
            self.balance -= (value + self.fee(value))
            print("Fee:", self.fee(value))
            print("Withdraw Successfully")
        else:
            print("Not enough")

    def acc_infor(self):
        print("Account name:", self.acc_name)
        print("Account number:", self.acc_number)
        print("Account balance:", self.balance)

acc = BankAccount("LuongBang", 11111, 1000000)
acc.deposit(500000)
acc.acc_infor()
acc.withdraw(200000)
acc.acc_infor()