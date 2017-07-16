
"""
program to find prime number.
"""


# reading a value from the user
number = input("enter a number to check : ")
# checking if the number is less than 2
if number < 2 :
    print "Prime numbers start from number 2"
# checking if the input is 2
if number == 2:
    print str(number) + " is a prime number"
# else checking it by dividing the number from 2 to number-1
else:
    for i in range(2,number):
        if number % i == 0:
            print str(number) + " is not a prime number"
            break
        else:
            print str(number) + " is a prime number"
            break