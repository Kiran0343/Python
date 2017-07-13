'''
program to find greater number between three number.
'''

#read three numbers from the user
num1 = int(input("enter first number : "))
num2 = int(input("enter second number : "))
num3 = int(input("enter third number : "))
if num1 > num2 and num1 > num3:
    print str(num1) + " is the greatest number"
elif num2 > num1 and num2 > num3:
    print str(num2) + " is the greatest number"
else:
    print str(num3) + " is the greatest number"