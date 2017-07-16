"""
program to swap(exchange value of two variables) without using third variable.
"""


# reading two numbers from the user
num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))
# printing values before swap
print "Values before swap :"
print "num1 : " + str(num1)
print "num2 : " + str(num2)
# swapping the values
num1,num2 = num2,num1
# printing values after swap
print "Values after swap :"
print "num1 : " + str(num1)
print "num2 : " + str(num2)