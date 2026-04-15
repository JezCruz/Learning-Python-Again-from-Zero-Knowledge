import json
import os

FILE_NAME = "expenses.json"


def load_expenses():
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r") as file:
                return json.load(file)
        except json.JSONDecodeError:
            return []
    return []


def save_expenses(expenses):
    with open(FILE_NAME, "w") as file:
        json.dump(expenses, file, indent=4)


def add_expense(expenses):
    name = input("Expense name: ").strip()
    if not name:
        print("Expense name cannot be empty.\n")
        return

    try:
        amount = float(input("Amount: "))
        expenses.append({"name": name, "amount": amount})
        save_expenses(expenses)
        print("Expense added.\n")
    except ValueError:
        print("Invalid amount.\n")


def view_expenses(expenses):
    if not expenses:
        print("No expenses recorded.\n")
        return

    print("\nExpenses:")
    total = 0
    for i, expense in enumerate(expenses, start=1):
        print(f"{i}. {expense['name']} - {expense['amount']:.2f}")
        total += expense["amount"]

    print(f"Total: {total:.2f}\n")


def main():
    expenses = load_expenses()

    while True:
        print("=== EXPENSE TRACKER ===")
        print("1. Add expense")
        print("2. View expenses")
        print("3. Exit")

        choice = input("Choose: ").strip()

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid choice.\n")


if __name__ == "__main__":
    main()