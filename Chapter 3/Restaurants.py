# File: <Resturants>
# Description: <Tells us what resturants we can go to within the give dietary restictions>
# Assignment Name and Number: program exersize chapter 3
#
# Name: <Zachary Windus>
# GitHub: <Vizorel>
#
# On my honor, <Zachary Windus>, this programming assignment is my own work
# and I have not provided this code to any other student.
print('make sure to answer the folloing questions with 0(yes) or 1(no).')
print()
vegan = int(input('is anyone in your party vegan: '))
print()
vegetarian = int(input('is anyone in your party vegetarian: '))
print()
glutenfree = int(input('is anyone in your party gluten-free: '))
print()

Resturant1 = [1, 1, 1]
Resturant2 = [0, 1, 0]
Resturant3 = [0, 0, 0]
Resturant4 = [0, 1, 1]
Resturant5 = [0, 0, 0]

errorlist1 = [1,0,0]
errorlist2 = [1,1,0]
errorlist3 = [0,0,1]
errorlist4 = [1,0,1]




Resturantokays = []
group = []
if vegan == 0:
    group.append(0)
else:
    group.append(1)

if vegetarian == 0:
    group.append(0)
else:
    group.append(1)

if glutenfree == 0:
    group.append(0)
else:
    group.append(1)

if group == Resturant1:
    Resturantokays.append("Joe's Gourmet Burgers")
if group == Resturant2:
    Resturantokays.append("Main Street Pizza Company")
if group == Resturant3:
    Resturantokays.append("Corner Café")
if group == Resturant4:
    Resturantokays.append("Mama's Fine Italian")
if group == Resturant5:
    Resturantokays.append("The Chef's Kitchen")
if group == errorlist1:
    print('since we have: ', vegan, ' vegans, ', vegetarian, ' vegetarians, and ', glutenfree, " gluten-free restrictions we can't go to any resturant")
elif group == errorlist2:
    print('since we have: ', vegan, ' vegans, ', vegetarian, ' vegetarians, and ', glutenfree, " gluten-free restrictions we can't go to any resturant")
elif group == errorlist3:
    print('since we have: ', vegan, ' vegans, ', vegetarian, ' vegetarians, and ', glutenfree, " gluten-free restrictions we can't go to any resturant")
elif group == errorlist4:
    print('since we have: ', vegan, ' vegans, ', vegetarian, ' vegetarians, and ', glutenfree, " gluten-free restrictions we can't go to any resturant")
else:
    print('since we have: ', vegan, ' vegans, ', vegetarian, ' vegetarians, and ', glutenfree, ' gluten-free restrictions we can go to the following resturants: ', Resturantokays)
