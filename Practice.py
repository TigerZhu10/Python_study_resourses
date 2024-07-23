import pygame

class BankAccount:
    def __init__(self):
        self.balance = 0

    def deposit(self, cash):
        self.balance += cash
        

    def withdraw(self):
        pass
    
    def check_balance(self):
        return self.balance

    def transfer(self):
        pass

Tiger_account = BankAccount()
Tiger_account.deposit(500)
print(Tiger_account.check_balance())