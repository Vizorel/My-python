# File: <Magic 8 Ball>
# Description: <>
# Assignment Name and Number: #13 of Chapter 7
#
# Name: <Zachary Windus>
# GitHub: <Vizorel>
#
# On my honor, <Zachary Windus>, this programming assignment is my own work
# and I have not provided this code to any other student.

#important note: I think I broke python becuase if you enter a response it won't answer it but if you click run pytho file it will answer the previous question idk why
#either that or its just answering before you respond... either way I am so confused and don't know how to fix this error if you could help me that would be great
import random

responses = 0
def magic_8_ball(responses):
    print("Welcome to the Magic 8 Ball!")
    while True:
        question = input("Ask the Magic 8 Ball a yes or no question (or type 'quit' to exit): ")
        if question.lower() == 'quit':
            break
        
        response = random.choice(responses)
        print(f"Magic 8 Ball says: {response}\n")

def load_responses(filename):
   with open(filename, 'r') as file:
    responses = file.read().splitlines()
    return responses

magic_8_ball(responses)
responses = load_responses("/Users/ZacharyWindus/Downloads/8_ball_responses.txt")
