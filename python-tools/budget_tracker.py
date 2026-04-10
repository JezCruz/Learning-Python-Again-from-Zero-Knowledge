records = []
balance = 0.0

while True:
    print("\n===== BUDGET TRACKER =====")
    print("1. Add Income")
    print("2. Add Expense")
    print("3. View Records")
    print("4. Show Balance")
    print("5. Exit")

    choice = input("Choose an option: ").strip()

    if choice == "1":
        name = input("Enter income name: ").strip()

        while True:
            amount_input = input("Enter income amount: ").strip()
            try:
                amount = float(amount_input)
                if amount < 0:
                    print("Amount cannot be negative.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter a number.")

        record = {
            "type": "Income",
            "name": name,
            "amount": amount
        }

        records.append(record)
        balance += amount
        print(f"Income added successfully! Current balance: ₱{balance:.2f}")

    elif choice == "2":
        name = input("Enter expense name: ").strip()

        while True:
            amount_input = input("Enter expense amount: ").strip()
            try:
                amount = float(amount_input)
                if amount < 0:
                    print("Amount cannot be negative.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter a number.")

        record = {
            "type": "Expense",
            "name": name,
            "amount": amount
        }

        records.append(record)
        balance -= amount
        print(f"Expense added successfully! Current balance: ₱{balance:.2f}")

    elif choice == "3":
        if not records:
            print("\nNo records yet.")
        else:
            print("\n===== ALL RECORDS =====")
            for i, record in enumerate(records, start=1):
                print(f"{i}. {record['type']} - {record['name']} - ₱{record['amount']:.2f}")

    elif choice == "4":
        print(f"\nCurrent Balance: ₱{balance:.2f}")

    elif choice == "5":
        print("Exiting Budget Tracker. Goodbye!")
        break

    else:
        print("Invalid choice. Please select 1 to 5.")