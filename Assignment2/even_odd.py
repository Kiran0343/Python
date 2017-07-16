"""
program to check if a number is even or odd.
"""

# Reading value from the user
num = int(raw_input("Enter a number :"))
if num % 2 == 0:
    print str(num)," is an even number"
else:
    print str(num)," is an odd number"