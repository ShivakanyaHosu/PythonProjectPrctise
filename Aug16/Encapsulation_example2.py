class bank:

    def __init__(self, account_number, balance):
        self.balance = balance  # public
        self.__account_number = account_number  # private

    def public_method(self):
        self.__internal_private_method()

    def check_balance(self):
        print(self.balance)

    def deposit(self, amount):
        self.balance = self.balance + amount

    def show_me_balance(self, Isauth):
        if Isauth == True:
            print(self.__account_number)
        else:
            print("Not allowed!")

    def __internal_private_method(self):
        print("Private method only access by class")


icici = bank(987654321, 100)
icici.deposit(100)
icici.check_balance()
print(icici.balance)
# print(icici.__account_number)
icici.show_me_balance(False)
# icici.__internal_private_method()
icici.public_method()
