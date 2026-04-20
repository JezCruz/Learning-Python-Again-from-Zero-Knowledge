# Salesman's Monthly Sales Computation.


# Determine the monthly income of a salesperson by using the following commission schedule:

#                 Monthly Sales                        |                  Income
# Greater than or equal to 50,000                      | 375 plus 16% of sales
# Less than 50,000 but greater than or equal to 40,000 | 350 plus 14% of sales
# Less than 40,000 but greater than or equal to 30,000 | 325 plus 12% of sales
# Less than 30,000 but greater than or equal to 20,000 | 300 plus 9% of sales
# Less than 20,000 but greater than or equal to 10,000 | 250 plus 5% of sales
# Less than 10,000                                     | 200 plus 3% of sales


# Using this information, write a Python program that will accept the salesman's Monthly Sales display the Income.
# For testing purposes, verify your program by using the following input. Display all the output needed.


#   Monthly Sales   |          Income   
# 70,000.00         | Answer: Your Total Income: 11575.0
# 45,000.00         | Answer: Your Total Income: 6650.000000000001
# 35,000            | Answer: Your Total Income: 4525.0
# 15,000            | Answer: Your Total Income: 1000.0
# 5,000             | Answer: Your Total Income: 350.0



print("""
================================================
+     Salesman's Monthly Sales Computation.    +
================================================""")

sales = int(input('Enter Your Monthly Sales: '))

# system logic formula.
if sales >= 50000:
    income = 375 + sales * 0.16
elif sales >= 40000:
    income = 350 + sales * 0.14
elif sales >= 30000:
    income = 325 + sales * 0.12
elif sales >= 20000:
    income = 300 + sales * 0.09
elif sales >= 10000:
    income = 250 + sales * 0.05
elif sales < 10000:
    income = 200 + sales * 0.03
else:
    income = print('Input Error.')

print('Your Total Income:', income)