from abc import ABC, abstractmethod

# Strategy Interface
class PaymentStrategy(ABC):

    @abstractmethod
    def pay(self, amount):
        pass


# Concrete Strategies
class CreditCard(PaymentStrategy):

    def pay(self, amount):
        print(f"Paid ₹{amount} using Credit Card")


class UPI(PaymentStrategy):

    def pay(self, amount):
        print(f"Paid ₹{amount} using UPI")


class Cash(PaymentStrategy):

    def pay(self, amount):
        print(f"Paid ₹{amount} using Cash")


# Context
class ShoppingCart:

    def __init__(self, strategy):
        self.strategy = strategy

    def checkout(self, amount):
        self.strategy.pay(amount)


# Client Code
cart = ShoppingCart(CreditCard())
cart.checkout(1000)

cart = ShoppingCart(UPI())
cart.checkout(500)

cart = ShoppingCart(Cash())
cart.checkout(200)

