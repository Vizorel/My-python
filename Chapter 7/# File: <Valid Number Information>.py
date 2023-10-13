# File: <Valid Number Information>
# Description: < a program that uses a loop to build a list named valid_numbers that contains only the numbers between 0 and 100 from the numbers list below>
# Assignment Name and Number: #1 of Chapter 7
#
# Name: <Zachary Windus>
# GitHub: <Vizorel>
#
# On my honor, <Zachary Windus>, this programming assignment is my own work
# and I have not provided this code to any other student.
numbers = [74, 19, 105, 20, -2, 67, 77, 124, -45, 38]
valid_numbers = []
total = 0
count = 0

for num in numbers:
    if 0 <= num <= 100:
        valid_numbers.append(num)
        total += num
        count += 1
if count > 0:
    average = total / count
else:
    0

print('original numbers:', numbers)
print('Valid Numbers:', valid_numbers)
print('Total:', total)
print('Average:', average)
