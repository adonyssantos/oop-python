class BankAccount:

    def set_details(self, name, balance):
        self.name = name
        self.balance = balance

    def get_balance(self):
        return f"{self.name} has {self.balance} dollars."

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if self.balance < amount:
            return "Insufficient funds"
        else:
            self.balance -= amount
            return self.balance


# create account
adonys_bank = BankAccount()

# set account details
adonys_bank.set_details("Adonys", 0)

# get account balance
print(adonys_bank.get_balance())

# deposit money and get new balance
adonys_bank.deposit(100)
print(adonys_bank.get_balance())

# withdraw money and get new balance
adonys_bank.withdraw(50)
print(adonys_bank.get_balance())

# withdraw more money than available
print(adonys_bank.withdraw(500))
