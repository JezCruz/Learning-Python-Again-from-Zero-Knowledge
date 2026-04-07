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

def update_user():
     
    select_name = input("Search User name want's to update: ").strip().title()

    found = False

    for user in users:
        if select_name == user["name"]:
            print("User Named", select_name, "found!, and able to update.\n")
        
            update_name = input("Enter your updated name: ").strip().title()

            while True:
                update_age = input("Enter your updated age: ").strip()
                if update_age.isdigit():
                    update_age = int(update_age)
                    break
                else:
                    print("Invalid age.")         

            user["name"] = update_name
            user["age"] = update_age

            print("User Updated!")
            found = True
            break
    if not found:
            print("User not found.")

    with open(file_loc, "w")as f:
            json.dump(users, f, indent=4)

while True:
    selection = input("enter function: ").strip().lower()

    if selection == "exit":
             print("Goodbye!")
             break
    elif selection == "delete":
        delete_name = input("Enter name to delete: ").strip().title()

        found = False


        for user in users:
            if user["name"] == delete_name:
                users.remove(user)
                print("User Deleted!")
                found = True
                break
        if not found:
            print(f"No user named, '{delete_name}'.")

        with open(file_loc, "w")as f:
            json.dump(users, f, indent=4)

    elif selection == "ping":
         ping()

    elif selection == "hello":
         hello()

    elif selection == "read data":
         read_data()

    elif selection == "update data":
         update_user()