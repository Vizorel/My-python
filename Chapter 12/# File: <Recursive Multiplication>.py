# File: <Recursive Multiplication>
# Description: <shows us the process of a multipcation equation>
# Assignment Name and Number: #2 of Chapter 12
#
# Name: <Zachary Windus>
# GitHub: <Vizorel>
#
# On my honor, <Zachary Windus>, this programming assignment is my own work
# and I have not provided this code to any other student.
x = int(input('give me a number: '))
y = int(input('give me another number: '))
equation_list = []
solution = (x*y)
yfor = y - 1
for i in range(yfor):
    equation_list.append(x)
    equation_list.append('+')
equation_list.append(x)
print('the recursive multiplication of (', x, ')(', y, ') is ', format(equation_list), '=', solution)
