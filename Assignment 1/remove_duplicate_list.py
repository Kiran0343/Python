'''
Python program to remove duplicates from a list.
'''


#creating a list with some duplicate values
list = [2,3,4,5,6,7,3,5,7]
#creating an empty list to append only unique numbers
list2 = []
#iterating through the loop
for i in list:
    if i not in list2:
        list2.append(i)
print list2
