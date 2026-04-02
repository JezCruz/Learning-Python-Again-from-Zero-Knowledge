# User Data Saver

import os

os.makedirs("python-try/user_data", exist_ok=True)

name = input("Enter your name: ")
age = int(input("Enter your age: "))

with open("python-try/user_data/data.txt", "a") as f:
    f.write(f"Name: {name}, Age: {age}\n")
print("Saved Successfully!")

# Output:
# Name: James, Age: 25
# Name: Jezreel, Age: 23
# Name: Anger, Age: 36
# Name: John, Age: 5645