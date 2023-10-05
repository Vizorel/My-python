def Monthcheck ():
    if Month >= 13:
        while Month >=13:
            print()
            print('error invalid Month(1-12)')
            print()
            Month = int(input('what Month is it: '))
            print()
            if Month <=12:
                break
def Daycheck():
    if Day >= 32:
        while Day >= 32:    
            print()
            print('error invalid Day(1-31)')
            print()
            Day = int(input('what Day is it: '))
            print()
            if Day <= 31:
                break

    if Month == 2 & Day >= 28:
        while Day >= 28:
            print()
            print('error invalid Day(1-28)')
            print()
            Day = int(input('what Day is it: '))
            print()
            if Day <= 28:
                break
        
    elif (Month == 4 or Month == 6 or Month == 9 or Month == 11) & Day >= 30:
        while Day >=30:
            print()
            print('error invalid Day(1-30)')
            print()
            Day = int(input('what Day is it: '))
            print()
            if Day <= 30:
                break

Year = int(input('what Year is it: '))
Month = int(input('what Month is it: '))
Day = int(input('what Day is it: '))
Monthcheck()
Daycheck()
Skip = int(input('how many days have been skipped: '))

if Day + Skip > 28 and Month == 2: #checks the month
    DMchange = round((Day + Skip) / 28) #divides the amount of days into months
    
elif Day + Skip > 30 and (Month == 4 or Month == 6 or Month == 9 or Month == 11): #checks the month
    print()
elif Day + Skip > 31: #checks the month
    print()
else:
    FinalDay = Day + Skip