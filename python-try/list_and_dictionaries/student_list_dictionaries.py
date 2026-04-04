# Student List Dictionaries

# task 1 and 2

students = [
    {"name": "Jezreel", "age": 32, "course": "BSIT"},
    {"name": "Ana", "age": 21, "course": "CS"},
    {"name": "Mark", "age": 19, "course": "SE"}
]

# task 3 - print all using loop
for student in students:
    print(student)

# task 4 - print the second student's name
print(students[1]["name"])

# task 5 - update the first student's age
students[0]["age"] = 23
print(students[0])

# task 6 - add student in the list dictionary
students.append({"name": "John", "age": 19, "course": "BSIT"})
for new_list in students:
    print(new_list)

# task 7 - print clean and specific
for clean_list in students:
    print(clean_list["name"], clean_list["age"], clean_list["course"])