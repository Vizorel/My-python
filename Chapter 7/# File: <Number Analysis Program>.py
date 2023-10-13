# File: <Number Analysis Program>
# Description: < a program that asks the user to enter a series of 20 numbers and will store the numbers in a list that will then display the following data>
# Assignment Name and Number: #4 of Chapter 7
#
# Name: <Zachary Windus>
# GitHub: <Vizorel>
#
# On my honor, <Zachary Windus>, this programming assignment is my own work
# and I have not provided this code to any other student.
# Initialize an empty list to store the numbers
from statistics import mean
numbers = []
num = 0
total = 0
for i in range(20):
    num = int(input('enter a number: '))
    numbers.append(num)
    total += num
max = max(numbers)
min = min(numbers)
avg = mean(numbers)
print('the Max number is', max)
print('the Min number is', min)
print('the Average is', avg)
print('the Total is', total)