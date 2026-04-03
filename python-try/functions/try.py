# functions

def show_menu():
    print("= - = - = Menu = - = - =")
    print("0. Exit")
    print("1. Add")
    print("2. Read")
    print("3. Delete")
    print("4. Update")
show_menu()


def greet(name):
    print("Hello!",name)
greet("Jez")


def add(a, b):
    print(a + b)
add(100, 50)


def add(a, b):
    return a + b
result = add(5, 3)
print(result)


def add(a, b):
    return a + b
a = int(input("Enter Your First Number: "))
b = int(input("Enter Your Second Number: "))
print(add(a, b))


y = add(5, 9)
x = add(8, 6)
print(y * x)