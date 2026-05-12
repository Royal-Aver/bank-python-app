# storage.py - слой хранения данных

from models import User, BankAccount

class Storage:
    """
    Временное хранилище в памяти.
    Позже заменим на PostgreSQL.
    """

    def __init__(self):
        self.users = {}
        self.accounts = {}
        self._next_id = 1

    def add_user(self, user: User):
        """Добавить пользователя"""
        if user.email in self.users:
            raise ValueError(f"Пользователь с email {user.email} уже существует!")
        self.users[user.email] = user
        return user

    def get_user_by_email(self, email):
        """Получить пользователя по email"""
        return self.users.get(email)

    def get_all_users(self):
        """Получить всех пользователей"""
        return list(self.users.values())

    def add_account(self, account: BankAccount):
        """Добавить счёт"""
        self.accounts[account.id] = account
        return account

    def get_account_by_id(self, account_id):
        """Получить счёт по ID"""
        return self.accounts.get(account_id)

    def get_accounts_by_user(self, user_email):
        """Получить все счета пользователя"""
        return [acc for acc in self.accounts.values() if acc.user.email == user_email]

    def get_all_accounts(self):
        """Получить все счета"""
        return list(self.accounts.values())

    def transfer(self, from_account_id, to_account_id, amount):
        """Перевод между счетами"""
        from_account = self.get_account_by_id(from_account_id)
        to_account = self.get_account_by_id(to_account_id)

        if not from_account or not to_account:
            raise ValueError("Счёт не найден!")

        return from_account.transfer(to_account, amount)