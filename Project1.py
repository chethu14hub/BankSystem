class bank:
    def __init__(self,name="",city="",ac_number=""):
        self.name=name
        self.city=city
        self.ac_number=ac_number

    def create_ac(self):
        self.name=input("Enter your name ")
        self.city=input("Enter your city ")
        self.ac_number=int(input("Enter your account number "))
        
    def display(self):
        print("Account details")
        print(f"{self.name}\n{self.city}\n{self.ac_number}\n")
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