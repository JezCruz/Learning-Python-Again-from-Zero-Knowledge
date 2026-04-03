# Menu system using def

import os

folder_path = "python-try/functions/data"
file_path = os.path.join(folder_path, "user_data.txt")

os.makedirs(folder_path, exist_ok=True)

if not os.path.exists(file_path):
    with open(file_path, "w") as f:
        pass

while True:

    def show_menu():
        print("\n= - = - = Menu = - = - =\n")
        print("0. Exit")
        print("1. Add")
        print("2. Read")
        print("3. Delete")
        print("4. Update")
    show_menu()

    def add_user():
        print("\n=-=-=-= Add User Data =-=-=-=\n")

        try:
            name = input("\nEnter your name: ")
            age = int(input("Enter your age: "))

        
            with open("python-try/functions/data/user_data.txt", "a") as f:
                f.write(f"Name: {name}, Age: {age}\n")
            print("\nSaved Successfully!\n")
        except ValueError:
            print("\nInvalid Input.\n")

    def read_data():
        print("\n=-=-=-= Read All Data =-=-=-=\n")

        with open("python-try/functions/data/user_data.txt", "r") as f:
            user_data = f.readlines()

        if not user_data:
            print("\nNo user data found.\n")
            return

        print("\n= = = Users Data = = =")
        for i, user in enumerate(user_data):
            print(f"{i+1}. {user.strip()}")

    def delete_user_data():
        print("\n=-=-=-= Delete User Data =-=-=-=\n")

        try:
            with open("python-try/functions/data/user_data.txt", "r") as f:
                user_data = f.readlines()
            
            if not user_data:
                print("\nNo user data to delete.\n")
                return

            print("\n= = = Users Data = = =")
            for i, user in enumerate(user_data):
                print(f"{i+1}. {user.strip()}")

            delete_index = int(input("\nEnter User Index to Delete: ")) - 1

            if 0 <= delete_index < len(user_data):
                user_data.pop(delete_index)

                with open("python-try/functions/data/user_data.txt", "w") as f:
                    f.writelines(user_data)

                print("\nUser Deleted!\n")
                print("\n= = = Current User Data = = =\n")

                with open("python-try/functions/data/user_data.txt", "r") as f:
                    user_data = f.readlines()

                if not user_data:
                    print("No remaining users.\n")
                else:
                    for i, user in enumerate(user_data):
                        print(f"{i+1}. {user.strip()}")
            else:
                print("\nInvalid Selection.\n")
        except ValueError:
                    print("\nPlease input a valid number\n")

    def update_user_data():
        print("\n=-=-=-= Update User Data =-=-=-=\n")

        try:    
            with open("python-try/functions/data/user_data.txt", "r") as f:
                user_data = f.readlines()

            if not user_data:
                print("\nNo user data to update.\n")
                return

            print("\n= = = User Data = = =")
            for i, user in enumerate(user_data):
                print(f"{i+1}. {user.strip()}")
            
            update_index = int(input("\nEnter User Index to Update: ")) - 1
            

            if 0 <= update_index < len(user_data):
                name = input("Update new name: ")
                age = int(input("Update age: "))

                user_data[update_index] = f"Name: {name}, Age: {age}\n"

                with open("python-try/functions/data/user_data.txt", "w") as f:
                    f.writelines(user_data)

                print("\nUser Updated!\n")

                with open("python-try/functions/data/user_data.txt", "r") as f:
                    user_data = f.readlines()

                print("\n= = = Updated Users Data = = =")

                for i, user in enumerate(user_data):
                    print(f"{i+1}. {user.strip()}")

            else:
                print("\nInvalid Input.\n")
        except ValueError:
                    print("\nPlease input a valid number\n")

    selection = input("\nSelect Menu: ").lower()

    if selection == "0":
        print("\nBye!\n")
        break
    elif selection == "1":
        add_user()
    elif selection == "2":
        read_data()
    elif selection == "3":
        delete_user_data()
    elif selection == "4":
        update_user_data()
    else:
        print(f"\nNo Selection '{selection}' on Menu!\n")