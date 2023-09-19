# File: <Radius of a cirlce>
# Description: <gives the radius of a circle>
# Assignment Name and Number: program exersize chapter 2
#
# Name: <Zachary Windus>
# GitHub: <Vizorel>
#
# On my honor, <Zachary Windus>, this programming assignment is my own work
# and I have not provided this code to any other student.
def main():
    Radius = int(input('Enter the radius of a circle: '))
    P = 3.14159265359

    Area = int( P * Radius**2)
    Circumference = int( 2 * P * Radius)
    print('Using the Given Radius:' , Radius, 'The Area of the Circle would be:' , Area,
    'and the Circumference of the Circle would be:' , Circumference,)
main()
