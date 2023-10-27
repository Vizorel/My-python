# File: <Kinetic Energy>
# Description: <a program that asks the user to enter values for mass and velocity, then calls the kinetic_energy function to get the object’s kinetic energy>
# Assignment Name and Number: #14 of Chapter 5
#
# Name: <Zachary Windus>
# GitHub: <Vizorel>
#
# On my honor, <Zachary Windus>, this programming assignment is my own work
# and I have not provided this code to any other student.
KE = 0
M = 0
V = 0
M = int(input('enter the objects Mass: '))
V = int(input('enter the objects Velocity: '))
def Kenetic_energy (M, V):
    KE = 1/2 * (M*(V**2))
    print('the kenetic energy of the object is', KE)
Kenetic_energy(M, V)