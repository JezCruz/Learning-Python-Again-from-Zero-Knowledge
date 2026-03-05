#Converting Data Types Exercise 2

# USD to Php Converter

print('~ USD to Php Converter ~\n')

print('(e.g. 1 USD = 50 Php, then enter 50)\n')
exrate = float(input('Magkano ang 1 Dollar toPHP ngayon? '))
usdAmount = float(input('Ilang USD ang iko-convert natin? '))

#formula of conversion
phpValue = exrate * usdAmount


print('\nAng ' + str(usdAmount) + ' USD ay katumbas ng ' + str(phpValue) + ' Php\n')

#~ USD to Php Converter ~
#
#(e.g. 1 USD = 50 Php, then enter 50)
#
#Magkano ang 1 Dollar toPHP ngayon? 55.75
#Ilang USD ang iko-convert natin? 100

#Ang 100.0 USD ay katumbas ng 5575.0 Php