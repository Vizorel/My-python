# File: <Largest List Item>
# Description: <a function that accepts a list as an argument and returns the largest value in the list>
# Assignment Name and Number: #4 of Chapter 12
#
# Name: <Zachary Windus>
# GitHub: <Vizorel>
#
# On my honor, <Zachary Windus>, this programming assignment is my own work
# and I have not provided this code to any other student.
times = int(input('how long will the list be: '))
num = 0
numlist=[]
def numbers(times):
   if times > 0:
    num = int(input('give me a number: '))
    numlist.append(num)
    numbers(times - 1)

numbers(times)
largest_number = max(numlist)
print(numlist)
print(largest_number)