class Account:
    def __init__(self,owner, balance):
        self.owner = owner
        self.balance = balance

        print(f"Account owner: {self.owner}")
        print(f"Account balance: ${self.balance}")

    def deposit(self,amount):
        self.balance = self.balance + amount
        print("Deposit Accepted")

    def withdraw(self, wdraw_amount):
        if wdraw_amount > self.balance:
            print("Available balance is low")
        else:
            self.balance = self.balance-wdraw_amount
            print("Withdrawal Accepted")

#Instantiate the class
acct1 = Account('Jose', 100)

#print the object
print(acct1)

#show account owner attribute
print(acct1.owner)

#show account balance attribute
print(acct1.balance)

#make a series of deposit and withdrawal
acct1.deposit(50)

acct1.withdraw(75)

#make a withdrawal that exceeds the available balance
acct1.withdraw(500)


        
