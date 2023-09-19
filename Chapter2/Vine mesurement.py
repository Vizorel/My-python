# File: <Vine mesurement>
# Description: <makes a mesurement of vine growth>
# Assignment Name and Number: program exersize chapter 2
#
# Name: <Zachary Windus>
# GitHub: <Vizorel>
#
# On my honor, <Zachary Windus>, this programming assignment is my own work
# and I have not provided this code to any other student.
def main():
    R = int(input('Give me the length of the vine: '))
    E = int(input('Give me the amount of space used by the end-post: '))
    S = int(input('Give me the space between each vine: '))

    V = int( (R - 2*E)/S)
    if V >= 2:
        print('Using the given inputs there should be' , V, 'grapevines that will fit in the row')
    else:
        if V <= -1:
            print('error negative number not accepted. Please try again')
        else:
            print('Using the given inputs there should be' , V, 'grapevine that will fit in the row')
main()
