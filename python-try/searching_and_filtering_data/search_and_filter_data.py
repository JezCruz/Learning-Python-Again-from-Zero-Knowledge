# Search and Filter Data

import json

file_loc = "python-try/python-json/data-json/users_data.json"

with open(file_loc, "r")as f:
    users = json.load(f)

search_name = input("Search User: ").strip().title()

found = False

for user in users:
    if user["name"] == search_name:
        print("\n=-=-=-= User Found: =-=-=-=")
        print("Name:", user["name"])
        print("Age:", user["age"])
        print()
        found = True

if not found:
    print("\nUser not found\n")