from bank_accounts import *

Martina = BankAccount(2000, "Martina Zurli")
Alex = BankAccount(5000, "Alejandro Saez")

Martina.getBalance()
Alex.getBalance()

Martina.deposit(500)
Alex.deposit(270)

Martina.withdraw(10000)
Alex.withdraw(500)
Alex.withdraw(500)

Martina.transfer(50000, Alex)
Alex.transfer(200, Martina)

Mum = InterestRewardsAcct(1000, "Mum")

Mum.getBalance()
Mum.deposit(100)
Mum.transfer(200, Martina)

Dad = SavingAcct(1000, "Dad")

Dad.getBalance()
Dad.deposit(100)
Dad.transfer(1000, Mum)