# string method

while True:
    name = input("What is your name? ").strip().title()
    age = input("How old are you? ").strip()
    if age.isdigit():
        age = int(age)
        break
    else:
        print("Invalid Input.\n")
print("Name:",name)
print("Age:",age)