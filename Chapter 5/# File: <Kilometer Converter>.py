# File: <Kilometer Converter>
# Description: <converts kilometers into miles>
# Assignment Name and Number: #1 of Chapter 5
#
# Name: <Zachary Windus>
# GitHub: <Vizorel>
#
# On my honor, <Zachary Windus>, this programming assignment is my own work
# and I have not provided this code to any other student.
def convert_to_miles ():
    kilo = float(input('give me a distance in km (just the number): '))
    mile = float(kilo*0.6214)
    print(kilo, 'km is equal to ', mile, 'miles')

convert_to_miles()
