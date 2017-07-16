"""
program to find greater number between three number.
"""
# reading 3 numbers from the users
num1 = int(raw_input("Enter first number : "))
num2 = int(raw_input("Enter first number : "))
num3 = int(raw_input("Enter first number : "))

if num1 > num2 and num1 > num3:
    print str(num1) + " is the greatest number of " +str(num1) + " " + str(num2) + " " + str(num3)
if num2 > num1 and num2 > num3:
    print str(num2) + " is the greatest number of " +str(num1) + " " + str(num2) + " " + str(num3)
if num3 > num1 and num3 > num2:
    print str(num3) + " is the greatest number of " +str(num1) + " " + str(num2) + " and " + str(num3)