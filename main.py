# bank-python-app - версия 3 (с функциями)
def show_balance(balance):
    """Показывает баланс"""
    print(f"💰 Ваш баланс: {balance} руб.")

def deposit(balance):
    """Пополнение счёта"""
    amount = int(input("Сумма пополнения: "))
    if amount <= 0:
        print("❌ Сумма должна быть положительной!")
        return balance
    new_balance = balance + amount
    print(f"✅ Счёт пополнен на {amount} руб.")
    return new_balance

def withdraw(balance):
    """Снятие денег"""
    amount = int(input("Сумма снятия: "))
    if amount <= 0:
        print("❌ Сумма должна быть положительной!")
        return balance
    if amount > balance:
        print("❌ Недостаточно средств!")
        return balance
    new_balance = balance - amount
    print(f"✅ Снято {amount} руб.")
    return new_balance

def main():
    """Главная функция программы"""
    print("🏦 Банк 'Ученик'")

    balance = 5000

    while True:
        print("\n1 - Баланс")
        print("2 - Пополнить")
        print("3 - Снять")
        print("4 - Выход")

        choice = input("Выберите действие: ")

        if choice == "1":
            show_balance(balance)
        elif choice == "2":
            balance = deposit(balance)
        elif choice == "3":
            balance = withdraw(balance)
        elif choice == "4":
            print("👋 До свидания!")
            break
        else:
            print("❌ Неверный выбор!")

if __name__ == "__main__":
    main()