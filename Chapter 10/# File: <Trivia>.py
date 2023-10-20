# File: <Trivia Game>
# Description: <A program that plays a Trivia Game>
# Assignment Name and Number: #9 of Chapter 10
#
# Name: <Zachary Windus>
# GitHub: <Vizorel>
#
# On my honor, <Zachary Windus>, this programming assignment is my own work
# and I have not provided this code to any other student.
class Question:
    def __init__(self, question, choices, correct_answer):
        self.question = question
        self.choices = choices
        self.correct_answer = correct_answer

    def get_question(self):
        return self.question

    def get_choices(self):
        return self.choices

    def get_correct_answer(self):
        return self.correct_answer

def main():
    trivia_questions = [
        Question('What is the capital of France?', ['1. London', '2. Berlin', '3. Paris', '4. Madrid'], 3),
        Question('Which planet is known as the Red Planet?', ['1. Mars', '2. Venus', '3. Earth', '4. Jupiter'], 1),
        Question('What is the largest mammal in the world?', ['1. Elephant', '2. Blue Whale', '3. Giraffe', '4. Rhino'], 2),
        Question('What is 2+2', ['1. 22', '2. 2', '3. 69', '4. 34'], 2),
        Question('What is not the largest mammal in the world?', ['1. Elephant', '2. Blue Whale', '3. Giraffe', '4. Pygmy possum'], 4),
        Question('What river was dammed to create the International Amistad Reservoir?',['1. Rio Grande River', '2. Indus River', '3. Danube River', '4. Ob River'], 1),
        Question('How are U-shaped valleys formed?', ['1. Water', '2. Errosion', '3. Ice', '4. God'], 3),
        Question('Which US state shares a border with Ohio, Indiana and Wisconsin?', ['1. California', '2. Minnesota', '3. Boston', '4. Michigan'], 4),
        Question("What was the name of the world's last passenger pigeon?", ['1. Martha', '2. Bob', '3. pigeon #2,147,483,647', '4. Drug Bird'], 1),
        Question("Which is Earth's smallest ocean?", ['1. Atlantic Ocean', '2. Pacific Ocean', '3. Indian Ocean', '4. Arctic Ocean'], 4),
    ]
    player1_score = 0
    player2_score = 0

    for i, question in enumerate(trivia_questions, 1):
        print(f'\nQuestion {i}: {question.get_question()}')
        for choice in question.get_choices():
            print(choice)

        player1_answer = int(input('Player 1, enter your answer (1-4): '))
        player2_answer = int(input('Player 2, enter your answer (1-4): '))

        if player1_answer == question.get_correct_answer():
            player1_score += 1

        if player2_answer == question.get_correct_answer():
            player2_score += 1

    print('\nGame Over! Final Scores:')
    print(f'Player 1 Score: {player1_score}')
    print(f'Player 2 Score: {player2_score}')

    if player1_score > player2_score:
        print('Player 1 wins!')
    elif player2_score > player1_score:
        print('Player 2 wins!')
    else:
        print("It's a tie!")

if __name__ == '__main__':
    main()
