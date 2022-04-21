class BankAccount:

    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    def get_balance(self):
        return f"{self.name} has {self.__balance} dollars."

    def deposit(self, amount):
        self.__balance += amount
        return self.__balance

    def withdraw(self, amount):
        if self.__balance < amount:
            return "Insufficient funds"
        else:
            self.__balance -= amount
            return self.__balance


# create account
adonys_bank = BankAccount("Adonys", 100)

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
