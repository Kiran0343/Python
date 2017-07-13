'''
Python program to multiplies all the items in a list.
'''
list = [2,3,4,5,6]
value = 1
for i in range(len(list)):
    value = value * list[i]
print "multiplies of all items in the list is : " , str(value)
