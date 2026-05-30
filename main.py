def show_menu():
    print("\n1 - Добавить трату")
    print("2 - Показать все траты")
    print("3 - Показать общую сумму")
    print("4 - Выход")


def add_expense(expenses):
    name = input("Название: ").strip()

    # Проверяем, что сумма - число
    while True:
        try:
            amount = float(input("Сумма: "))
            if amount <= 0:
                print("Сумма должна быть больше 0!")
                continue
            break
        except ValueError:
            print("Ошибка! Введите число (например: 150 или 99.50)")

    expenses.append({"name": name, "amount": amount})
    print(f"✓ Трата '{name}' на {amount} руб. добавлена!")


def show_all(expenses):
    if not expenses:
        print("\nСписок трат пуст. Добавьте хотя бы одну трату!")
        return

    print("\nСписок всех трат:")
    for i, expense in enumerate(expenses, start=1):
        print(f"{i}. {expense['name']} — {expense['amount']} руб.")


def show_total(expenses):
    if not expenses:
        print("\nНет трат для подсчёта!")
        return

    total = sum(expense['amount'] for expense in expenses)
    print(f"\nВсего потрачено: {total} руб.")


def main():
    expenses = []

    while True:
        show_menu()
        choice = input("\nВыбери действие: ").strip()

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            show_all(expenses)
        elif choice == "3":
            show_total(expenses)
        elif choice == "4":
            print("\nПока!")
            break
        else:
            print("Ошибка! Выберите число от 1 до 4.")


if __name__ == "__main__":
    main()
