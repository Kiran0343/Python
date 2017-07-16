"""
Python script to merge two Python dictionaries.
"""


# creating 2 sample dictionaries
dict1 = {'Name' : 'kiran','City' : 'Dallas'}
dict2 = {'course':'Python','Assignment_no' : 1}
# printing the dict after merging
print "Dictionary before merging : "
print "dict1 : ",dict1
print "dict1 : ",dict2
# merging dict2 into dict1
for key,value in dict2.items():
    dict1[key] = value
# printing the dict after merging
print "Dictionary after merging : ", dict1