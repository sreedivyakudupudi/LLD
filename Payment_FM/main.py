from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

class CreditCardPayment(Payment):
    def process_payment(self, amount):
        print(f"\nProcessing credit card payment of ${amount}")

class UPIPayment(Payment):
    def process_payment(self, amount):
        print(f"\nProcessing UPI payment of ${amount}")

class DebitCardPayment(Payment):
    def process_payment(self, amount):
        print(f"\nProcessing debit card payment of ${amount}")

class PaymentCreator(ABC):
    @abstractmethod
    def create_payment(self):
        pass
    
    def process_payment(self, amount):
        if(amount<0):
            raise ValueError("Amount cannot be negative")
        payment = self.create_payment()
        payment.process_payment(amount)
        print("Payment processed successfully.\n")

class CreditCardPaymentCreator(PaymentCreator):
    def create_payment(self):
        return CreditCardPayment()

class UPIPaymentCreator(PaymentCreator):    
    def create_payment(self):
        return UPIPayment()

class DebitCardPaymentCreator(PaymentCreator):
    def create_payment(self):
        return DebitCardPayment()

def main():
    # Example usage
    credit_card_creator = CreditCardPaymentCreator()
    credit_card_creator.process_payment(100)

    upi_creator = UPIPaymentCreator()
    upi_creator.process_payment(200)

    debit_card_creator = DebitCardPaymentCreator()
    debit_card_creator.process_payment(300)

if __name__ == "__main__":
    main()
