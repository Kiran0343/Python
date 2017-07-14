"""
program to find the factorial of a number.
"""


# reading a number to find factorial
number = input("Enter a number to find its factorial : ")
# initializing a fact variable to value 1
fact = 1

# checking if the input value is zero
if number == 0 :
    print "factorial of number " + str(number) + " is 0"
# calculating factorial bu multiplying starting from 2 through to the input number
for i in range(2,number+1):
    fact = fact * i
# printing the factorial of the number
print "factorial of number " + str(number) + " is " + str(fact)


