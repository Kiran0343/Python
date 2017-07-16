"""
program to check if a number is positive,negative or zero.
"""

# Reading a number from user
num = int(raw_input("Enter a number : "))
if num == 0:
    print "input value is Zero"
elif num > 0:
    print str(num),"is a positive number"
else:
    print str(num),"is a negative number"