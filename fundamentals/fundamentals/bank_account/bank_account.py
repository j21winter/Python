class Bank_account:
    all_accounts = []

    def __init__(self, balance, interest_rate):
        self.balance = balance
        self.interest_rate = interest_rate
        Bank_account.all_accounts.append(self)
    
    def deposit(self, amount):
        self.balance += amount
        return self
    
    def withdraw(self, amount):
        if self.balance < amount:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
            return self
        else:
            self.balance -= amount
            return self
    
    def display_account_info(self):
        print(f'Balance : ${self.balance}')
        return self
    
    def yield_interest(self):
        if self.balance <= 0:
            return self
        else:
            self.balance = self.balance + (self.balance * self.interest_rate)
            return self
    
    @classmethod
    def display_all_instance_account_info(cls):
        account_number = 0
        for account in cls.all_accounts:
            account_number = account_number + 1
            print(f"\nAccount number: {account_number} \nAccount Balance: ${account.balance} \nAccount Interest Rate: {account.interest_rate * 100}%")


account_1 = Bank_account(0, 0.01)
account_2 = Bank_account(0, 0.05)

account_1.deposit(10).deposit(10).deposit(10).withdraw(5).yield_interest().display_account_info()

account_2.deposit(100).deposit(100).withdraw(25).withdraw(55).withdraw(30).withdraw(100).yield_interest().display_account_info()

Bank_account.display_all_instance_account_info()