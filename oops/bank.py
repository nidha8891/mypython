class bank:
    acno=int
    balance=int
    ac_type=str
    p_name=str

    def create_account(self,acno,bal,ac_type,p_name):
        self.acno=acno
        self.balance=bal
        self.ac_type=ac_type
        self.p_name=p_name

    def deposit(self ,amount):
            self.balance+=amount
            print(f"your sbk account {self.acno} has been debited with amount {amount} aval bal is {self.balance}")


    def withdraw(self,amount):
         if self.balance >= amount:
              self.balance-=amount
              print(f"your sbk account {self.acno} has been debited with amount {amount} aval bal is {self.balance}")
         else:
              print("transaction faild insufficient bal")


obj1=bank()
obj1.create_account(100,2000,"savings","nidha")
obj1.withdraw(1000)

