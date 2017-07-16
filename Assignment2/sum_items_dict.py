"""
Python program to sum all the items in a dictionary
"""


# creating a dictionary to sum the values
dict = {'sachin' : 48,'Dravid': 54,'Sehwag' : 75,'Ganguly' : 49}
# initializing sum to 0
sum = 0
# loop through the list and add all the values to sum
for key,value in dict.items():
    sum = sum + value
# print sum value
print "Sum of the items in the dictionary is : ", sum