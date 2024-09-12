class Bank:
    def __init__(self,accountNumber,Balance):
        self.accountNumber=accountNumber
        self.Balance=Balance
    def debit(self,amount):
        self.Balance=self.Balance-amount
        print(f"The debited amount is {amount}")
        print("The remaining balance is ",self.Balance)
    def credit(self,amount):
        self.Balance+=amount
        print(f"The debited amount is {amount}")
        print("The remaining balance is ",self.Balance)
Customer1=Bank(11,2000)
Customer1.debit(400)
Customer1.credit(1000)