'''
program to check leap year.
'''


#reading the year number from the user
year = input("Enter the year to check : ")
try:
    #Dividing the year by 4 to check if it is a leap year
    if year % 4 == 0:
        print str(year) + " is a leap year"
    else:
        print str(year) + " is not a leap year"
#throwing an exception if the user enters string as year
except:
    print "year can't be a string"