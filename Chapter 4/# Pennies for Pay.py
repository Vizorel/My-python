# File: <Pennies for Pay>
# Description: <the program will tell you how many pennies you will have if the amount of pennies you had doubled each day>
# Assignment Name and Number: #7 chapter 4
#
# Name: <Zachary Windus>
# GitHub: <Vizorel>
#
# On my honor, <Zachary Windus>, this programming assignment is my own work
# and I have not provided this code to any other student.
print('your salary is ¢1 + the amount of of pennies you earned the day before')
print()
print('so on your first day you make ¢1 and on the second day you make ¢2')
print()
days = int(input('enter the number of days that you work (do not enter 0): '))
print()
pennies = 1
nnumberofdays = 1
if nnumberofdays != days:
    while nnumberofdays != days:
        nnumberofdays = (nnumberofdays + 1)
        pennies = pennies*2
        if nnumberofdays == days:
            break
print('with in ', days, ' days you have earned ', pennies, ' pennies.')