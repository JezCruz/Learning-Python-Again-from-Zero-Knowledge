# Age Category Checker.

print('==============================')
print('     Age Category Checker     ')
print('==============================\n')

name = input('Enter Your Name: ')
age = int(input('Enter Your Age: '))


# Age	   |   Category
# 0–12	        Child
# 13–17	        Teen
# 18–59	        Adult
# 60+	        Senior

# Age Category Logic.
if age <= 12:
    category = 'Child'
elif age >= 13 and age <= 17:
    category = 'Teen'
elif age >= 18 and age <= 59:
    category = 'Adult'
elif age >= 60:
    category = 'Senior'

# Allowed or not Allowed Logic.
if age >= 18 and age <= 59:
    isAllowed = 'You are Eligible to apply for Jobs.'
elif age <= 18:
    isAllowed = 'You are Not Allowed to apply for Jobs.'
elif age >= 60:
    isAllowed = 'You are Eligible to apply,\nbut Are you sure? you are too old :('

print('\n')
print('==============================')
print('            Status            ')
print('==============================\n')
print('Hello', name+'!')
print('Your are', age, 'years old.')
print('Category:', category)
print('\nState:', isAllowed)
print('\n')



# output:
#
# ==============================
#      Age Category Checker     
# ==============================
# 
# Enter Your Name: Jezreel James Cruz
# Enter Your Age: 22
# 
# 
# ==============================
#             Status
# ==============================
# 
# Hello Jezreel James Cruz!
# Your are 22 years old.
# Category: Adult
# 
# State: You are Eligible to apply for Jobs.