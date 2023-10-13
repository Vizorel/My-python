# File: <Magic 8 Ball>
# Description: <a program that simulates a Magic 8 Ball>
# Assignment Name and Number: #13 of Chapter 7
#
# Name: <Zachary Windus>
# GitHub: <Vizorel>
#
# On my honor, <Zachary Windus>, this programming assignment is my own work
# and I have not provided this code to any other student.
import random


with open('/Users/ZacharyWindus/Downloads/8_ball_responses.txt', 'r') as file:
    responses = file.read().splitlines()

def magic_8_ball():
    while True:
        question = input("Ask the Magic 8 Ball a yes or no question (or 'quit' to exit): ").lower()
        if question == 'quit':
            print("Goodbye!")
            break

        if '?' not in question:
            print("Please ask a yes or no question.")
        else:
            random_response = random.choice(responses)
            print(random_response)

if __name__ == "__main__":
    print("Welcome to the Magic 8 Ball!")
    magic_8_ball()
