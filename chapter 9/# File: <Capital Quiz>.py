# File: <Capital Quiz>
# Description: <a program that creates a dictionary containing the U.S. states as keys, and their capitals as values>
# Assignment Name and Number: #2 of Chapter 9
#
# Name: <Zachary Windus>
# GitHub: <Vizorel>
#
# On my honor, <Zachary Windus>, this programming assignment is my own work
# and I have not provided this code to any other student.
import random

us_states_and_capitals = {
    'Alabama': 'Montgomery',
    'Alaska': 'Juneau',
    'Arizona': 'Phoenix',
    'Arkansas': 'Little Rock',
    'California': 'Sacramento',
    'Colorado': 'Denver',
    'Connecticut': 'Hartford',
    'Delaware': 'Dover',
    'Florida': 'Tallahassee',
    'Georgia': 'Atlanta',
    'Hawaii': 'Honolulu',
    'Idaho': 'Boise',
    'Illinouis': 'Springfield',
    'Indiana': 'Indianapolis',
    'Iowa': 'Des Moines',
    'Kansas': 'Topeka',
    'Kentucky': 'Frankfort',
    'Louisiana': 'Baton Rouge',
    'Maine': 'Augusta',
    'Maryland': 'Annapolis',
    'Massachusetts': 'Boston',
    'Michigan': 'Lansing',
    'Minnesota': 'Saint Paul',
    'Mississippi': 'Jackson',
    'Missouri': 'Jefferson City',
    'Montana': 'Helena',
    'Nebraska': 'Lincoln',
    'Nevada': 'Carson City',
    'New Hampshire': 'Concord',
    'New Jersey': 'Trenton',
    'New Mexico': 'Santa Fe',
    'New York': 'Albany',
    'North Carolina': 'Raleigh',
    'North Dakota': 'Bismarck',
    'Ohio': 'Columbus',
    'Oklahoma': 'Oklahoma City',
    'Oregon': 'Salem',
    'Pennsylvania': 'Harrisburg',
    'Rhode Island': 'Providence',
    'South Carolina': 'Columbia',
    'South Dakota': 'Pierre',
    'Tennessee': 'Nashville',
    'Texas': 'Austin',
    'Utah': 'Salt Lake City',
    'Vermont': 'Montpelier',
    'Virginia': 'Richmond',
    'Washington': 'Olympia',
    'West Virginia': 'Charleston',
    'Wisconsin': 'Madison',
    'Wyoming': 'Cheyenne'
}
correct_responses = 0
incorrect_responses = 0
states_to_quiz = list(us_states_and_capitals.keys())
num_questions = 5  

for _ in range(num_questions):
    random_state = random.choice(states_to_quiz)
    user_answer = input(f'What is the capital of {random_state}? ').strip()
    if user_answer == us_states_and_capitals[random_state]:
        print('Correct!')
        correct_responses += 1
    else:
        print(f'Incorrect. The capital of {random_state} is {us_states_and_capitals[random_state]}.')
        incorrect_responses += 1
print('\nQuiz Complete!')
print(f'You got {correct_responses} correct and {incorrect_responses} incorrect responses.')