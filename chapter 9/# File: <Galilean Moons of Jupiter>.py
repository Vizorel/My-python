# File: <Galilean Moons of Jupiter>
# Description: <a program that displays info of jupiters moons>
# Assignment Name and Number: #1 of Chapter 9
#
# Name: <Zachary Windus>
# GitHub: <Vizorel>
#
# On my honor, <Zachary Windus>, this programming assignment is my own work
# and I have not provided this code to any other student.
mean_radius = {
    'Io': 1821.6,
    'Europa': 1560.8,
    'Ganymede': 2634.1,
    'Callisto': 2410.3
}

surface_gravity = {
    'Io': 1.796,
    'Europa': 1.314,
    'Ganymede': 1.428,
    'Callisto': 1.235
}

orbital_period = {
    'Io': 1.769,
    'Europa': 3.551,
    'Ganymede': 7.154,
    'Callisto': 16.689
}

moon_name = input('Enter the name of a Galilean moon of Jupiter (Io, Europa, Ganymede, Callisto): ')

if moon_name in mean_radius and moon_name in surface_gravity and moon_name in orbital_period:
    print(f'Mean Radius of {moon_name}: {mean_radius[moon_name]}')
    print(f'Surface Gravity of {moon_name}: {surface_gravity[moon_name]}')
    print(f'Orbital Period of {moon_name}: {orbital_period[moon_name]}')

else:
    print('Invalid moon name. Please enter one of the following: Io, Europa, Ganymede, Callisto')
