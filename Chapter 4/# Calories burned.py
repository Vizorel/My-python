# File: <Calories Burned>
# Description: <it will calculate the amount of calories burned>
# Assignment Name and Number: #2 chapter 4
#
# Name: <Zachary Windus>
# GitHub: <Viorel>
#
# On my honor, <Zachary Windus>, this programming assignment is my own work
# and I have not provided this code to any other student.
print('your running on a treadmill and for every minute you lose 4.2 calories')
time = 0
calories = 4.2
calories_burnt = calories*time
print()
print('it has been ', time, ' minutes you have burned ', calories_burnt, 'calories so far')
time = (time + 5)
print()
if time == 5:
    while time < 30:
        print()
        time = (time + 5)
        calories_burnt = calories*time
        print('it has been ', time, ' minutes you have burned ', calories_burnt, 'calories so far')
        print()
        if time == 30:
            break
