'''
program to check if a number is even or odd.
'''
#read value from the user
number = int(input("enter a number to check : "))
#checking if the number is odd or even
if number%2 == 0:
    print str(number) + " is a even number"
else:
    print str(number) + "is a odd number"
