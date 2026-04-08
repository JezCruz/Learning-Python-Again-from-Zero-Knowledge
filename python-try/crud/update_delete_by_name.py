# Update Delete User by name

import json

file_loc = "python-try/python-json/data-json/users_data.json"

with open(file_loc, "r")as f:
    users = json.load(f)
    print(users)


def hello():
    print("Hello World!")


def ping():
    print("pong!")


def read_data():
    with open(file_loc, "r")as f:
        read_users = json.load(f)
        print("+++++++++++++ All Data +++++++++++++\n")
        for user in read_users:
            print("Name:",user["name"])
            print("Age:",user["age"])
            print()


def add_user():
    print("\n+ = + = + = Add New User = + = + = +\n")

    name = input("Enter Name: ").strip().title()

    while True:
        age = input("Enter Age: ").strip()
        if age.isdigit():
            age = int(age)
            break
        else:
            print("Invalid Input Age Numbers Only.")
    
    users.append({"name": name, "age": age})

    with open(file_loc, "w")as f:
         json.dump(users, f, indent=4)

    print("\nUser Added.\n")


def update_user():
    if not users:
        print("\nNo users to update.\n")
        return

    print("\n+++++++++++++ Users List +++++++++++++\n")
    for i, user in enumerate(users, start=1):
        print(f"{i}. Name: {user['name']}, Age: {user['age']}")

    try:
        update_index = int(input("\nEnter user number to update: ")) - 1

        if 0 <= update_index < len(users):
            new_name = input("Enter updated name: ").strip().title()

            while True:
                new_age = input("Enter updated age: ").strip()
                if new_age.isdigit():
                    new_age = int(new_age)
                    break
                else:
                    print("Invalid age. Numbers only.")

            users[update_index]["name"] = new_name
            users[update_index]["age"] = new_age

            with open(file_loc, "w") as f:
                json.dump(users, f, indent=4)

            print("\nUser updated successfully!\n")
        else:
            print("\nInvalid user number.\n")

    except ValueError:
        print("\nPlease enter a valid number.\n")

            
def delete_user():
    delete_name = input("Enter name to delete: ").strip().title()

    matches = []

    for i, user in enumerate(users):
        if user["name"] == delete_name:
            matches.append((i, user))

    if not matches:
        print(f"No user named '{delete_name}'.")
        return

    print("\nMatches found:")
    for num, (real_index, user) in enumerate(matches, start=1):
        print(f"{num}. Name: {user['name']}, Age: {user['age']}")

    try:
        choice = int(input("\nChoose user number to delete: ")) - 1

        if 0 <= choice < len(matches):
            real_index = matches[choice][0]
            deleted_user = users.pop(real_index)

            print(f"\nDeleted: {deleted_user['name']} - {deleted_user['age']}")

            with open(file_loc, "w") as f:
                json.dump(users, f, indent=4)
        else:
            print("Invalid selection.")

    except ValueError:
        print("Please enter a valid number.")

while True:
    selection = input("enter function: ").strip().lower()

    if selection == "exit":
             print("\nGoodbye!\n")
             break
    
    elif selection == "delete":
        delete_user()

    elif selection == "ping":
         ping()

    elif selection == "hello":
         hello()

    elif selection == "read data":
         read_data()

    elif selection == "update data":
         update_user()

    elif selection == "add data":
         add_user()