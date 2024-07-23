class BankAccount:
    def __init__(self):
        self.balance = 0
        self.balance_is_enough = False

    def deposit(self, amount):
        self.balance += amount
        if self.balance > 0:
            self.balance_is_enough = True


    def withdraw(self, amount):
        #? 如果要取的钱 小于 余额 执行当前if 
        if amount < self.balance:
            self.balance_is_enough = True
            self.balance -= amount
        else:
            self.balance_is_enough = False
        
    def check_balance(self):
        if self.balance_is_enough == True:
            return self.balance
        else:
            return "Balance is not enough"
        
    def transfer(self, amount, target_account):
        self.withdraw(amount)
        target_account.balance += amount
        if target_account.balance > 0:
            target_account.balance_is_enough = True
        

Tiger = BankAccount()
Alex = BankAccount()

Tiger.deposit(500)
print(Tiger.check_balance())
Tiger.withdraw(200)
Tiger.transfer(300, Alex)
print(Tiger.check_balance())
print(Alex.check_balance())
