"""
program to find greater number between three number.
"""


# read three numbers from the user
num1 = input("enter first number : ")
num2 = input("enter second number : ")
num3 = input("enter third number : ")
# checking the greatest number using if condition
if num1 > num2 and num1 > num3:
    print str(num1) + " is the greatest number"
elif num2 > num1 and num2 > num3:
    print str(num2) + " is the greatest number"
else:
    print str(num3) + " is the greatest number"