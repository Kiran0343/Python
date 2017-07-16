"""
Python program to multiplies all the items in a list.
"""
from functools import reduce
value = reduce(lambda i,j:i*j,[2,5,7,8])
print value