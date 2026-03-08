#Comparison Operator Exercise 2. - Temperature Checker.

#create a python code for temperature testing if less than or equal to 36.9 degrees, pwede pumasok.
#if more than or equal 37 degrees, bawal pumasok.


temperature = float(input('What\'s temperature degree?: '))

passed_degree = 36.9
failed_degree = 37


if temperature <= passed_degree:
    print(str(temperature)+', - Your Temperature is good, allowed to enter.')
    #output:
    #What's temperature degree?: 35.5
    #35.5, - Temperature good, allowed to enter.
else:
    if temperature >= failed_degree:
        print(str(temperature)+', - Your Temperature is not good, not allowed to enter.')
        #output:
        #What's temperature degree?: 37.5
        #37.5, - Your Temperature is not good, not allowed to enter.