class BankAccount:
    list_accounts = []

    def __init__(self, opening_val):
        self.percent_rate = 0.01
        if  opening_val > 0:
            self.balance = opening_val
        else:
            self.balance = 0
        BankAccount.list_accounts.append(self)
        
    def deposit(self, amount):
        self.balance = self.balance + amount
        return self

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance = self.balance - amount
            return self
        else:
            print("Insufficient funds: charging a $5 fee.")
            self.balance = self.balance - 5
            return self

    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance = self.balance + (self.balance * self.percent_rate)
        return self

    @classmethod
    def print_all_info(cls):
        for x in range(0,len(cls.list_accounts)):
            print(f"Balance: ${cls.list_accounts[x].balance}")        


account1 = BankAccount(50)
account2 = BankAccount(0)

account1.deposit(15).deposit(25).deposit(100).withdraw(52).yield_interest().display_account_info()
account2.deposit(10).deposit(50).withdraw(10).withdraw(15).withdraw(35).withdraw(10).yield_interest().display_account_info()
BankAccount.print_all_info()