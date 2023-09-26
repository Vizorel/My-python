# File: <Stadium Seating>
# Description: <a program that asks how many tickets for each class of seats were sold, then displays the amount of income generated from ticket sales>
# Assignment Name and Number: #7 of Chapter 5
#
# Name: <Zachary Windus>
# GitHub: <Vizorel>
#
# On my honor, <Zachary Windus>, this programming assignment is my own work
# and I have not provided this code to any other student.
tsoldA = int(input('how many tickets were sold for Class A: '))
tsoldB = int(input('how many tickets were sold for Class B: '))
tsoldC = int(input('how many tickets were sold for Class C: '))
Acost = 20
Bcost = 15
Ccost = 10
Aincome = Acost*tsoldA
Bincome = Bcost*tsoldB
Cincome = Ccost*tsoldC
Totalincome = Aincome + Bincome + Cincome
TSsold = tsoldC+tsoldB+tsoldA
print('Section A sold', tsoldA, 'tickets. Section B sold', tsoldB, 'tickets. Section C sold', tsoldC, 'tickets')
print('so in total we sold', TSsold, 'total tickets earning us $', Totalincome)
