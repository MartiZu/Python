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
            print("\nWithdraw completed of £" + str(amount) + ".")
            self.getBalance()
        except BalanceExeption as error:
            print(f"\nUnable to withdraw: {error}")

    def transfer(self, amount, account):
        try:
            print("\n**********\n\nBeginning transfer..💰")
            self.viableTransaction(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print("\nTransfer completer for £" + str(amount))
        except BalanceExeption as error:
            print(f"\nTransfer interrupted. {error}")

class InterestRewardsAcct(BankAccount):
     def deposit(self, amount):
         self.balance = self.balance + (amount * 1.05)
         print("\nDeposit complete.")
         self.getBalance()

class SavingAcct(InterestRewardsAcct):
    def __init__(self, initialAmount, acctName):
        super().__init__(initialAmount, acctName)
        self.fee = 5

    def withdraw(self, amount):
        try:
            self.viableTransaction(amount + self.fee)
            self.balance = self.balance - (amount + self.fee)
            print("\nWithdraw complete and fee of £" + str(self.fee) + " deducted!")
            self.getBalance()
        except BalanceExeption as error:
            print(f"Withdrawn declined: {error}")