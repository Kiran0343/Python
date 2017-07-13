'''
program to calculate GCD of two numbers.
'''
num1 = input("Enter first number : ")
num2 = input("Enter second number :")
max1 = []
for i in range(2,num1):
    if num1 % i == 0 and num2 % i ==0:
        max1.append(i)
print "GCD of " +str(num1) +" and " + str(num2) +" is : " + str(max(max1))
