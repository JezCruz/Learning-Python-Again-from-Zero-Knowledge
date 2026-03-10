#If and Else-If Exercise. - Find Generation by Year of Birth.


#Example range.
#year of birth range:     |      Generation:
# 1946 - 1964                      Baby Boomer
# 1965 - 1980                      Generation X
# 1981 - 1996                      Millenial
# 1997 - 2015                      Gen Z

# Genaration
gen1 = "Baby Boomer"
gen2 = "Generation X"
gen3 = "Millenial"
gen4 = "Gen Z"



year_of_birth = int(input('Enter your Year of Birth: '))

if year_of_birth >= 1946 and year_of_birth <= 1964:
    print("You're a "+ gen1)
elif year_of_birth >= 1965 and year_of_birth <= 1980:
    print("You're a "+ gen2)
elif year_of_birth >= 1981 and year_of_birth <= 1996:
    print("You're a "+ gen3)
elif year_of_birth >= 1997 and year_of_birth <= 2015:
    print("You're a "+ gen4)
else:
    print("Invalid Year.")