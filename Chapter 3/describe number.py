# File: <describe number>
# Description: <describes if the number is a positive or a negitive and if its even or odd>
# Assignment Name and Number: program exersize chapter 3
#
# Name: <Zachary Windus>
# GitHub: <Vizorel>
#
# On my honor, <Zachary Windus>, this programming assignment is my own work
# and I have not provided this code to any other student.
integer = int(input('please input an integer (do not add the negative symbol yet): '))
evenodd = (integer % 2)

if integer != 0:
    negative = int(input('was your number a negative (respond with 1 for yes and 0 for no): '))
    if negative == 0:
        if evenodd == 0:
            print('the number is a positive even number')
        else:
            print('the number is a positive odd number')

    elif negative == 1:
        if evenodd == 0:
            print('the number is a negative even number')
        else:
            print('the number is a negative odd number')
elif integer == 0:
    print('the number is Zero')
