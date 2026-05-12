# models.py - классы пользователя и банковского счёта

from datetime import datetime
from mixins import (
    LoggerMixin, BonusMixin, TimestampMixin,
    IDMixin, ValidationMixin
)

class User(ValidationMixin):
    """
    Класс пользователя банка.
    Использует только ValidationMixin для проверки данных.
    """

    def __init__(self, name, email, phone):
        # Проверяем данные перед созданием
        if not self.validate_email(email):
            raise ValueError(f"Неверный формат email: {email}")
        if not self.validate_phone(phone):
            raise ValueError(f"Неверный формат телефона: {phone}")

        self.name = name
        self.email = email
        self.phone = phone
        self.created_at = datetime.now()
        self.is_active = True

    def __str__(self):
        return f"User(name='{self.name}', email='{self.email}')"

    def __repr__(self):
        return f"User('{self.name}', '{self.email}', '{self.phone}')"


class BankAccount(LoggerMixin, BonusMixin, TimestampMixin, IDMixin):
    """
    Основной класс банковского счёта.
    Собирает все миксины: логирование, бонусы, временные метки, ID.
    """

    def __init__(self, user: User, initial_balance=0):
        # Инициализация всех миксинов через super()
        super().__init__()

        self.user = user
        self._balance = float(initial_balance)

        self.log(f"🏦 Создан счёт для {user.name} с балансом {self._balance:.2f} руб.")

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        """Сеттер с проверкой — баланс не может быть отрицательным"""
        if value < 0:
            raise ValueError("Баланс не может быть отрицательным!")
        self._balance = value

    def deposit(self, amount):
        """Пополнение счёта"""
        if amount <= 0:
            self.log("❌ Ошибка: сумма должна быть положительной!")
            return False

        self._balance += amount
        bonus = self.add_bonus(amount)
        self.log(f"✅ Пополнение: +{amount:.2f} руб.")
        return True

    def withdraw(self, amount):
        """Снятие денег"""
        if amount <= 0:
            self.log("❌ Ошибка: сумма должна быть положительной!")
            return False

        if amount > self._balance:
            self.log(f"❌ Ошибка: недостаточно средств! Доступно: {self._balance:.2f} руб.")
            return False

        self._balance -= amount
        self.log(f"💰 Снятие: -{amount:.2f} руб.")
        return True

    def transfer(self, target_account, amount):
        """Перевод на другой счёт"""
        if not isinstance(target_account, BankAccount):
            self.log("❌ Ошибка: получатель должен быть объектом BankAccount")
            return False

        if amount <= 0:
            self.log("❌ Ошибка: сумма перевода должна быть положительной!")
            return False

        if amount > self._balance:
            self.log(f"❌ Ошибка: недостаточно средств для перевода!")
            return False

        # Выполняем перевод
        self._balance -= amount
        target_account._balance += amount

        self.log(f"💸 Перевод: -{amount:.2f} руб. → {target_account.user.name}")
        target_account.log(f"💸 Получен перевод: +{amount:.2f} руб. от {self.user.name}")
        return True

    def use_bonus(self):
        """Использовать бонусы для пополнения счёта"""
        try:
            bonus_amount = super().use_bonus()
            self._balance += bonus_amount
            self.log(f"✅ Бонусы зачислены на счёт: +{bonus_amount:.2f} руб.")
            return True
        except ValueError as e:
            self.log(f"❌ {e}")
            return False

    def show_info(self):
        """Показать полную информацию о счёте"""
        print(f"\n🏦 ИНФОРМАЦИЯ О СЧЁТЕ")
        print("=" * 40)
        print(f"👤 Владелец: {self.user.name}")
        print(f"📧 Email: {self.user.email}")
        print(f"📱 Телефон: {self.user.phone}")
        print(f"🆔 ID счёта: {self.id}")
        print(f"💰 Баланс: {self._balance:.2f} руб.")
        print(f"🎁 Бонусный счёт: {self.get_bonus_balance():.2f} руб.")
        print(f"📅 Создан: {self.get_created_date()}")
        print("=" * 40)

    def __str__(self):
        return f"Создан счет #{self.id} на имя {self.user.name}. Начальный баланс: {self.balance:.2f}"

    def __repr__(self):
        return f"BankAccount('{self.user.name}', {self.balance})"

    def __add__(self, other):
        """Сложение счетов — сумма балансов"""
        if isinstance(other, BankAccount):
            return self.balance + other.balance
        return NotImplemented

    def __bool__(self):
        """Счёт считается истинным, если на нём есть деньги"""
        return self.balance > 0