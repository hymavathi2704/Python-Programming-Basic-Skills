'''
Problem:
Use the variable x as you write this program. x will represent a positive integer. Write a program that determines if x is between 0 and 25 or between 75 and 100. If yes, print the message:_ is between 0 and 25 or 75 and 100, where the blank would be the value of x. The program should do nothing if the value of x does not fit into either range.
Expected Output:
If x is 8, then the output would be: 8 is between 0 and 25 or 75 and 100.
If x is 80, then the output would be: 80 is between 0 and 25 or 75 and 100.
If x is 50, then the output would be blank (your program does not print anything).'''

#Code:

import sys
x = int(sys.argv[1])

########################################################
# Enter your code below
########################################################
if x > 0 and x < 25 or x > 75 and x < 100:
    print(str(x) + " is between 0 and 25 or 75 and 100")