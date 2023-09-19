# File: <Population>
# Description: <a program that predicts the approximate size of a population of organisms>
# Assignment Name and Number: #13 chapter 4
#
# Name: <Zachary Windus>
# GitHub: <Viorel>
#
# On my honor, <Zachary Windus>, this programming assignment is my own work
# and I have not provided this code to any other student.
popbefore = int(input('give the beginning amount of organisms(any # equal to or greater than 1): '))
growthpercent = float(input('give the growth percent of the species (in decimal form): '))
num_days = int(input('how many days does the organism have to grow: '))
popafter = popbefore
day = 0
day = day + 1
print (day, ' ', popbefore)
if num_days == 1:
    print('on day 1 the population is ', popbefore)
else:
    for i in range(1, num_days):
        day = day + 1
        popafter = float((popafter*growthpercent)+popafter)
        print(day, ' ', popafter)
    print()