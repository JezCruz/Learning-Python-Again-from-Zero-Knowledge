expenses = []

while True:
    print("\n--- EXPENSE TRACKER ---")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Show Total")
    print("4. Exit")

    choice = input("Choose: ")

    if choice == "1":
        name = input("Expense name: ")
        amount = float(input("Amount: "))
        expenses.append({"name": name, "amount": amount})
        print("Expense added!")

    elif choice == "2":
        if not expenses:
            print("No expenses recorded.")
        else:
            for expense in expenses:
                print(f"{expense['name']} - ₱{expense['amount']:.2f}")

    elif choice == "3":
        total = sum(expense["amount"] for expense in expenses)
        print(f"Total Expenses: ₱{total:.2f}")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")