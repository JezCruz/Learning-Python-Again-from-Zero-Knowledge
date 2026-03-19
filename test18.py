# Determine the Number if Possitive or Negative, Odd or Even.

# asks user for number
# 
# prints:
# 
#       "Positive Even"
#       
#       "Positive Odd"
#       
#       "Negative Even"
#       
#       "Negative Odd"
#       
#       "Zero"


number = int(input("Enter a Number: "))

if number == 0:
    print("Zero")
else:
    if number > 0:
        positive_negative = 'Positive'
    elif number < 0:
        positive_negative = 'Negative'
    if number % 2 == 0:
        odd_even = 'Even'
    else:
        odd_even = 'Odd'
    
    print(positive_negative, odd_even)  


# Outputs: 

# Example Odd:
# Enter a Number: 3
# Positive Odd

# Enter a Number: -3
# Negative Odd


# Example Even:

# Enter a Number: 8
# Positive Even

# Enter a Number: -8
# Negative Even