class Bank:

    def __init__(self, balance: List[int]):
        self.balance = balance
    
    def validate_account(self, account):
        if not(1 <= account <= len(self.balance)):
            return False
        return True

    def validate_account_with_money(self, account, money):
        if not self.validate_account(account) or self.balance[account - 1] < money:
            return False
        return True

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if not self.validate_account_with_money(account1, money) or not self.validate_account(account2):
            return False
        self.balance[account1 - 1] -= money
        self.balance[account2 - 1] += money
        return True

    def deposit(self, account: int, money: int) -> bool:
        if not self.validate_account(account):
            return False
        self.balance[account - 1] += money
        return True

    def withdraw(self, account: int, money: int) -> bool:
        if not self.validate_account_with_money(account, money):
            return False
        self.balance[account - 1] -= money
        return True