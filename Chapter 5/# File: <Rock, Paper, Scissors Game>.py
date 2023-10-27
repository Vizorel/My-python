# File: <Rock, Paper, Scissors Game>
# Description: < a program that lets the user play the game of Rock, Paper, Scissors against the computer>
# Assignment Name and Number: #21 of Chapter 5
#
# Name: <Zachary Windus>
# GitHub: <Vizorel>
#
# On my honor, <Zachary Windus>, this programming assignment is my own work
# and I have not provided this code to any other student.
import random

def get_user_choice():
    while True:
        user_choice = input('Choose Rock, Paper, or Scissors: ').strip().lower()
        if user_choice in ['rock', 'paper', 'scissors']:
            return user_choice
        else:
            print('Invalid choice. Please choose Rock, Paper, or Scissors.')

def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif user_choice == 'rock' and computer_choice == 'scissors':
        return 'You win!'
    elif user_choice == 'paper' and computer_choice == 'rock':
        return 'You win!'
    elif user_choice == 'scissors' and computer_choice == 'paper':
        return 'You win!'
    else:
        return 'Computer wins!'

def main():
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print(f'You chose {user_choice}.')
        print(f'The computer chose {computer_choice}.')

        result = determine_winner(user_choice, computer_choice)
        print(result)

if __name__ == '__main__':
    print('lets play a game')
    main()
