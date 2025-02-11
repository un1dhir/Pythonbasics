from abc import ABC,abstractmethod
# encapsulation
class Account:
    def __init__(self,account_id,holder_name,balance):
        self.account_id= account_id
        self.holder_name= holder_name
        self.balance= balance
    def deposit(self,amount):
        self.balance +=amount
    def withdraw(self,amount):
        if amount<= self.balance:
            self.balance -= amount
        else:
            print("Insufficent balance")

    def get_balance(self):
        return self.balance

    def get_holdername(self):
        return self.holder_name
    # inheritance
class Customer(Account):
        def __init__(self,acccount_id,holder_name,balance,phone_number):
            super().__init__(acccount_id,holder_name,balance)
            self.phone_number=phone_number

    # polymorphism
class Transaction:
        def __init__(self,amount):
            self.amount = amount

        def execute(self,account):
            pass
class DepositTransaction(Transaction):
        def execute(self,account):
            account.deposit(self.amount)



    # Abstraction

class PaymentSystem(ABC):
        @abstractmethod
        def process_payment(self,amount):
            pass
class MpesaPaymentSystem(PaymentSystem):
        def process_payment(self,amount):
            print(f"Processing M-pesa payment of {amount}")


    # example usage
mpesa = MpesaPaymentSystem()
account1=Customer(1,"Corleone",1000,7104945231)
deposit=DepositTransaction(1000)
withdraw=Transaction(500)

deposit.execute(account1)
withdraw.execute(account1)
print(f"The balance of {account1.get_holdername()} is :"
      f"{account1.get_balance()}")














