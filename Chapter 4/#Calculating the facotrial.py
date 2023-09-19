# File: <Calculating the facotrial of a number>
# Description: <it asks for a non-negitive number and displays its factorial >
# Assignment Name and Number: #12 chapter 4
#
# Name: <Zachary Windus>
# GitHub: <Viorel>
#
# On my honor, <Zachary Windus>, this programming assignment is my own work
# and I have not provided this code to any other student.
num = int(input('enter a nonnegative integer: '))
fact = 1
if num < 0:
   print('Error, there is no factorial for negative numbers')
elif num == 0:
    print('the factorial of 0 is 1')
else:
    for i in range(1, num + 1):
        fact = fact*i
    print('the factorial of ', num, ' is ', fact)