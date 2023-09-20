# File: <Largest List Item>
# Description: <a function that accepts a list as an argument and returns the largest value in the list>
# Assignment Name and Number: #4 of Chapter 12
#
# Name: <Zachary Windus>
# GitHub: <Vizorel>
#
# On my honor, <Zachary Windus>, this programming assignment is my own work
# and I have not provided this code to any other student.
def sort(n):
  return abs(n - 50)
numList = []
numloop = int(input('how many numbers would you like the list to be: '))
for i in range(numloop):
    num = int(input('give me a number: '))
    numList.append(num)
print('you gave me', numList)
numList.sort(key=sort)
lastnum = numList[-1:][0]
print('according to the list the largest number in the list is', lastnum)
