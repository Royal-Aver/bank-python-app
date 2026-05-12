# services.py - бизнес-логика приложения

from models import User, BankAccount
from storage import Storage

class BankService:
    """Сервис для работы с банковскими операциями"""

    def __init__(self):
        self.storage = Storage()

    def register_user(self, name, email, phone):
        """Регистрация нового пользователя"""
        try:
            user = User(name, email, phone)
            self.storage.add_user(user)
            print(f"✅ Пользователь {name} успешно зарегистрирован!")
            return user
        except ValueError as e:
            print(f"❌ Ошибка регистрации: {e}")
            return None

    def create_account(self, user_email, initial_balance=0):
        """Создание банковского счёта для пользователя"""
        user = self.storage.get_user_by_email(user_email)
        if not user:
            print(f"❌ Пользователь с email {user_email} не найден!")
            return None

        if initial_balance < 0:
            print("❌ Начальный баланс не может быть отрицательным!")
            return None

        account = BankAccount(user, initial_balance)
        self.storage.add_account(account)
        print(f"✅ Счёт создан! ID: {account.id}")
        return account

    def get_accounts(self, user_email):
        """Получить все счета пользователя"""
        return self.storage.get_accounts_by_user(user_email)

    def deposit(self, account_id, amount):
        """Пополнение счёта"""
        account = self.storage.get_account_by_id(account_id)
        if not account:
            print(f"❌ Счёт {account_id} не найден!")
            return False
        return account.deposit(amount)

    def withdraw(self, account_id, amount):
        """Снятие со счёта"""
        account = self.storage.get_account_by_id(account_id)
        if not account:
            print(f"❌ Счёт {account_id} не найден!")
            return False
        return account.withdraw(amount)

    def transfer(self, from_id, to_id, amount):
        """Перевод между счетами"""
        try:
            return self.storage.transfer(from_id, to_id, amount)
        except ValueError as e:
            print(f"❌ {e}")
            return False

    def use_bonus(self, account_id):
        """Использовать бонусы"""
        account = self.storage.get_account_by_id(account_id)
        if not account:
            print(f"❌ Счёт {account_id} не найден!")
            return False
        return account.use_bonus()

    def show_account_info(self, account_id):
        """Показать информацию о счёте"""
        account = self.storage.get_account_by_id(account_id)
        if not account:
            print(f"❌ Счёт {account_id} не найден!")
            return
        account.show_info()

    def show_account_logs(self, account_id, last_n=10):
        """Показать историю операций счёта"""
        account = self.storage.get_account_by_id(account_id)
        if not account:
            print(f"❌ Счёт {account_id} не найден!")
            return
        account.show_logs(last_n)

    def list_all_accounts(self):
        """Показать все счета в системе"""
        accounts = self.storage.get_all_accounts()
        if not accounts:
            print("📭 Нет зарегистрированных счетов")
            return

        print("\n🏦 ВСЕ СЧЕТА В СИСТЕМЕ")
        print("=" * 50)
        for acc in accounts:
            print(f"ID: {acc.id} | {acc.user.name} | Баланс: {acc.balance:.2f} руб.")
        print("=" * 50)