# File: <Falling Distance>
# Description: <a program that calls the function in a loop that passes the values 1 through 10 as arguments and displays the return value>
# Assignment Name and Number: #13 of Chapter 5
#
# Name: <Zachary Windus>
# GitHub: <Vizorel>
#
# On my honor, <Zachary Windus>, this programming assignment is my own work
# and I have not provided this code to any other student.
g=9.8
x = 0
t = 0
timeinterval= int(input('give me a time in seconds: '))
def Falling_distance (t):
    x = (1/2)*g*(t**2)
    print('in ', t, 'seconds we have fallen', x, 'meters.')

for i in range(timeinterval):
    t = t+1
    Falling_distance(t)
    