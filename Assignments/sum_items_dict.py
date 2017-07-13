'''
Python program to sum all the items in a dictionary
'''
dict = {'sachin' : 48,'Dravid': 54,'Sehwag' : 75,'Ganguly' : 49}
sum = 0
for key,value in dict.items():
    sum = sum + value
print "Sum of the items in the dictionary is : ", sum