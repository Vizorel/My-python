# File: <Driver’s License Exam>
# Description: <Grades a driver's license test>
# Assignment Name and Number: #7 of Chapter 7
#
# Name: <Zachary Windus>
# GitHub: <Vizorel>
#
# On my honor, <Zachary Windus>, this programming assignment is my own work
# and I have not provided this code to any other student.
# Read the correct answers from a list
correct_answers = ['A', 'C', 'A', 'A', 'D', 'B', 'C', 'A', 'C', 'B', 'A', 'D', 'C', 'A', 'D', 'C', 'B', 'B', 'D', 'A']

total_correct = 0
total_incorrect = 0
incorrect_questions = []


with open('/Users/ZacharyWindus/Downloads/student_answers.txt', 'r') as file:
    student_answers = file.read().splitlines()


for i in range(len(correct_answers)):
    if student_answers[i] == correct_answers[i]:
        total_correct += 1
    else:
        total_incorrect += 1
        incorrect_questions.append(i + 1)


passing_score = 15
if total_correct >= passing_score:
    result = "Pass"
else:
    result = "Fail"

print(f"Result: {result}")
print(f"Total Correct Answers: {total_correct}")
print(f"Total Incorrect Answers: {total_incorrect}")
print(f"Incorrectly Answered Questions: {incorrect_questions}")
