# create text file with input

name = input("Enter your name: ")

with open("python-try/names.txt", "w") as f:
    f.write(name)

# after run the program open the names.txt then you will si the inside of it.
# Output:
# Jezreel James

# so yeah you can use it with "a" or append to add new names inside of it. :)