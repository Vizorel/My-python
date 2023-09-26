# File: <Paint Job Estimator>
# Description: < display the following data: The number of gallons of paint required, The hours of labor required, The cost of the paint, The labor charges, The total cost of the paint job>
# Assignment Name and Number: #8 of Chapter 5
#
# Name: <Zachary Windus>
# GitHub: <Vizorel>
#
# On my honor, <Zachary Windus>, this programming assignment is my own work
# and I have not provided this code to any other student.
Spacereqpainted = int(input('enter the amount of wall space that needs to be painted (in square feet): '))
PGallon = int(input('enter the price of paint per gallon (exclude the $): '))
reqgallons = Spacereqpainted / 112
Labortime = (Spacereqpainted / 112) * 8
payperhour =  Labortime * 35
TPgallon = PGallon * reqgallons
totalprice =payperhour + TPgallon
print('the amount of Gallons of paint required is', reqgallons, 'gallons')
print('the amount of hours of labor required is', Labortime, 'hours')
print('the cost of paint is $', PGallon, 'per gallon')
print('you will have to pay $ 35 per hour so...')
print('the total amount of money required to pay for the labor is $', payperhour)
print('in total you will have to pay $', totalprice)