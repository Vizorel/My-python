# File: <Roulette>
# Description: <plays a round of roulette without losing money>
# Assignment Name and Number: program exersize chapter 3
#
# Name: <Zachary Windus>
# GitHub: <Vizorel>
#
# On my honor, <Zachary Windus>, this programming assignment is my own work
# and I have not provided this code to any other student.
Bidnumber = int(input('what pocket would you like to bid on (0-36): '))
if Bidnumber >=37:
    while Bidnumber >=37:
        print()
        print('error not a valid number')
        print()
        Bidnumber = int(input('what pocket would you like to bid on (0-36): '))
        if Bidnumber <=36:
            break

if Bidnumber == 0:
    Bidcolor = 'green'

elif Bidnumber <= 10:
    if (Bidnumber & 2) == 0: #if the bid is even
        Bidcolor = "black"
    else: #if the bid is odd
        Bidcolor = "red"

elif Bidnumber <= 18:
    if (Bidnumber & 2) == 0: #if the bid is even
        Bidcolor = "red"
    else: #if the bid is odd
        Bidcolor = "black"

elif Bidnumber <= 28:
    if (Bidnumber & 2) == 0: #if the bid is even
        Bidcolor = "black"
    else: #if the bid is odd
        Bidcolor = "red"

elif Bidnumber <= 36:
    if (Bidnumber & 2) == 0: #if the bid is even
        Bidcolor = "red"
    else: #if the bid is odd
        Bidcolor = "black"


print()
print('You bet on ', Bidnumber, ' which is a ', Bidcolor, ' number')
