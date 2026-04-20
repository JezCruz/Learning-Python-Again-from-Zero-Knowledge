# store data in Json

import json

users = [
    {"name":"jezreel","age":23},
    {"name":"ana","age":20}
]

file = "python-try/python-json/data-json/data.json"

with open(file, "w") as f:
    json.dump(users, f, indent=4)

try:
    with open(file, "r")as f:
        users = json.load(f)
    print(users)
except:
    users = []

for user in users:
    print(user["name"])

users.append({"name":"james","age":22})

with open(file, "w")as f:
    json.dump(users, f, indent=4)
print(users)

for user in users:
    print(user["name"])