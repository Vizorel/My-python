# File: <Calories from Fat and Carbohydrates>
# Description: <calculates calories from fat and carbs>
# Assignment Name and Number: #6 of Chapter 5
#
# Name: <Zachary Windus>
# GitHub: <Vizorel>
#
# On my honor, <Zachary Windus>, this programming assignment is my own work
# and I have not provided this code to any other student.
def calculate_calories_from_fat(fat):
    Caloriesffat = fat * 9
    return Caloriesffat

def calculate_calories_from_carbs(carb):
    Caloriesfcarb = carb * 4
    return Caloriesfcarb


def main():
    fat = int(input('How much fat do you consume daily: '))
    carb = int(input('How many carbs do you consume daily: '))
    
    Caloriesffat = calculate_calories_from_fat(fat)
    Caloriesfcarb = calculate_calories_from_carbs(carb)
    
    print('Because you consume', fat, 'grams of fat and', carb, 'grams of carbohydrates')
    print('You gain', Caloriesffat, 'calories from Fat and', Caloriesfcarb, 'calories from Carbs')

main()