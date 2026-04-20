#Comparison Operator Exercise.

value1 = int(input('Enter first number: '))
value2 = int(input('Enter first number: '))

if value1 > value2:
    print("Mas Mataas! si value1, "+str(value1)+" kay sa kay value2, "+str(value2))
    #Enter first number: 50
    #Enter first number: 20
    #Mas Mataas! si value1, 50 kay sa kay value2, 20
else:
    if value1 < value2:
        print("Mas Mababa! si value1, "+str(value1)+" kay sa kay value2, "+str(value2))
        #Enter first number: 20
        #Enter first number: 30
        #Mas Mababa! si value1, 20 kay sa kay value2, 30
    else:
        print("Equal, si value1, "+str(value1)+" at value2, "+str(value2))
        #Enter first number: 50
        #Enter first number: 50
        #Equal, si value1, 50 at value2, 50
