cart = []

def add_item():
    name = input("Item name: ")
    price = float(input("Item price: ₱"))
    quantity = int(input("Quantity: "))

    item = {
        "name": name,
        "price": price,
        "quantity": quantity,
        "total": price * quantity
    }

    cart.append(item)
    print("Item added!\n")


def view_cart():
    if not cart:
        print("Cart is empty.\n")
        return

    print("\n===== CART =====")
    total = 0

    for item in cart:
        print(f"{item['name']} x{item['quantity']} = ₱{item['total']:.2f}")
        total += item["total"]

    print(f"Total: ₱{total:.2f}\n")


def checkout():
    if not cart:
        print("Cart is empty.\n")
        return

    total = sum(item["total"] for item in cart)

    print(f"\nTotal amount: ₱{total:.2f}")
    payment = float(input("Payment: ₱"))

    if payment < total:
        print("Not enough payment.\n")
    else:
        change = payment - total
        print("\n===== RECEIPT =====")
        for item in cart:
            print(f"{item['name']} x{item['quantity']} - ₱{item['total']:.2f}")

        print(f"Total: ₱{total:.2f}")
        print(f"Payment: ₱{payment:.2f}")
        print(f"Change: ₱{change:.2f}")
        print("Thank you for shopping!\n")

        cart.clear()


def main():
    while True:
        print("===== GROCERY COUNTER =====")
        print("1. Add Item")
        print("2. View Cart")
        print("3. Checkout")
        print("4. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            add_item()
        elif choice == "2":
            view_cart()
        elif choice == "3":
            checkout()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.\n")


main()
