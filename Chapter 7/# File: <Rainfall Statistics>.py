# File: <Rainfall Statistics>
# Description: <a program that lets the user enter the total rainfall for each of 12 months into a list. The program should calculate and display the total rainfall for the year, the average monthly rainfall, the months with the highest and lowest amounts.>
# Assignment Name and Number: #3 of Chapter 7
#
# Name: <Zachary Windus>
# GitHub: <Vizorel>
#
# On my honor, <Zachary Windus>, this programming assignment is my own work
# and I have not provided this code to any other student.
from statistics import mean 
Months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
Num_Months = 12
rainfall = []
current_month = Months[1]
change = 0
total_rain = 0
Referencelist = []

for i in range(Num_Months):
    current_month = Months[change]
    Referencelist.append(current_month)
    print('what was the total rainfall in', current_month)
    UInput = int(input('total rainfall: '))
    Referencelist.append(UInput)
    rainfall.append(UInput)
    change = change + 1
    total_rain += UInput

Average_rainfall = mean(rainfall)
print(Referencelist)
MaxRain = max(rainfall)
MinRain = min(rainfall)
Maxmonthrange = (((rainfall.index(max(rainfall)))+1)*2)-2
Minmonthrange = (((rainfall.index(min(rainfall)))+1)*2)-2
print()
print()
print()
print('——————————————————————————————————————————————————————')
print('the total rainfall throughout the year was:', total_rain)
print('——————————————————————————————————————————————————————')
print('the average rainfall throughout the year was:', Average_rainfall)
print('——————————————————————————————————————————————————————')
print('the month with the most rainfall was', Referencelist[Maxmonthrange], 'with a rainfall of', MaxRain)
print('——————————————————————————————————————————————————————')
print('the month with the least rainfall was', Referencelist[Minmonthrange], 'with a rainfall of', MinRain)
print()
print()
print()