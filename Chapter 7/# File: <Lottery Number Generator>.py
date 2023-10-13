# File: <Lottery Number Generator>
# Description: < a program that generates a seven-digit lottery number>
# Assignment Name and Number: #2 of Chapter 7
#
# Name: <Zachary Windus>
# GitHub: <Vizorel>
#
# On my honor, <Zachary Windus>, this programming assignment is my own work
# and I have not provided this code to any other student.
import random
loop = 7
Results = []
for i in range(loop):
    Results.append(random.randrange(0, 10))
print(Results)