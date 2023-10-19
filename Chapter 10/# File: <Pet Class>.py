# File: <Pet Class>
# Description: <A program that ask the user for pet info>
# Assignment Name and Number: #1 of Chapter 10
#
# Name: <Zachary Windus>
# GitHub: <Vizorel>
#
# On my honor, <Zachary Windus>, this programming assignment is my own work
# and I have not provided this code to any other student.
class Pet:
    def __init__(self, name, animal_type, age):
        self.__name = name
        self.__animal_type = animal_type
        self.__age = age

    def set_name(self, name):
        self.__name = name

    def set_animal_type(self, animal_type):
        self.__animal_type = animal_type

    def set_age(self, age):
        self.__age = age

    def get_name(self):
        return self.__name

    def get_animal_type(self):
        return self.__animal_type

    def get_age(self):
        return self.__age

# Create an object of the Pet class
pet = Pet('', '', 0)

# Prompt the user to enter pet details
name = input("Enter the pet's name: ")
animal_type = input("Enter the pet's type (e.g., Dog, Cat, Bird): ")
age = int(input("Enter the pet's age: "))

# Set the pet's attributes using the setter methods
pet.set_name(name)
pet.set_animal_type(animal_type)
pet.set_age(age)

# Display the pet's information using the getter methods
print('\nPet Information:')
print('Name: ' + pet.get_name())
print('Type: ' + pet.get_animal_type())
print('Age: ' + str(pet.get_age()))