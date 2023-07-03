# What do they mean buy "use a classmethod to print all instances of a Bank Account's info". Do they want the mem location or the interest rates and balances? If the latter, how should it be formatted? Please give me some feedback thanks!
class BankAccount:
    instances = [] # This is a class arr right?

    def __init__(self, int_rate = 0.01, balance = 0):
        BankAccount.instances.append(self) #--do they want this?--
        self.int_rate = int_rate
        # BankAccount.instances.append(self.int_rate) # I don't feel like these are it 
        self.balance = balance 
        # BankAccount.instances.append(self.balance)

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        else:
            self.balance += amount
        return self

    def display_account_info(self):
        print(self.balance)
        print(self.int_rate)
        return self

    def yield_interest(self): # Is this even right? Do they want the interest rate % or number after the calculation shown?
        if self.balance > 0:
            self.balance += (self.int_rate * self.balance)
        return self
    # Where should a class method go? Should it go below or above every method or does it not matter?
    @classmethod
    def all_instances(cls):
        for instance in cls.instances:
            print(f"Balance-{instance.balance}, Interest rate-{instance.int_rate}")



account_1 = BankAccount().deposit(10).deposit(20).deposit(30).withdraw(50).yield_interest().display_account_info()
account_2 = BankAccount().deposit(100).deposit(100).withdraw(20).withdraw(20).withdraw(20).withdraw(20).yield_interest().display_account_info()
print("-" * 80)
BankAccount.all_instances()
