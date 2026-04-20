# User Data Saver full function

import os

folder_path = "python-try/user_data"
file_path = os.path.join(folder_path, "data.txt")

os.makedirs(folder_path, exist_ok=True)

if not os.path.exists(file_path):
    with open(file_path, "w") as f:
        pass

while True:

    print("""\n+ = = = = User Data = = = = +

    Selections:
    0 = Exit.
    1 = Input User Data.
    2 = Read User Data.
    3 = Delete User Data.
    4 = Update User Data.""")

    selection = input("\nSelect: ")
    
    if selection == "1":
        try:
            name = input("\nEnter your name: ")
            age = int(input("Enter your age: "))

        
            with open("python-try/user_data/data.txt", "a") as f:
                f.write(f"Name: {name}, Age: {age}\n")
            print("\nSaved Successfully!\n")
        except ValueError:
            print("\nInvalid Input.\n")

    elif selection == "2":
        
        with open("python-try/user_data/data.txt", "r") as f:
            user_data = f.readlines()

        if not user_data:
            print("\nNo user data found.\n")
            continue

        print("\n= = = Users Data = = =")
        for i, user in enumerate(user_data):
            print(f"{i+1}. {user.strip()}")

    elif selection == "3":
        try:
            with open("python-try/user_data/data.txt", "r") as f:
                user_data = f.readlines()
            
            if not user_data:
                print("\nNo user data to delete.\n")
                continue

            print("\n= = = Users Data = = =")
            for i, user in enumerate(user_data):
                print(f"{i+1}. {user.strip()}")

            delete_index = int(input("\nEnter User Index to Delete: ")) - 1

            if 0 <= delete_index < len(user_data):
                user_data.pop(delete_index)

                with open("python-try/user_data/data.txt", "w") as f:
                    f.writelines(user_data)

                print("\nUser Deleted!\n")
                print("\n= = = Current User Data = = =\n")

                with open("python-try/user_data/data.txt", "r") as f:
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

    elif selection == "4":
        try:    
            with open("python-try/user_data/data.txt", "r") as f:
                user_data = f.readlines()

            if not user_data:
                print("\nNo user data to update.\n")
                continue

            print("\n= = = User Data = = =")
            for i, user in enumerate(user_data):
                print(f"{i+1}. {user.strip()}")
            
            update_index = int(input("\nEnter User Index to Update: ")) - 1
            

            if 0 <= update_index < len(user_data):
                name = input("Update new name: ")
                age = int(input("Update age: "))

                user_data[update_index] = f"Name: {name}, Age: {age}\n"

                with open("python-try/user_data/data.txt", "w") as f:
                    f.writelines(user_data)

                print("\nUser Updated!\n")

                with open("python-try/user_data/data.txt", "r") as f:
                    user_data = f.readlines()

                print("\n= = = Updated Users Data = = =")

                for i, user in enumerate(user_data):
                    print(f"{i+1}. {user.strip()}")

            else:
                print("\nInvalid Input.\n")
        except ValueError:
                    print("\nPlease input a valid number\n")
    elif selection == "0":
        print("\nGoodbye!\n")
        break

    else:
        print("\nInvalid Selection.\n")
