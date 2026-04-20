#Converting Data Types.

#manghihingi ng stick ng fishball na order nya
#manghihingi ng pera nya
#ang price ng 1 stick ng fishball ay 20 pesos
#ipapakita sa kanya kung ilang sticks ng fishball ang binili nya
#ipapakita sa kanya kung magkano ang total ng order nya
#ibibigay ng system kung magkano ang sukli nya

price_per_stick = 15.31

print('Welcome sa fishball stand!')
print('Ang presyo ng 1 stick ng fishball ay ' + str(price_per_stick) +' pesos.\n')

numsticks = input('Ilang sticks ng fishball ang bibilhin mo? ')
peranya = input('Magkano yung pera mo? ')

#formula para malaman ang total ng order at sukli
total = float(numsticks) * price_per_stick
change = float(peranya) - total

print('\n\n~Order Receipt~')
print('\nOrder: ' + str(numsticks) + ' sticks of fishballs')
print('Total Order: ' + str(round(total, 2)) + ' pesos')
print('Cash: ' + str(round(float(peranya), 2)) + ' pesos')
print('Change:  ' + str(round(change, 2)) + ' pesos\n')

#Output:
#Welcome sa fishball stand!
#Ang presyo ng 1 stick ng fishball ay 20 pesos.

#Ilang sticks ng fishball ang bibilhin mo? 2
#Magkano yung pera mo? 45

#~Order Receipt~
#Order: 2 sticks of fishballs
#Total Order: 40 pesos
#Cash: 500 pesos
#Change: 460 pesos


#I add a float() function to convert the string input into a float data type 
#so that I can perform mathematical operations on it.

#I also added a round() function to round the total, cash, and change to 2 decimal places for better presentation.