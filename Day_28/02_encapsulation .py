class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Deposit successful.")
        else:
            print("Amount must be positive.")

    def check_balance(self):
        print("Balance:", self.__balance)


account = BankAccount(1000)

account.deposit(500)
account.check_balance()