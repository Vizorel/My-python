# File: <(month)(day)=year?>
# Description: <tells us if the month times the day is equal to the year>
# Assignment Name and Number: program exersize chapter 3
#
# Name: <Zachary Windus>
# GitHub: <Vizorel>
#
# On my honor, <Zachary Windus>, this programming assignment is my own work
# and I have not provided this code to any other student.
print()
print('______________________________________________________________________________________________________________________________')
print()
print('enter the following in numerical value')
Month = int(input('enter the Month: '))
if Month >= 13:
    while Month >=13:
        print()
        print('error not real month value(1-12)')
        print()
        Month = int(input('enter the Month: '))
        print()
        if Month <=12:
            break

Day = int(input('enter the Day: '))
if Day >= 32:
    while Day >= 32:    
        print()
        print('error not real Day value(1-31)')
        print()
        Day = int(input('enter the Day: '))
        print()
        if Day <= 31:
            break

if Month == 2 & Day >= 28:
    while Day >= 28:
        print()
        print('error not real Day value(1-28)')
        print()
        Day = int(input('enter the Day: '))
        print()
        if Day <= 28:
            break
    
elif Month == 4 & Day >= 30:
    while Day >=30:
        print()
        print('error not real Day value(1-30)')
        print()
        Day = int(input('enter the Day: '))
        print()
        if Day <= 30:
            break

elif Month == 6 & Day >= 30:
    while Day >=30:
        print()
        print('error not real Day value(1-30)')
        print()
        Day = int(input('enter the Day: '))
        print()
        if Day <= 30:
            break

elif Month == 9 & Day >= 30:
    while Day >=30:
        print()
        print('error not real Day value(1-30)')
        print()
        Day = int(input('enter the Day: '))
        print()
        if Day <= 30:
            break

elif Month == 11 & Day >= 30:
    while Day >=30:
        print()
        print('error not real Day value(1-30)')
        print()
        Day = int(input('enter the Day: '))
        print()
        if Day <= 30:
            break

Year = int(input('enter the Year: '))
if Year >=100:
    while Year >=100:
        print()
        print('error this year is not usable')
        print()
        Year = int(input('enter the Year: '))
        print()
        if Year <=99:
            break

print()
print('______________________________________________________________________________________________________________________________')
print()
print()
print('the date is: ', Month, '/', Day, '/', Year)
print()
print('will the Month and Day be equal to the year if they are both multiplied?')
print()
if (Month * Day) == Year:
    print('Yes! the Month times the Day is equal to the year')
else:
    print('no. the Month times the Day is not equal to the year')
print('______________________________________________________________________________________________________________________________')
print()
