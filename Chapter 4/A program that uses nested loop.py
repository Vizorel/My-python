# File: <a program that uses nested loops to draw a pattern>
# Description: <a program that uses nested loops to draw a pattern:>
# Assignment Name and Number: #14 chapter 4
#
# Name: <Zachary Windus>
# GitHub: <Viorel>
#
# On my honor, <Zachary Windus>, this programming assignment is my own work
# and I have not provided this code to any other student.
rows = 7
for i in range(rows, 0 , -1):
    print()
    for j in range(i):
        print('* ', end='')