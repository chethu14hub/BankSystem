class Account:
    def __init__(self,id,holder_name,balance):
        self.id=id
        self.holder_name=holder_name
        self._balance=0

    def check_balance(self):
        print(f"Your balance is{self._balance}")
    
    def deposite(self,amount):
        amount=int(input("Enter the amount to deposit"))
        self._balance+=amount
        print(f"Your balance is {self._balance}")
    
    def withdraw(self,amount):
        if(amount>=0):
            print("Insufficant balance")
        else:
            amount=int(input("Enter the amount to withdraw"))
            self._balance-=amount
            print(f"Your balance is {self._balance}")
        
class account:
    def __init__(self,Deposit="",check_bal=""):
       self.Deposit=Deposit
       self.check_bal=check_bal

    def deposit(self):
        Balance=[]
        amount=int(input("Enter the amount to deposit"))
        Balance.append(amount)
        print(f"Your balance is {Balance}")
    
bnk=bank()
bnk.create_ac()
bnk.display()
ac=account()
ac.deposit()