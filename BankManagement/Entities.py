import Utils

from abc import ABC


class BankAccount(ABC):
    def __init__(self, account_number: str = '', balance: float = 0):
        self.__account_number = account_number
        self.__balance = balance

    @property
    def account_number(self):
        return self.__account_number

    @account_number.setter
    def account_number(self, account_number: str):
        self.__account_number = account_number

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, balance):
        self.__balance = balance

    def send_money(self):
        receiving_account = input("Receiving account number: ")
        amount_of_money = Utils.input_int("Amount of money: ")
        if amount_of_money <= self.balance:
            self.balance -= amount_of_money
            print("Money transfer successful!!!")
        else:
            print("Not enough balance!!!")

    # @abstractmethod
    def draw_money(self, *args):
        amount_of_money = Utils.input_int("Amount of money: ")
        if amount_of_money <= self.balance:
            self.balance -= amount_of_money
            print("Draw money successful!!!")
        else:
            print("Not enough balance!!!")

    def check_balance(self):
        print("Total balance:", self.balance)

    def __str__(self):
        return "Account number: {}, Balance: {}, ".format(self.account_number, self.balance)


class SavingAccount(BankAccount):
    def __init__(self, account_number: str = '', balance: float = 0, interest: float = 0):
        super().__init__(account_number, balance)
        self.__interest = interest

    @property
    def interest(self):
        return self.__interest

    @interest.setter
    def interest(self, interest):
        self.__interest = interest

    def draw_money(self):
        super().draw_money()

    def __str__(self):
        return super().__str__() + "Interest: {}".format(self.interest)


class CheckingAccount(BankAccount):
    def __init__(self, account_number: str = '', balance: float = 0, saving_account_number: str = None):
        super().__init__(account_number, balance)
        self.__saving_account_number = saving_account_number

    @property
    def saving_account_number(self):
        return self.__saving_account_number

    @saving_account_number.setter
    def saving_account_number(self, saving_account_number):
        self.__saving_account_number = saving_account_number

    def draw_money(self, saving_account: SavingAccount):
        if self.saving_account_number == '':
            super().draw_money()
        else:
            amount_of_money = Utils.input_int("Amount of money: ")
            if amount_of_money <= self.balance:
                self.balance -= amount_of_money
            else:
                if amount_of_money <= (self.balance + saving_account.balance):
                    amount_of_money -= self.balance
                    self.balance = 0
                    saving_account.balance -= amount_of_money

    def __str__(self):
        return super().__str__() + "Linked saving account: {}".format(self.saving_account_number)


class Customer:
    def __init__(self, name: str = ''):
        self.__name = name
        self.__accounts = []
        self.__num_of_accounts = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def accounts(self):
        return self.__accounts

    @accounts.setter
    def accounts(self, accounts):
        self.__accounts = accounts

    @property
    def num_of_accounts(self):
        return self.__num_of_accounts

    @num_of_accounts.setter
    def num_of_accounts(self, num_of_accounts):
        self.__num_of_accounts = num_of_accounts

    def add_account(self):
        choice = 0
        while 1 > choice or choice > 2:
            print("1. Saving account")
            print("2. Checking account")
            choice = Utils.input_int("Choose type of account:")

        account_number = input("Account number: ")
        balance = Utils.input_float("Balance: ")
        if choice == 1:
            interest = Utils.input_float("Interest: ")
            saving_account = SavingAccount(account_number, balance, interest)
            self.accounts.append(saving_account)
            self.num_of_accounts = len(self.accounts)
            print("Added saving account successfully!!!")
        else:
            checking_account = CheckingAccount(account_number, balance)
            choice = input("Do you want to link checking account to saving account [y/n]?")
            if choice == 'y':
                choice = True
                while choice:
                    saving_account_number = input("Saving account number: ")
                    for account in self.accounts:
                        if isinstance(account, SavingAccount) and account.account_number == saving_account_number:
                            checking_account.saving_account_number = saving_account_number
                            choice = False
                            break
                        else:
                            print("Wrong saving account number!!!")
            self.accounts.append(checking_account)
            self.num_of_accounts = len(self.accounts)
            print("Added checking account successfully!!!")

    def take_account(self, account_number):
        for account in self.accounts:
            if account.account_number == account_number:
                return account

    def show_accounts(self):
        total_balance = 0
        for account in self.accounts:
            print(account)
            total_balance += account.balance
        print("Total balance of all accounts:", total_balance)

