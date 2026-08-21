from abc import ABC, abstractmethod

# Strategy Interface
class PaymentStrategy(ABC):

    @abstractmethod
    def pay(self, amount):
        pass


# Credit Card Payment
class CreditCardPayment(PaymentStrategy):

    def __init__(self, card_number, card_holder, cvv):
        self.card_number = card_number
        self.card_holder = card_holder
        self.cvv = cvv

    def pay(self, amount):
        print("\n----- Payment Successful -----")
        print(f"Amount: ₹{amount}")
        print(f"Paid using Credit Card")
        print(f"Card Holder: {self.card_holder}")
        print(f"Card Number: XXXX-XXXX-XXXX-{self.card_number[-4:]}")


# Debit Card Payment
class DebitCardPayment(PaymentStrategy):

    def __init__(self, card_number, card_holder, pin):
        self.card_number = card_number
        self.card_holder = card_holder
        self.pin = pin

    def pay(self, amount):
        print("\n----- Payment Successful -----")
        print(f"Amount: ₹{amount}")
        print(f"Paid using Debit Card")
        print(f"Card Holder: {self.card_holder}")
        print(f"Card Number: XXXX-XXXX-XXXX-{self.card_number[-4:]}")


# UPI Payment
class UpiPayment(PaymentStrategy):

    def __init__(self, upi_id):
        self.upi_id = upi_id

    def pay(self, amount):
        print("\n----- Payment Successful -----")
        print(f"Amount: ₹{amount}")
        print(f"Paid using UPI")
        print(f"UPI ID: {self.upi_id}")


# Net Banking Payment
class NetBankingPayment(PaymentStrategy):

    def __init__(self, bank_name, account_number):
        self.bank_name = bank_name
        self.account_number = account_number

    def pay(self, amount):
        print("\n----- Payment Successful -----")
        print(f"Amount: ₹{amount}")
        print(f"Paid using Net Banking")
        print(f"Bank: {self.bank_name}")
        print(f"Account Number: XXXXXXX{self.account_number[-4:]}")


# Context Class
class PaymentProcessor:

    def __init__(self, strategy):
        self.strategy = strategy

    def process_payment(self, amount):
        self.strategy.pay(amount)


# Main Program
def main():

    amount = float(input("Enter Payment Amount: ₹"))

    print("\nSelect Payment Method")
    print("1. Credit Card")
    print("2. Debit Card")
    print("3. UPI")
    print("4. Net Banking")

    choice = int(input("Enter Choice: "))

    if choice == 1:
        card_number = input("Enter Credit Card Number: ")
        card_holder = input("Enter Card Holder Name: ")
        cvv = input("Enter CVV: ")
        strategy = CreditCardPayment(card_number, card_holder, cvv)

    elif choice == 2:
        card_number = input("Enter Debit Card Number: ")
        card_holder = input("Enter Card Holder Name: ")
        pin = input("Enter PIN: ")
        strategy = DebitCardPayment(card_number, card_holder, pin)

    elif choice == 3:
        upi_id = input("Enter UPI ID: ")
        strategy = UpiPayment(upi_id)

    elif choice == 4:
        bank_name = input("Enter Bank Name: ")
        account_number = input("Enter Account Number: ")
        strategy = NetBankingPayment(bank_name, account_number)

    else:
        print("Invalid Choice!")
        return

    processor = PaymentProcessor(strategy)
    processor.process_payment(amount)


if __name__ == "__main__":
    main()