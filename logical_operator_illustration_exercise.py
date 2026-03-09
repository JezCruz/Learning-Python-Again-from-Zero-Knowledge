#Logical Operation Illustration Exercise.


#millenial year: 1981 - 1996.
#so if you type year 1981 to 1996 What should come out is "Millenial ka! Apir!".
#then if you type outside in this range, should come out is "Wag Assuming.".


birth_year = int(input('What is your Year of birth? '))

if birth_year >= 1981 and birth_year <= 1996:
    print("Millenial ka! Apir!")
else:
    print("Wag Assuming.")