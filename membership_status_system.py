# Membership Status System. - Using match-case.

# Write a program that will display the appropriate seminar fee which is based on the
# membership status and age entered by the user. Use the information below to complete the program.

#     Status       |             Criteria             |      Seminar Fee
#     S or s       | Club member 60 yrs old and above |          5
#     M or m       | Club member less than 60 yrs old |          10
#     N or n       | None member                      |          20

# ** if you input the wrong status then display the message "Input Error".

print("""
===========================================================================
=    Status       |                Age               |      Seminar Fee   =
=    S or s       | Club member 60 yrs old and above |          5         =
=    M or m       | Club member less than 60 yrs old |          10        =
=    N or n       | None member                      |          20        =
===========================================================================
""")
print("================Membership-Status-System================\n")

status = input('Are you a Member? ').lower()
age = int(input('How old are you? '))

print('\n')
match (status, age):
    case ("s", age) if age >= 60:
        print('Seminar Fee = 5')
    case ("m", age) if age < 60:
        print('Seminar Fee = 10')
    case ("n", age):
        print('Seminar Fee = 20')
    case _:
        print('Input Error')






# Output: "Senior"
# ===========================================================================
# =    Status       |                Age               |      Seminar Fee   =
# =    S or s       | Club member 60 yrs old and above |          5         =
# =    M or m       | Club member less than 60 yrs old |          10        =
# =    N or n       | None member                      |          20        =
# ===========================================================================
# 
# ================Membership-Status-System================
# 
# Are you a Member? S
# How old are you? 75
# 
# 
# Seminar Fee = 5



 
# # Output: "Minor"
# ===========================================================================
# =    Status       |                Age               |      Seminar Fee   =
# =    S or s       | Club member 60 yrs old and above |          5         =
# =    M or m       | Club member less than 60 yrs old |          10        =
# =    N or n       | None member                      |          20        =
# ===========================================================================
# 
# ================Membership-Status-System================
# 
# Are you a Member? M
# How old are you? 22
# 
# 
# 
# Seminar Fee = 10



# Output: "None Member"
# 
# ===========================================================================
# =    Status       |                Age               |      Seminar Fee   =
# =    S or s       | Club member 60 yrs old and above |          5         =
# =    M or m       | Club member less than 60 yrs old |          10        =
# =    N or n       | None member                      |          20        =
# ===========================================================================
# 
# ================Membership-Status-System================
# 
# Are you a Member? N
# How old are you? 35
# 
# 
# Seminar Fee = 20