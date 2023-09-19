# File: <hotdog cookout>
# Description: <tells us how many hotdogs and buns need to be ordered for a cookout>
# Assignment Name and Number: program exersize chapter 3
#
# Name: <Zachary Windus>
# GitHub: <Vizorel>
#
# On my honor, <Zachary Windus>, this programming assignment is my own work
# and I have not provided this code to any other student.
import math
print()
print('______________________________________________________________________________________________________________________________')
print()
People = int(input('how many people will be attending?: '))
if People == 0:
    while People ==0:
        print()
        print("the number of people can't be 0")
        print()
        People = int(input('how many people will be attending?: '))
        print()
        if People > 0:
            break
print('hot dogs come in packages of 10, and hot dog buns come in packages of 8')
print()
print("so we'll have to solve how many hotdogs are needed to order to have the least amount of leftovers")
Hotdogs = People/10
strHotdogs = str(Hotdogs)
if strHotdogs.isdecimal() == False:
    strHotdogs = math.ceil(Hotdogs)
Hotdogs =int(strHotdogs)
Buns = People/8
strBuns = str(Buns)
if strBuns.isdecimal() == False:
    strBuns = math.ceil(Buns)
Buns =int(strBuns)
print()
if People > 1:
    print("there will be ", People, " people at the cookout so we'll need to order this many hotdogs packages: ", Hotdogs, " and this many bun packages: ", Buns)
else:
    print("there will be " , People, " person at the cookout so we'll need to order this many hotdog packages: ", Hotdogs, " and this many bun packages: ", Buns)
print()
Hleftovers = (Hotdogs * 10)-People
Bleftovers = (Buns * 8)-People
print('after the cookout there will be this many hotdogs leftover: ', Hleftovers, ' and this many bun leftovers: ', Bleftovers)
print()
print('______________________________________________________________________________________________________________________________')
print()
