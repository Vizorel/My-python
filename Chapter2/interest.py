# File: <Interest>
# Description: <gives the interest rate and other results>
# Assignment Name and Number: program exersize chapter 2
#
# Name: <Zachary Windus>
# GitHub: <Vizorel>
#
# On my honor, <Zachary Windus>, this programming assignment is my own work
# and I have not provided this code to any other student.
def main():
    P = int(input('Give me the amount of principal originally deposited into the account: '))
    R = int(input('Give me the annual interest rate paid by the account: '))
    N = int(input('Give me the number of times per year that the interest is compounded: '))
    T = int(input('Give me the number of years the account will be left to earn interest: '))

    A = P*(1+(R/N))**(N*T)
    print('using the given information the amount of money in the account after ' , T, ' years will be $' , A,)
main()
