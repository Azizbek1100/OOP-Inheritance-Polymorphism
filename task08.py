class BankAccount:
    def withdraw(self, amount):
        return f"Withdraw {amount}"

class SavingsAccount(BankAccount):
    def get_interest(self):
        return "Interest rate: 6%"

class CheckingAccount(BankAccount):
    def get_interest(self):
        return "No interest for checking account"

accounts = [SavingsAccount(), CheckingAccount()]
for a in accounts:
    print(a.get_interest())
    print(a.withdraw(100))