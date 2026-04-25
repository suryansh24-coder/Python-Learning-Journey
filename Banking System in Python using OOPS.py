## WAP to create account class with 2 attributes - balance & account no. create methodes for debit , credit & printing the balance :- 
class account:
    def __init__(self,balance,accNum):
        self.balance = balance
        self.an = accNum
        
    # Debit Methode
    def debit(self, ammount):
        self.balance -= ammount
        print("Rs.",ammount,"was debited")
        print("Total Balance : \t",self.get_Balance)
        
    # Credit Methode
    
    def credit(self, ammount):
        self.balance += ammount
        print("Rs.",ammount,"was credited")    
        
    # Show Balance
    def get_Balance(self):
        return self.balance
    
acc1 = account(1000,12345)
print(acc1.balance)
print(acc1.an)
acc1.debit(1000)
acc1.credit(100)
