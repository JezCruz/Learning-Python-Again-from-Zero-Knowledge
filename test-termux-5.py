# Access System.

# Test - Access System
# 
# status = admin / user
# 
# age < 18 → restricted
# 
# admin + 18+ → full access
# 
# user + 18+ → limited access

print("""
=============================
        Access System
=============================
      """)

role = input('What is Your Role? ').lower()
age = int(input('How old are you? '))


match (role, age):
    case ("user", age) if age < 18:
        print('Restricted')
    case ("admin", age) if age >= 18:
        print('Full Access')
    case ("user", age) if age >= 18:
        print('Limited Access')
    case _:
        print("Not allowed")


# Output.
# =============================
#         Access System
# =============================
#       
# What is Your Role? Admin
# How old are you? 22
# Full Access
