# mixins.py - переиспользуемые миксины

from datetime import datetime
import re

class LoggerMixin:
    """Миксин для логирования операций"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._logs = []

    def log(self, message):
        timestamp = datetime.now().strftime("%H:%M:%S")
        log_entry = f"[{timestamp}] {message}"
        self._logs.append(log_entry)
        print(f"📝 {log_entry}")

    def get_logs(self, last_n=None):
        if last_n:
            return self._logs[-last_n:]
        return self._logs

    def show_logs(self, last_n=10):
        if not self._logs:
            print("📭 История операций пуста")
            return
        print(f"\n📜 ПОСЛЕДНИЕ ОПЕРАЦИИ (последние {min(last_n, len(self._logs))}):")
        print("-" * 50)
        for log in self._logs[-last_n:]:
            print(f"   {log}")
        print("-" * 50)


class BonusMixin:
    """Миксин для бонусной системы"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._bonus_balance = 0.0
        self._bonus_rate = 0.01  # 1% бонуса от пополнения

    def calculate_bonus(self, amount):
        return amount * self._bonus_rate

    def add_bonus(self, amount):
        bonus = self.calculate_bonus(amount)
        self._bonus_balance += bonus
        self.log(f"🎁 Начислено бонусов: {bonus:.2f} руб.")
        return bonus

    def get_bonus_balance(self):
        return self._bonus_balance

    def use_bonus(self):
        if self._bonus_balance <= 0:
            raise ValueError("Нет бонусов для использования!")

        amount = self._bonus_balance
        self._bonus_balance = 0
        self.log(f"🎁 Использовано бонусов: {amount:.2f} руб.")
        return amount


class TimestampMixin:
    """Миксин для добавления временных меток"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.created_at = datetime.now()

    def get_age(self):
        """Возвращает возраст объекта в секундах"""
        delta = datetime.now() - self.created_at
        return delta.total_seconds()

    def get_created_date(self):
        return self.created_at.strftime("%d.%m.%Y %H:%M:%S")


class IDMixin:
    """Миксин для генерации уникальных ID"""

    _counter = 0

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        IDMixin._counter += 1
        self._id = IDMixin._counter

    @property
    def id(self):
        return self._id


class ValidationMixin:
    """Миксин для валидации данных"""

    @staticmethod
    def validate_phone(phone):
        cleaned = re.sub(r'[\s\-\(\)]', '', phone)
        return bool(re.match(r"^\+7\d{10}$", cleaned))

    @staticmethod
    def validate_email(email):
        pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        return bool(re.match(pattern, email))

    @staticmethod
    def validate_amount(amount):
        return amount > 0