
"""
Python Encapsulation
Project: Simple Bank Account
"""


class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = 0

        if balance >= 0:
            self.__balance = balance
        else:
            print("Initial balance cannot be negative.")

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive.")
            return

        self.__balance += amount
        print(f"Deposited: Rs. {amount}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > self.__balance:
            print("Insufficient balance.")
        else:
            self.__balance -= amount
            print(f"Withdrawn: Rs. {amount}")

    def get_balance(self):
        return self.__balance

    def display_account(self):
        print("\n--- Account Details ---")
        print(f"Account Holder: {self.owner}")
        print(f"Current Balance: Rs. {self.get_balance()}")


def main():
    account = BankAccount("Suraj", 2000)

    account.display_account()
    account.deposit(500)
    account.withdraw(300)
    account.display_account()

    account.withdraw(5000)


if __name__ == "__main__":
    main()
