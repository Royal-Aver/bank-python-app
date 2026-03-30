# bank-python-app - версия 2
print("🏦 Банк 'Ученик'")

balance = 5000  # начальный баланс

while True:
    print("\n1 - Проверить баланс")
    print("2 - Пополнить счет")
    print("3 - Снять деньги")
    print("4 - Выйти")

    choice = input("Ваш выбор: ")

    if choice == "1":
        print(f"💰 Ваш баланс: {balance} руб.")
    elif choice == "2":
        amount = int(input("Сколько внести? "))
        if amount <= 0:
            print("❌ Сумма должна быть положительной!")
        else:
            balance += amount
            print(f"✅ Счет пополнен. Новый баланс: {balance} руб.")
    elif choice == "3":
        amount = int(input("Сколько снять? "))
        if amount <= 0:
            print("❌ Сумма должна быть положительной!")
        elif amount > balance:
            print("❌ Недостаточно средств!")
        else:
            balance = balance - amount
            print(f"✅ Снято {amount} руб. Новый баланс: {balance} руб.")
    elif choice == "4":
        print("👋 До свидания!")
        break
    else:
        print("❌ Неверный выбор. Попробуйте снова.")