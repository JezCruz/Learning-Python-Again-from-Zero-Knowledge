#Getting User Inputs Using The Input() Function Exercise.


fname = input("Enter Your First Name: ")
num1 = input("Enter your First Number: ")
num2 = input("Enter your Second Number: ")

print("Thanks " + fname + "\nAng mga number inputs mo ay " + num1 + " and " + num2)

#output: Enter Your First Name: Jezreel
#Enter your First Number: 10
#Enter your Second Number: 20
#Thanks Jezreel
#Ang mga number inputs mo ay 10 and 20


#no need to use str() function to convert the number inputs to string because the 
#input() function already converts the user input to string.


#or we can use num1 = int(input("Enter your First Number: ")) 
#to convert the user input to integer.
#so in print statement we need to make str(num1) to print it as string.