# Program that checks:

# if number is EVEN → print "Even"
# 
# if number is ODD → print "Odd"
# 
# if number is ZERO → print "Zero"

print("""\n***Determine Odd or Even the Number***\n""")
number = int(input('Enter a Number: '))


if number == 0:
    print(f'{number}, Zero')
elif number % 2 == 0:
    print(f'{number}, Even Number')
else:
    print(f'{number}, Odd Number')



# Outputs:

# ***Determine Odd or Even the Number***
# 
# Enter a Number: 7
# 7, Odd Number
# 
# 
# ***Determine Odd or Even the Number***
# 
# Enter a Number: 4
# 4, Even Number
# 
# 
# ***Determine Odd or Even the Number***
# 
# Enter a Number: 0
# 0, Zero