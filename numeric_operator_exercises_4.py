#Numeric Operator Exercise 4. - Convert seconds to hours, minutes, and seconds.

#The user will input a number of seconds, and the program will convert it to hours, minutes, and seconds.


seconds = int(input("Enter the number of seconds: "))

computed_hours = seconds // 3600
remaining_seconds = seconds % 3600

computed_minutes = remaining_seconds // 60
computed_seconds = remaining_seconds % 60

print('the original number of seconds: ' + str(seconds))
print(str(computed_hours) + ' hours, ' + str(computed_minutes) + ' minutes, and ' + str(computed_seconds) + ' seconds.')

#output:
#Enter the number of seconds: 10000
#the original number of seconds: 10000
#2 hours, 46 minutes, and 40 seconds.
