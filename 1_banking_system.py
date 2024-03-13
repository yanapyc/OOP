class TransactionLog:
    def __init__(self):
        self.transactions = []

    def log_transaction(self,transaction_details):
        self.transactions.append(transaction_details)


class CustomerAccount:
    def __init__(self,customer_id,customer_name,account_balance,transaction_log):
        self.customer_id = customer_id
        self.customer_name = customer_name
        self.account_balance = account_balance
        self.transaction_log = transaction_log

    def deposit(self,amount):
        self.account_balance += amount
        transaction_details = f"Deposited {amount}. New balance: {self.account_balance}"
        self.transaction_log.log_transaction(transaction_details)

    def withdraw(self,amount):
        self.account_balance -= amount
        transaction_details = f"Withdrew {amount} New balance: {self.account_balance}"
        self.transaction_log.log_transaction(transaction_details)



transaction_log = TransactionLog()

account = CustomerAccount(7,"Bob Smith", 3000, transaction_log)

account.deposit(300)
account.withdraw(700)
account.deposit(1000)
account.deposit(-200)
account.withdraw(-300)

print("Transaction History:")
for transaction in transaction_log.transactions:
    print(transaction)
