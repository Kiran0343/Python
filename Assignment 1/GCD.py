'''
program to calculate GCD of two numbers.
'''


#taking the numbers as input from the user
num1 = input("Enter first number : ")
num2 = input("Enter second number :")
#using a list to store all the divisors
max1 = []
for i in range(2,num1):
    if num1 % i == 0 and num2 % i ==0:
        max1.append(i)
#printing the maximum value value from the divisor list
print "GCD of " +str(num1) +" and " + str(num2) +" is : " + str(max(max1))
