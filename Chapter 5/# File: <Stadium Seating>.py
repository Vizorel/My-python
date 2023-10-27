# File: <Stadium Seating>
# Description: <a program that asks how many tickets for each class of seats were sold, then displays the amount of income generated from ticket sales>
# Assignment Name and Number: #7 of Chapter 5
#
# Name: <Zachary Windus>
# GitHub: <Vizorel>
#
# On my honor, <Zachary Windus>, this programming assignment is my own work
# and I have not provided this code to any other student.
def calculate_income(class_a_tickets, class_b_tickets, class_c_tickets):
    class_a_price = 20
    class_b_price = 15
    class_c_price = 10
    income_class_a = class_a_tickets * class_a_price
    income_class_b = class_b_tickets * class_b_price
    income_class_c = class_c_tickets * class_c_price
    total_income = income_class_a + income_class_b + income_class_c
    return total_income

def main():
    class_a_tickets = int(input("Enter the number of Class A tickets sold: "))
    class_b_tickets = int(input("Enter the number of Class B tickets sold: "))
    class_c_tickets = int(input("Enter the number of Class C tickets sold: "))
    total_income = calculate_income(class_a_tickets, class_b_tickets, class_c_tickets)
    print("Total income generated from ticket sales: $", total_income)

main()
