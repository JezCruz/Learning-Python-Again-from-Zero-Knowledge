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