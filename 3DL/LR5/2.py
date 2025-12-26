class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance
    def deposit(self, amount):
        """Пополнить счёт на сумму amount."""
        self.balance += amount
    def withdraw(self, amount):
        """Снять сумму amount, если достаточно средств."""
        if amount > self.balance:
            print("Недостаточно средств!")
        else:
            self.balance -= amount
    def get_balance(self):
        """Вернуть текущий баланс."""
        return self.balance


# Пример использования
account = BankAccount("Ivanov", 100)
account.deposit(50)
account.withdraw(200)  # Ошибка(Потому что недостаточно средств)
account.withdraw(30)
print(account.get_balance())