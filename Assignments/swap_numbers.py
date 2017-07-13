'''
program to swap(exchange value of two variables) without using third variable.
'''

num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))
print "Values before swap :"
print "num1 : " + str(num1)
print "num2 : " + str(num2)
num1,num2 = num2,num1
print "Values after swap :"
print "num1 : " + str(num1)
print "num2 : " + str(num2)