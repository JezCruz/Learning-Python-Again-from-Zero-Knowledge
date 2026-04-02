# User Data Saver

import os

os.makedirs("python-try/user_data", exist_ok=True)

while True:

    print("""\n+ = = = = User Data = = = = +

    Selections:
    0 = Exit.
    1 = Input User Data.
    2 = Read User Data.""")
    selection = input("\nSelect: ")

    if selection == "1":
        
        name = input("Enter your name: ")
        age = int(input("Enter your age: "))

        with open("python-try/user_data/data.txt", "a") as f:
            f.write(f"Name: {name}, Age: {age}\n")
        print("Saved Successfully!")

    elif selection == "2":
        
        with open("python-try/user_data/data.txt", "r") as f:
            print(f.read())
        print("\nAll Data Printed Successfully!")
    elif selection == "0":
        print("Goodbye!")
        break
    else:
        print("\nInvalid Selection.\n")


# Output: 
# + = = = = User Data = = = = +
# 
#     Selections:
#     0 = Exit.
#     1 = Input User Data.
#     2 = Read User Data.
# 
# Select: 1
# Enter your name: fenrir
# Enter your age: 19
# Saved Successfully!
# 
# + = = = = User Data = = = = +
# 
#     Selections:
#     0 = Exit.
#     1 = Input User Data.
#     2 = Read User Data.
# 
# Select: 2
# Name: James, Age: 25
# Name: Jezreel, Age: 23
# Name: Anger, Age: 36
# Name: John, Age: 5645
# Name: Johval, Age: 19
# Name: mel, Age: 19
# Name: mav, Age: 19
# Name: fenrir, Age: 19
# 
# 
# All Data Printed Successfully!
# 
# + = = = = User Data = = = = +
# 
#     Selections:
#     0 = Exit.
#     1 = Input User Data.
#     2 = Read User Data.
# 
# Select: 0
# Goodbye!