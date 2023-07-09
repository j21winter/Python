class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.saving_account = Bank_account(0, 0.01, 'saving')
        self.checking_account = Bank_account(0, 0.04, 'checking')
        print(f'{self.name} created')
    
    def make_deposit(self, account_type, amount):
        if account_type == 'checking':
            self.checking_account.deposit(amount)
            return self
        else:
            self.saving_account.deposit(amount)
            return self
    
    def make_withdrawal(self, account_type, amount):
        if account_type == 'checking':
            self.checking_account.withdraw(amount)
            return self
        else:
            self.saving_account.withdraw(amount)
            return self
    
    def display_account_balance(self, account_type):
        print(f'\n{self.name}')
        if account_type == 'checking':
            self.checking_account.display_account_info()
            return self
        else:
            self.saving_account.display_account_info()
            return self
    
    def transfer_money(self, amount, receiving_party, account_type):
        self.make_withdrawal(account_type, amount)
        receiving_party.make_deposit('checking', amount)
        print(f'\nTransferring ${amount} from {self.name}: {account_type} account to {receiving_party.name}: checking account.')


class Bank_account:
    all_accounts = []

    def __init__(self, balance, interest_rate, account_type):
        self.balance = balance
        self.interest_rate = interest_rate
        self.account_type = account_type
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
        print(f'{self.account_type} account balance : ${self.balance}')
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

user_1 = User('user_1', 'user1@email.com')
user_2 = User('user_2', 'user2@email.com')

user_1.make_deposit('checking',100).display_account_balance('checking').make_deposit('saving',200).display_account_balance('saving').transfer_money(50, user_2, 'saving')
user_2.display_account_balance('checking').make_deposit('saving', 50).display_account_balance('checking').display_account_balance('saving')