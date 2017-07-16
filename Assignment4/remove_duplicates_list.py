"""
Python program to remove duplicates from a list.
"""
# declaring a sample list with repeated values
list1 = [1,2,3,4,5,1,2,3,4,5]
# removing duplicates by converting it into a set
list1 = set(list1)
# converting back to list after removing duplicates
list1 = list(list1)
print list1