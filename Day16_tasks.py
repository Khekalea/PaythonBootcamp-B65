class BankAccount:
    def __init__(self,balance):
        self.balance=balance
    def withdraw(self,amt):
        if amt>self.balance:
            raise ValueError('Insufficient Balance')
        self.balance=self.balance-amt
        return self.balance
    
account=BankAccount(5000)

print(account.withdraw(3000))

try:
  print(account.withdraw(30000))
except ValueError as e:
  print('Transaction Failed',e)
finally:
   print('Thank you!!!')

print('------------------------TASK2---------------------')

