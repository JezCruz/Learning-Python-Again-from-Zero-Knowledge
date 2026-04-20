# Search and Filter Data

import json

file_loc = "python-try/python-json/data-json/users_data.json"

with open(file_loc, "r")as f:
    users = json.load(f)

# Task 1 - Search User by exact name.

# search_name = input("Search User: ")

# found = False

# for user in users:
#     if search_name.strip().title() == user["name"]:
#         print("\n= = = User Info = = =\n")
#         print("name:",user["name"])
#         print("Age:",user["age"])
#         print()
#         found = True

# if not found:
#     print("\nUser not found.\n")


#Task 2 - Partial Search.

# search_name = input("Search Name: ").strip().lower()

# found = False

# for user in users:
#     if search_name in user["name"].lower():
#         print("\n= = = Users Found = = =\n")
#         print(user)
#         print()
#         found = True
# if not found:
#     print("\n= = = User not found. = = =\n")


# Task 3 - Filter user by age.

# print("= = = = filter users. = = = =")

# while True:
#     filter_user = input("Enter age greater-than or equal?: ").strip()
#     if filter_user.isdigit():
#         filter_user = int(filter_user)
#         break
#     else:
#         print("Invalid Input.")

# found = False

# for user in users:
#     if user["age"] >= filter_user:
#         print("Name:",user["name"])
#         print("Age:",user["age"])
#         print()
#         found = True

# if not found:
#     print("No User with that age.")