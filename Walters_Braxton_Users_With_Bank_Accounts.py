class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        # creating a list of bank accounts for each instance
        self.accounts = []
    
    # creating a new account 
    def new_account(self, account_name):
        # add the account to the instance's account list
        self.accounts.append(BankAccount(account_name))
    
    def make_deposit(self, amount, account_name):
        # need to check the the accounts list and compare it to the given account name
        for account in self.accounts:
            if account.account_name == account_name:
                # Once we have the account we have to call the deposit function in the bank account class. 
                account.deposit(amount)
                # else print that the account name is wrong.
        return self
    
    def make_withdraw(self, amount, account_name):
        for account in self.accounts:
            if account.account_name == account_name:
                account.withdraw(amount)
        return self

    def account_balance(self, account_name):
        for account in self.accounts:
            if account.account_name == account_name:
                account.display_account_info()
        return self
    
    # def transfer(self, amount, account_name): 
        

class BankAccount:
    instances = []

    def __init__(self, account_name, int_rate = 0.01, balance = 0):
        BankAccount.instances.append(self) 
        self.account_name = account_name
        self.int_rate = int_rate 
        self.balance = balance 

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        else:
            self.balance -= amount
        return self

    def display_account_info(self):
        print(self.balance)
        print(self.int_rate)
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance += (self.int_rate * self.balance)
        return self
    
    @classmethod
    def all_instances(cls):
        for instance in cls.instances:
            print(f"Balance-{instance.balance}, Interest rate-{instance.int_rate}")
            
braxton = User("braxton", "bob@gmail.com")
robby = User("Robby", "robby@gmail.com")


print(dir(braxton.accounts))













# braxton.new_account("savings")
# braxton.account_balance("savings")
# print("-" * 10)
# braxton.make_deposit(69, "savings")
# braxton.account_balance("savings")
# print("-" * 10)
# braxton.make_withdraw(9, "savings")
# braxton.account_balance("savings")
# print("-" * 10)
# braxton.new_account("checking")
# braxton.account_balance("checking")
# print("-" * 10)
# braxton.make_deposit(420, "checking")
# braxton.account_balance("checking")
# print("-" * 10)
# braxton.account_balance("savings")


