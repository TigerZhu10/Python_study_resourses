import pygame

class BankAccount:
    def __init__(self):
        self.balance = 0
        self.check_money = False

    def deposit(self, cash):
        self.balance += cash
        self.check_money = True
        
        

    def withdraw(self,cash):
        if cash < self.balance: 
            self.balance -= cash
            self.check_money = True
        else:
            self.check_money = False
    
    def check_balance(self):
        if self.check_money == True:
            return self.balance
        else:
            return("You are poor")

    def transfer(self, cash, target_account):
        if self.balance >= cash:
            target_account.balance += cash
            self.withdraw(cash)

        if target_account.balance > 0:
            target_account.check_money = True
        self.withdraw(cash)

        

Tiger_account = BankAccount()
Alex_account = BankAccount()

Tiger_account.deposit(500)
print(Tiger_account.check_balance())
Tiger_account.withdraw(200)
print(Tiger_account.check_balance())
Tiger_account.transfer(300, Alex_account)
print(Alex_account.check_balance())




