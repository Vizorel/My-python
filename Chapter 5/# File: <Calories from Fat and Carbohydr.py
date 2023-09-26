# File: <Calories from Fat and Carbohydrates>
# Description: <calculates calories from fat and carbs>
# Assignment Name and Number: #6 of Chapter 5
#
# Name: <Zachary Windus>
# GitHub: <Vizorel>
#
# On my honor, <Zachary Windus>, this programming assignment is my own work
# and I have not provided this code to any other student.
fat = int(input('how much fat do you consume daily: '))
Caloriesffat = fat * 9
carb = int(input('how many carbs do you consume daily: '))
Caloriesfcarb = carb * 4
total = Caloriesfcarb+Caloriesffat
print('becuase you consume', fat, 'grams of fat and ', carb, 'grams of carbohydrates')
print()
print('so you gain', Caloriesffat, 'calories from Fat and', Caloriesfcarb, 'calories from Carbs')
print()
print('so in total you gain', total, 'calories daily in total')