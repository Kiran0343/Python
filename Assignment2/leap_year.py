"""
program to check leap year.
"""


# reading the year number from the user
year = input("Enter the year to check : ")

# Dividing the year by 4 to check if it is a leap year
if year % 4 == 0:
    print str(year) + " is a leap year"
else:
    print str(year) + " is not a leap year"