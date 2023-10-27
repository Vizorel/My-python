# File: <Paint Job Estimator>
# Description: < display the following data: The number of gallons of paint required, The hours of labor required, The cost of the paint, The labor charges, The total cost of the paint job>
# Assignment Name and Number: #8 of Chapter 5
#
# Name: <Zachary Windus>
# GitHub: <Vizorel>
#
# On my honor, <Zachary Windus>, this programming assignment is my own work
# and I have not provided this code to any other student.
def calculate_paint_gallons(square_feet):
    return square_feet / 112


def calculate_labor_hours(square_feet):
    return (square_feet / 112) * 8


def calculate_paint_cost(gallons, price_per_gallon):
    return gallons * price_per_gallon


def calculate_labor_charges(hours, labor_rate):
    return hours * labor_rate


def calculate_total_cost(paint_cost, labor_charges):
    return paint_cost + labor_charges


def main():
    square_feet = float(input("Enter the square feet of wall space to be painted: "))
    price_per_gallon = float(input("Enter the price of the paint per gallon: $"))
    gallons_required = calculate_paint_gallons(square_feet)
    labor_hours_required = calculate_labor_hours(square_feet)
    paint_cost = calculate_paint_cost(gallons_required, price_per_gallon)
    labor_charges = calculate_labor_charges(labor_hours_required, 35.00)
    total_cost = calculate_total_cost(paint_cost, labor_charges)
    print("Number of gallons of paint required:", gallons_required)
    print("Hours of labor required:", labor_hours_required)
    print("Cost of the paint: $", paint_cost)
    print("Labor charges: $", labor_charges)
    print("Total cost of the paint job: $", total_cost)

main()
