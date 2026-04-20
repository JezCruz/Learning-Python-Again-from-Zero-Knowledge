# =====================Coffe-Outlet===========================

# Order Volume Discount:

# Below and up to 25 bags        =        -5% of total cost
# 26 to 50 bags                  =        -6% of total cost
# 51 to 100 bags                 =        -7% of total cost
# 101 to 150 bags                =        -8% of total cost
# 151 to 200 bags                =        -9% of total cost
# Above 200                      =        -10% of total cost


# Each bag of beans costs $5.50, Write a program that will accept the number
# of bags ordered and print the total cost of the order based on the output below:

# Sample Output:
# 
# NUMBER OF BAGS ORDERED:        173
# TOTAL COST:                    $951.50
# DICOUNT:                       -$85.635
# YOUR TOTAL CHARGE IS:          $865.865


print('\n===============Hello Welcome to Coffee Outlet=================\n')
print('1 Bag of Coffee Bean = $5.50\n')

# Formula:

number_of_bags = int(input('How many of bags of Coffee Bean do you need?  '))

bags = 5.50

# total cost formula
if number_of_bags <= 25:
    total_cost = bags * number_of_bags
elif number_of_bags <= 50:
    total_cost = bags * number_of_bags
elif number_of_bags <= 100:
    total_cost = bags * number_of_bags
elif number_of_bags <= 150:
    total_cost = bags * number_of_bags
elif number_of_bags <= 200:
    total_cost = bags * number_of_bags
else:
    total_cost = bags * number_of_bags



# total discounted cost formula
if number_of_bags <= 25:
    discount_cost = total_cost * 5 / 100
elif number_of_bags <= 50:
    discount_cost = total_cost * 6 / 100
elif number_of_bags <= 100:
    discount_cost = total_cost * 7 / 100
elif number_of_bags <= 150:
    discount_cost = total_cost * 8 / 100
elif number_of_bags <= 200:
    discount_cost = total_cost * 9 / 100
else:
    discount_cost = total_cost * 10 / 100


# total cost with -%
if number_of_bags <= 25:
    total_charge = bags * number_of_bags * 0.95
elif number_of_bags <= 50:
    total_charge = bags * number_of_bags * 0.94
elif number_of_bags <= 100:
    total_charge = bags * number_of_bags * 0.93
elif number_of_bags <= 150:
    total_charge = bags * number_of_bags * 0.92
elif number_of_bags <= 200:
    total_charge = bags * number_of_bags * 0.91
else:
    total_charge = bags * number_of_bags * 0.90


print('\nNUMBER OF BAGS ORDRED:', str(number_of_bags))
print('\nTOTAL COST:', '$'+str(total_cost))
print('\nDISCOUNT:', '-'+'$'+ str(discount_cost))
print('\nYOUR TOTAL CHARGE IS:', '$'+ str(total_charge))



# Output:
# 
# ===============Hello Welcome to Coffee Outlet=================
# 
# 1 Bag of Coffee Bean = $5.50
# 
# How many of bags of Coffee Bean do you need?  173
# 
# NUMBER OF BAGS ORDRED: 173
# 
# TOTAL COST: $951.5
# 
# DISCOUNT: -$85.635
#
# YOUR TOTAL CHARGE IS: $865.865