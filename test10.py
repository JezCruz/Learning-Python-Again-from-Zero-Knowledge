#IF and Else-If.


average = int(input('Enter your Average Grade. (e.g. 95): '))

if average >= 98 and average <= 100:
    print('1.00')
elif average >= 90 and average <= 97:
    print('1.25')
elif average >= 85 and average <= 89:
    print('1.50')
elif average >= 80 and average <= 84:
    print('2.00')
elif average >= 77 and average <= 79:
    print('3.00')
elif average >= 75 and average <= 76:
    print('5.00')
else:
    print('failed')


#Average:
#98 - 100 = 1.00
#90 - 97 = 1.25
#85 - 89 = 1.50
#80 - 84 = 2.00
#77 - 79 = 3.00
#75 - 76 = 5.00
#then if the average grade is not 75 in between 100 = failed.