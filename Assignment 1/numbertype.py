'''
program to check if a number is positive,negative or zero.
'''
#reading number from the user
number = input("Enter a number:")
if number == 0:
    print "input value is a Zero"
elif number > 0 :
    print str(number) + " is a positive number"
else:
    print str(number) + " is a negative number"