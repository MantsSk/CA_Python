class BankAccount:
    def __init__(self, account_number, initial_balance=0):
        self.account_number = account_number
        self.balance = initial_balance

    def deposit(self, amount):
        if amount <= 0:
            return "Invalid deposit amount"
        self.balance += amount
        return "Deposit successful"

    def withdraw(self, amount):
        if amount <= 0:
            return "Invalid withdrawal amount"
        if amount > self.balance:
            return "Insufficient funds"
        self.balance -= amount
        return "Withdrawal successful"

    def get_balance(self):
        return self.balance


# Create a bank account object
account = BankAccount("1234567890")

# Deposit funds
print(account.deposit(1000))

# Withdraw funds
print(account.withdraw(300))


# Check account balance
balance = account.get_balance()
print("Account Balance:", balance)
