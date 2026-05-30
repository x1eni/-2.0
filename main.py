import json
from datetime import datetime


def show_menu():
    print("\n1 - Добавить трату")
    print("2 - Показать все траты")
    print("3 - Показать общую сумму")
    print("4 - Выход")
    print("5 - Очистить все траты (начать новый список)")
    print("6 - Экспортировать список в файл")


def load_expenses():
    """Загружает траты из файла expenses.json"""
    try:
        with open('expenses.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return []


def save_expenses(expenses):
    """Сохраняет траты в файл expenses.json"""
    with open('expenses.json', 'w', encoding='utf-8') as f:
        json.dump(expenses, f, ensure_ascii=False, indent=2)


def add_expense(expenses):
    name = input("Название: ").strip()

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
    save_expenses(expenses)
    print(f"✓ Трата '{name}' на {amount} руб. добавлена и сохранена!")


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


def clear_expenses(expenses):
    """Очищает все траты"""
    confirm = input("\nТочно хочешь удалить ВСЕ траты? (да/нет): ").strip().lower()
    if confirm == "да" or confirm == "д":
        expenses.clear()
        save_expenses(expenses)
        print("✓ Все траты удалены! Начинай новый список.")
    else:
        print("Очистка отменена.")


def export_expenses(expenses):
    """Экспортирует траты в отдельный файл с отчётом"""
    if not expenses:
        print("\nНет трат для экспорта!")
        return

    # Создаём имя файла с текущей датой и временем
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"expenses_export_{timestamp}.txt"

    total = sum(expense['amount'] for expense in expenses)

    with open(filename, 'w', encoding='utf-8') as f:
        f.write("=" * 50 + "\n")
        f.write("ОТЧЁТ О ТРАТАХ\n")
        f.write(f"Дата: {datetime.now().strftime('%d.%m.%Y %H:%M:%S')}\n")
        f.write("=" * 50 + "\n\n")

        f.write("Список трат:\n")
        for i, expense in enumerate(expenses, start=1):
            f.write(f"{i}. {expense['name']} — {expense['amount']} руб.\n")

        f.write("\n" + "-" * 50 + "\n")
        f.write(f"ИТОГО: {total} руб.\n")
        f.write("=" * 50 + "\n")

    print(f"✓ Отчёт сохранён в файл: {filename}")


def main():
    expenses = load_expenses()

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
            save_expenses(expenses)
            print("\nПока! Траты сохранены в файл expenses.json")
            break
        elif choice == "5":
            clear_expenses(expenses)
        elif choice == "6":
            export_expenses(expenses)
        else:
            print("Ошибка! Выберите число от 1 до 6.")


if __name__ == "__main__":
    main()