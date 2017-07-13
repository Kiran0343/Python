'''
program to check if a number is even or odd.
'''
#read value from the user
number = input("enter a number to check : ")
#checking if the number is odd or even
try:
    if number%2 == 0:
        print str(number) + " is a an even number"
    else:
        print str(number) + " is a an odd number"
#Throwing an exception if the user enters string
except:
    print "number can't be a string"
