# File: <Turtle Graphics: Repeating Squares>
# Description: <draws 100 squares using a loop>
# Assignment Name and Number: #16 chapter 4
#
# Name: <Zachary Windus>
# GitHub: <Viorel>
#
# On my honor, <Zachary Windus>, this programming assignment is my own work
# and I have not provided this code to any other student.
import turtle
t = turtle.Turtle()
t.pensize(1)
t.pendown
t.left(180)
forward = 0
squares = 100
for i in range(squares):
    forward = forward + 10
    t.forward(forward)
    t.right(90)
    t.forward(forward)
    t.right(90)
    t.forward(forward)
    t.right(90)
    t.forward(forward)
    t.right(90)