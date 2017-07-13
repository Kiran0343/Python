'''
Python program to multiplies all the items in a list.
'''


#creating a sample list with random numbers
list = [2,3,4,5,6]
value = 1
#iterating through the loop and multiplying all the elements in the list
for i in range(len(list)):
    value = value * list[i]
#printing the final value
print "multiplies of all items in the list is : " , str(value)
