# Membership Status System.

# Write a program that will display the appropriate seminar fee which is based on the
# membership status and age entered by the user. Use the information below to complete the program.

#     Status       |             Criteria             |      Seminar Fee
#     S or s       | Club member 60 yrs old and above |          5
#     M or m       | Club member less than 60 yrs old |          10
#     N or n       | None member                      |          20

# ** if you input the wrong status then display the message "Input Error".


print("================Membership-Status-System================\n")

status = input('Are you a Member? ').lower()
age = int(input('How old are you? '))


if status == 's' and age >= 60:
    print('Seminar Fee = 5')
elif status == 'm' and age < 60:
    print('Seminar Fee = 10')
elif status == 'n':
    print('Seminar Fee = 20')
else:
    print('Input Error')



# Output: "Senior"
# ================Membership-Status-System================

# Are you a Member? S
# How old are you? 68
# Seminar Fee = 5

# Output: "Minor"
# ================Membership-Status-System================

# Are you a Member? M
# How old are you? 25
# Seminar Fee = 10

# Output: "None Member"
# ================Membership-Status-System================

# Are you a Member? N
# How old are you? 62
# Seminar Fee = 20