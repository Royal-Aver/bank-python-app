# main.py - точка входа, консольное меню

from services import BankService

def print_menu():
    print("\n" + "=" * 50)
    print("🏦 БАНК 'УЧЕНИК' - ГЛАВНОЕ МЕНЮ")
    print("=" * 50)
    print("1 - Регистрация нового пользователя")
    print("2 - Создать банковский счёт")
    print("3 - Пополнить счёт")
    print("4 - Снять деньги")
    print("5 - Перевести деньги")
    print("6 - Использовать бонусы")
    print("7 - Показать информацию о счёте")
    print("8 - Показать историю операций")
    print("9 - Показать все счета")
    print("0 - Выход")
    print("-" * 50)

def main():
    service = BankService()

    print("\n🎉 Добро пожаловать в Банк 'Ученик'!")
    print("Версия 2.0 — с ООП, миксинами и SOLID")

    while True:
        print_menu()
        choice = input("👉 Ваш выбор: ")

        if choice == "1":
            print("\n--- РЕГИСТРАЦИЯ НОВОГО ПОЛЬЗОВАТЕЛЯ ---")
            name = input("Имя: ")
            email = input("Email: ")
            phone = input("Телефон (+7 123 456-78-90): ")
            service.register_user(name, email, phone)

        elif choice == "2":
            print("\n--- СОЗДАНИЕ БАНКОВСКОГО СЧЁТА ---")
            email = input("Email пользователя: ")
            balance = float(input("Начальный баланс (0 по умолчанию): ") or 0)
            service.create_account(email, balance)

        elif choice == "3":
            print("\n--- ПОПОЛНЕНИЕ СЧЁТА ---")
            account_id = int(input("ID счёта: "))
            amount = float(input("Сумма: "))
            service.deposit(account_id, amount)

        elif choice == "4":
            print("\n--- СНЯТИЕ ДЕНЕГ ---")
            account_id = int(input("ID счёта: "))
            amount = float(input("Сумма: "))
            service.withdraw(account_id, amount)

        elif choice == "5":
            print("\n--- ПЕРЕВОД ДЕНЕГ ---")
            from_id = int(input("ID вашего счёта: "))
            to_id = int(input("ID счёта получателя: "))
            amount = float(input("Сумма перевода: "))
            service.transfer(from_id, to_id, amount)

        elif choice == "6":
            print("\n--- ИСПОЛЬЗОВАНИЕ БОНУСОВ ---")
            account_id = int(input("ID счёта: "))
            service.use_bonus(account_id)

        elif choice == "7":
            print("\n--- ИНФОРМАЦИЯ О СЧЁТЕ ---")
            account_id = int(input("ID счёта: "))
            service.show_account_info(account_id)

        elif choice == "8":
            print("\n--- ИСТОРИЯ ОПЕРАЦИЙ ---")
            account_id = int(input("ID счёта: "))
            n = int(input("Сколько последних операций показать (10 по умолчанию): ") or 10)
            service.show_account_logs(account_id, n)

        elif choice == "9":
            service.list_all_accounts()

        elif choice == "0":
            print("\n👋 Спасибо, что пользуетесь Банком 'Ученик'! До свидания!")
            break

        else:
            print("❌ Неверный выбор! Попробуйте снова.")

if __name__ == "__main__":
    main()