# File: <Dice Rolling Function>
# Description: < a function named roll that accepts an integer argument number_of_throws. The function should generate and return a sorted list of number_of_throws random numbers between 1 and 6. The program should prompt the user to enter a positive integer that is sent to the function, and then print the returned list.>
# Assignment Name and Number: #6 of Chapter 7
#
# Name: <Zachary Windus>
# GitHub: <Vizorel>
#
# On my honor, <Zachary Windus>, this programming assignment is my own work
# and I have not provided this code to any other student.
# Read the correct answers from a list
import random

def roll(number_of_throws):
    random_numbers = [random.randint(1, 6) for _ in range(number_of_throws)]
    random_numbers.sort()
    return random_numbers

def main():
    try:
        number_of_throws = int(input("Enter the number of throws: "))
        if number_of_throws <= 0:
            print("Please enter a positive integer.")
        else:
            result = roll(number_of_throws)
            print("Sorted list of random numbers:", result)
    except ValueError:
        print("Invalid input. Please enter a positive integer.")

main()
