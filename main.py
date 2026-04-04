# bank-python-app - версия 5 (с переводами)

def show_balance(balance):
    print(f"💰 Ваш баланс: {balance:.2f} руб.")

def deposit(balance):
    amount = int(input("Сумма пополнения: "))
    if amount <= 0:
        print("❌ Сумма должна быть положительной!")
        return balance
    balance += amount
    print(f"✅ Счёт пополнен на {amount} руб.")
    return balance

def withdraw(balance):
    amount = int(input("Сумма снятия: "))
    if amount <= 0:
        print("❌ Сумма должна быть положительной!")
        return balance
    if amount > balance:
        print("❌ Недостаточно средств!")
        return balance
    balance -= amount
    print(f"✅ Снято {amount} руб.")
    return balance

def transfer(sender_balance, users, sender_name):
    """Перевод денег другому пользователю"""
    recipient = input("👤 Введите логин получателя: ")

    if recipient == sender_name:
        print("❌ Нельзя перевести самому себе!")
        return sender_balance, users

    if recipient not in users:
        print("❌ Пользователь не найден!")
        return sender_balance, users

    amount = int(input("💰 Сумма перевода: "))

    if amount <= 0:
        print("❌ Сумма должна быть положительной!")
        return sender_balance, users

    if amount > sender_balance:
        print("❌ Недостаточно средств!")
        return sender_balance, users

    # Выполняем перевод
    sender_balance -= amount
    users[recipient] += amount

    print(f"✅ Переведено {amount} руб. пользователю {recipient}")
    return sender_balance, users

def bank_menu(username, balance, users):
    """Меню банковских операций"""
    bonus_balance = 0

    while True:
        print(f"\n🏦 Добро пожаловать, {username}!")
        print("1 - Баланс")
        print("2 - Пополнить")
        print("3 - Снять")
        print("4 - Перевести")
        print("5 - Бонусы")
        print("6 - Выйти из аккаунта")

        choice = input("Выберите действие: ")

        if choice == "1":
            print(f"💰 Основной баланс: {balance:.2f} руб.")
            print(f"🎁 Бонусный счёт: {bonus_balance:.2f} руб.")
        elif choice == "2":
            balance = deposit(balance)
        elif choice == "3":
            balance = withdraw(balance)
        elif choice == "4":
            balance, users = transfer(balance, users, username)
        elif choice == "5":
            if bonus_balance <= 0:
                print("🎁 У вас нет бонусов!")
                continue
            print(f"🎁 У вас {bonus_balance:.2f} бонусных рублей.")
            use = input("Использовать бонусы? (да/нет): ")
            if use.lower() == "да":
                balance += bonus_balance
                print(f"✅ Бонусы зачислены! Новый баланс: {balance:.2f} руб.")
                bonus_balance = 0
        elif choice == "6":
            print(f"👋 До свидания, {username}!")
            return balance, users
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
    users[login] = 0
    print(f"✅ Пользователь {login} создан!")
    return users

def main():
    users = {"admin": 10000}

    while True:
        print("\n🏦 Банк 'Ученик'")
        print("1 - Вход")
        print("2 - Регистрация")
        print("3 - Выход")

        choice = input("Выберите действие: ")

        if choice == "1":
            username, balance = login(users)
            if username:
                new_balance, updated_users = bank_menu(username, balance, users)
                users = updated_users
                users[username] = new_balance
        elif choice == "2":
            users = register(users)
        elif choice == "3":
            print("👋 До свидания!")
            break
        else:
            print("❌ Неверный выбор!")

if __name__ == "__main__":
    main()