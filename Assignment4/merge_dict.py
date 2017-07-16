"""
Python script to merge two Python dictionaries.
"""

dict1 = {'name':'kiran','id':1,'city':'hyd'}
dict2 = {'age':20,'subject':'python'}
for key,value in dict2.iteritems():
    dict1[key] = value
print dict1