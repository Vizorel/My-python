# File: <Recursive Multiplication>
# Description: <a recursive function that accepts two arguments into the parameters x and y. The function should return the value of x times y>
# Assignment Name and Number: #2 of Chapter 12
#
# Name: <Zachary Windus>
# GitHub: <Vizorel>
#
# On my honor, <Zachary Windus>, this programming assignment is my own work
# and I have not provided this code to any other student.
x = int(input('give me a number: '))
y = int(input('give me another number: '))
solution = (x*y)
equation = []
def test(x, y):
    if y > 1:
        equation.append(x)
        equation.append('+')
        test(x, y-1)
    elif y == 1:
        equation.append(x)
test(x, y)
print('the recursive multiplication of (', x, ')(', y, ') is ', equation, '=', solution)
