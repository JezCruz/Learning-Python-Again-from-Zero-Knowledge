# create text file with input and using append

name = input("Enter your name: ")

with open("python-try/names.txt", "a") as f:
    f.write("\n"+name)
with open("python-try/names.txt", "r") as f:
    print(f.read())
    

# after run the program open the names.txt then you will see in the inside of it the Output
# Output:
# Jezreel
# James
# josh
# main
# albert
# johval
# fenrir
# mav
# mel
# lawins