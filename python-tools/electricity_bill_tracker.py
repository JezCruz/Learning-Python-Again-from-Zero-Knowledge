bills = []

while True:
    print("\n===== ELECTRICITY BILL TRACKER =====")
    print("1. Add Bill Record")
    print("2. View All Records")
    print("3. Show Total of All Bills")
    print("4. Exit")

    choice = input("Choose an option: ").strip()

    if choice == "1":
        month = input("Enter month (example: April 2026): ").strip()

        while True:
            kwh_input = input("Enter kWh used: ").strip()
            try:
                kwh_used = float(kwh_input)
                if kwh_used < 0:
                    print("kWh cannot be negative.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter a number.")

        while True:
            rate_input = input("Enter rate per kWh: ").strip()
            try:
                rate_per_kwh = float(rate_input)
                if rate_per_kwh < 0:
                    print("Rate cannot be negative.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter a number.")

        while True:
            other_input = input("Enter other charges (0 if none): ").strip()
            try:
                other_charges = float(other_input)
                if other_charges < 0:
                    print("Other charges cannot be negative.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter a number.")

        energy_charge = kwh_used * rate_per_kwh
        total_bill = energy_charge + other_charges

        bill = {
            "month": month,
            "kwh_used": kwh_used,
            "rate_per_kwh": rate_per_kwh,
            "other_charges": other_charges,
            "energy_charge": energy_charge,
            "total_bill": total_bill
        }

        bills.append(bill)

        print("\nBill record added successfully!")
        print(f"Month: {month}")
        print(f"Energy Charge: ₱{energy_charge:.2f}")
        print(f"Total Bill: ₱{total_bill:.2f}")

    elif choice == "2":
        if not bills:
            print("\nNo bill records yet.")
        else:
            print("\n===== ALL BILL RECORDS =====")
            for i, bill in enumerate(bills, start=1):
                print(f"\nRecord #{i}")
                print(f"Month: {bill['month']}")
                print(f"kWh Used: {bill['kwh_used']}")
                print(f"Rate per kWh: ₱{bill['rate_per_kwh']:.2f}")
                print(f"Other Charges: ₱{bill['other_charges']:.2f}")
                print(f"Energy Charge: ₱{bill['energy_charge']:.2f}")
                print(f"Total Bill: ₱{bill['total_bill']:.2f}")

    elif choice == "3":
        if not bills:
            print("\nNo bill records yet.")
        else:
            grand_total = sum(bill["total_bill"] for bill in bills)
            print(f"\nTotal of all recorded electricity bills: ₱{grand_total:.2f}")

    elif choice == "4":
        print("Exiting Electricity Bill Tracker. Goodbye!")
        break

    else:
        print("Invalid choice. Please select 1 to 4.")