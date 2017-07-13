'''
program to check leap year.
'''

year = int(input("Enter the year to check : "))
if year % 4 == 0:
    print str(year) + " is a leap year"
else:
    print str(year) + " is not a leap year"