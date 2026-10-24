from abc import ABC, abstractmethod


class Payment(ABC):

    @abstractmethod
    def pay(self, amount):
        pass


class UpiPayment(Payment):
    def pay(self, amount):
        print(f"Processing UPI payment of Rs. {amount}")


class CardPayment(Payment):
    def pay(self, amount):
        print(f"Processing card payment of Rs. {amount}")


upi = UpiPayment()
card = CardPayment()

upi.pay(500)
card.pay(1000)