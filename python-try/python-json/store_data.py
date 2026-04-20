# store data in json with user inputs

import json

file_loc = "python-try/python-json/data-json/users_data.json"
name = input("enter your name: ").strip().title()
while True:
    age_ = input("enter your age: ")
    if age_.isdigit():
        age = int(age_)
        break
    else:
        print("invalid Input.")

try:
    with open(file_loc, "r")as f:
        users = json.load(f)
except FileNotFoundError:
    users = []
except json.JSONDecodeError:
    users = []

users.append({"name": name, "age": age})

with open(file_loc, "w")as f:
    json.dump(users, f, indent=4)

print("\n=-=-= Users =-=-=\n")
for user in users:
    print("name:",user["name"], "\nage:",user["age"],"\n")