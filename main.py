# bank-python-app - версия 6 (с историей операций)

from datetime import datetime

def get_timestamp():
    """Возвращает текущую дату и время в формате ДД.ММ.ГГГГ ЧЧ:ММ:СС"""
    return datetime.now().strftime("%d.%m.%Y %H:%M:%S")

def add_to_history(user_data, operation, amount, recipient=None):
    """Добавляет запись в историю пользователя"""
    time_str = get_timestamp()

    if recipient:
        record = f"[{time_str}] {operation}: {amount} руб. → {recipient}"
    else:
        record = f"[{time_str}] {operation}: {amount} руб."

    user_data["history"].append(record)

def show_balance(user_data):
    print(f"💰 Ваш баланс: {user_data['balance']:.2f} руб.")

def deposit(user_data):
    amount = int(input("Сумма пополнения: "))
    if amount <= 0:
        print("❌ Сумма должна быть положительной!")
        return user_data

    user_data["balance"] += amount
    add_to_history(user_data, "ПОПОЛНЕНИЕ", amount)
    print(f"✅ Счёт пополнен на {amount} руб.")
    return user_data

def withdraw(user_data):
    amount = int(input("Сумма снятия: "))
    if amount <= 0:
        print("❌ Сумма должна быть положительной!")
        return user_data
    if amount > user_data["balance"]:
        print("❌ Недостаточно средств!")
        return user_data

    user_data["balance"] -= amount
    add_to_history(user_data, "СНЯТИЕ", amount)
    print(f"✅ Снято {amount} руб.")
    return user_data

def transfer(user_data, users, sender_name):
    """Перевод денег другому пользователю"""
    recipient = input("👤 Введите логин получателя: ")

    if recipient == sender_name:
        print("❌ Нельзя перевести самому себе!")
        return user_data, users

    if recipient not in users:
        print("❌ Пользователь не найден!")
        return user_data, users

    amount = int(input("💰 Сумма перевода: "))

    if amount <= 0:
        print("❌ Сумма должна быть положительной!")
        return user_data, users

    if amount > user_data["balance"]:
        print("❌ Недостаточно средств!")
        return user_data, users

    # Выполняем перевод
    user_data["balance"] -= amount
    users[recipient]["balance"] += amount

    # Добавляем в историю обоим пользователям
    add_to_history(user_data, "ПЕРЕВОД", amount, recipient)
    add_to_history(users[recipient], "ПОЛУЧЕНИЕ", amount, sender_name)

    print(f"✅ Переведено {amount} руб. пользователю {recipient}")
    return user_data, users

def show_history(user_data):
    """Показывает историю операций пользователя"""
    history = user_data.get("history", [])

    if not history:
        print("📭 История пуста")
        return

    print("\n📜 ИСТОРИЯ ОПЕРАЦИЙ:")
    print("-" * 50)
    for record in history:
        print(record)
    print("-" * 50)

def bank_menu(username, user_data, users):
    """Меню банковских операций"""
    bonus_balance = 0

    while True:
        print(f"\n🏦 Добро пожаловать, {username}!")
        print("1 - Баланс")
        print("2 - Пополнить")
        print("3 - Снять")
        print("4 - Перевести")
        print("5 - История операций")
        print("6 - Бонусы")
        print("7 - Выйти из аккаунта")

        choice = input("Выберите действие: ")

        if choice == "1":
            show_balance(user_data)
            print(f"🎁 Бонусный счёт: {bonus_balance:.2f} руб.")
        elif choice == "2":
            user_data = deposit(user_data)
        elif choice == "3":
            user_data = withdraw(user_data)
        elif choice == "4":
            user_data, users = transfer(user_data, users, username)
        elif choice == "5":
            show_history(user_data)
        elif choice == "6":
            if bonus_balance <= 0:
                print("🎁 У вас нет бонусов!")
                continue
            print(f"🎁 У вас {bonus_balance:.2f} бонусных рублей.")
            use = input("Использовать бонусы? (да/нет): ")
            if use.lower() == "да":
                user_data["balance"] += bonus_balance
                add_to_history(user_data, "БОНУСЫ", bonus_balance)
                print(f"✅ Бонусы зачислены! Новый баланс: {user_data['balance']:.2f} руб.")
                bonus_balance = 0
        elif choice == "7":
            print(f"👋 До свидания, {username}!")
            return user_data, users
        else:
            print("❌ Неверный выбор!")

def login(users):
    login = input("👤 Введите логин: ")
    if login in users:
        print(f"✅ Добро пожаловать, {login}!")
        return login, users[login]
    else:
        print("❌ Пользователь не найден!")
        return None, None

def register(users):
    login = input("📝 Придумайте логин: ")
    if login in users:
        print("❌ Такой логин уже существует!")
        return users

    users[login] = {
        "balance": 0,
        "history": []
    }
    print(f"✅ Пользователь {login} создан!")
    return users

def main():
    users = {
        "admin": {
            "balance": 10000,
            "history": [f"[{get_timestamp()}] СИСТЕМА: аккаунт создан"]
        },
        "Fedia": {
            "balance": 1000,
            "history": [f"[{get_timestamp()}] СИСТЕМА: аккаунт создан"]
        }
    }

    while True:
        print("\n🏦 Банк 'Ученик'")
        print("1 - Вход")
        print("2 - Регистрация")
        print("3 - Выход")

        choice = input("Выберите действие: ")

        if choice == "1":
            username, user_data = login(users)
            if username:
                updated_user, updated_users = bank_menu(username, user_data, users)
                users[username] = updated_user
                users = updated_users
        elif choice == "2":
            users = register(users)
        elif choice == "3":
            print("👋 До свидания!")
            break
        else:
            print("❌ Неверный выбор!")

if __name__ == "__main__":
    main()