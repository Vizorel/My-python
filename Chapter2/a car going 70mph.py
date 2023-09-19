# File: <Car going 70 mph>
# Description: <gives the distance that was traveled by a car going 70mph within the given time>
# Assignment Name and Number: program exersize chapter 2
#
# Name: <Zachary Windus>
# GitHub: <Vizorel>
#
# On my honor, <Zachary Windus>, this programming assignment is my own work
# and I have not provided this code to any other student.
def main():
    print('A car is going 70 miles per hour. Use the following responses to calculate the distance traveled')
    Question = int(input('Please respond with the following responses (6, 10, 15): '))
    Speed = float(70)

    Answer = int(Speed * Question)
    print('The Distance that was Traveled is' , Answer, 'miles')
    main()
