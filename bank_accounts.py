class BalanceExeption(Exception):
    pass

class BankAccount:
    def __init__(self, initialAmount, acctName):
        self.balance = initialAmount
        self.name = acctName
        print(f"\nAccount '{self.name}' created.\nBalance = £{self.balance:.2f}")

    #methods
    def getBalance(self):
        print(f"\nAccount '{self.name}' balance = £{self.balance:.2f}")

    def deposit(self, amount):
        self.balance = self.balance + amount
        print(f"\nDeposit complete.")
        self.getBalance()
    
    def viableTransaction(self, amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceExeption(
                f"\nSorry account '{self.name}' only has a balance of £{self.balance:.2f} transaction cannot be completed."
            )
        
    def withdraw(self, amount):
        try:
            self.viableTransaction(amount)
            self.balance = self.balance - amount
            print("\nWithdraw completed.")
            self.getBalance()
        except BalanceExeption as error:
            print(f"\nUnable to withdraw: {error}")