from lesson20_bank_accounts import *

Dave = BankAccount(1000, 'Dave')
Sarah = BankAccount(2000, 'Sarah')

Dave.getBalance()
Sarah.getBalance()

Sarah.deposit(500)
Dave.withdraw(10000)
Sarah.withdraw(150)

Dave.transfer(10000, Sarah)
Dave.transfer(10, Sarah)

Jim = InterestRewardsAcct(1000, "Jim")
Jim.getBalance()
Jim.deposit(100)
Jim.transfer(100, Dave)

Blaze = SavingsAccount(1000,"Blaze")
Blaze.getBalance()
Blaze.deposit(100)
Blaze.transfer(10000,Sarah)
Blaze.transfer(10,Sarah)