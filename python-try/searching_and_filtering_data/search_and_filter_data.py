# Search and Filter Data

users = [
    {"name": "Jez", "age": 20},
    {"name": "Ana", "age": 21},
    {"name": "Mark", "age": 19}
]

search_name = input("Search User: ").strip().title()

found = False

for user in users:
    if user["name"] == search_name:
        print("Found:", user)
        found = True

if not found:
    print("User not found")