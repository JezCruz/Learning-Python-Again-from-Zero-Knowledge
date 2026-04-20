#Numeric Operator Exercises.


firstname = input("What is your first name? ")
lastname = input("What is your last name? ")
year_of_birth = int(input("What year were you born? "))
present_year = int(input("What is the present year? "))

#formula to calculate age
age = present_year - year_of_birth

print("Full Name: "+ firstname + " " + lastname)
print("Age: " + str(age))

#output: 
#What is your first name? Jezreel
#What is your last name? Cruz
#What year were you born? 2003
#Full Name: Jezreel Cruz
#Age: 23