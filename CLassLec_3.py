class BankAccount:
    def __init__(self, money):
        self.amount = money

    def transfer(self, target_account, transfer_amount):
        target_account.amount += transfer_amount
        self.amount -= transfer_amount
        
        

Alex_account = BankAccount(500)
Tiger_account = BankAccount(800)

Tiger_account.transfer(Alex_account ,200)

print(Alex_account.amount)
print(Tiger_account.amount)