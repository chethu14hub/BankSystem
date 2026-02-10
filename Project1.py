import uuid
class Account:
    def __init__(self,id,holder_name,balance=""):
        self.id=id
        self.holder_name=holder_name
        self._balance=0

    def check_balance(self):
        print(f"Your balance is {self._balance}")
    
    def deposite(self,amount=""):
        amount=int(input("Enter the amount to deposit"))
        self._balance+=amount
        print(f"Your balance is {self._balance}")
    
    def withdraw(self,amount):
        if(amount<=0):
            print("Insufficant balance")
        else:
            amount=int(input("Enter the amount to withdraw"))
            self._balance-=amount
            print(f"Your balance is {self._balance}")
        
class SavingAccount(Account):
    def intrest(self):
        INTREST_RATE=0.4
        print(f"Intrest is {INTREST_RATE*self._balance}")

class CurretAccount(Account):
    
    def withdraw(self,amount):
        OVERDRAFT=1000
        self._balance-=amount
        while(self._balance==-1000):
            break
  
        
class bank(Account):
    def __init__(self,name,location):
        self.name=name
        self.location=location
    def createAcount(self,id,type,name):
        self.db={}
        if type=="SavingAccount":
            SavingAccount(id,name)
            self.db[id]=name
            print("Acount created done")
            print(self.db)
            
        
            return Account
        elif type=="CurretAccount":
            CurretAccount(id,name)
            self.db[id]=name
            print("Acount creaed done")
            return Account
    def getAccountDetails(self,id):
            if id in self.db:
                print(f"Account details for id {id} is {self.db[id]}")
            else:
                print("Account not found")
        
bnk=bank(name=input("Enter the name of bank"),location=input("Enter the location"))
bnk.createAcount(id=int(input("Enter the id")),type=input("Enter the type of account"),name=input("Enter the name of account holder"))
ac=Account("id1","Chethan")
ac.deposite()
ac.check_balance()
ac.withdraw(100)
bnk.getAccountDetails(id=int(input("Enter the id to get account details")))

