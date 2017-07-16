"""
Python script to check if a given key already exists in a Dictionary.
"""

dict = {'name':'kiran','id':1,'city':'hyd'}
key = str(raw_input("Enter key value to check in the dictionary : "))
if key in dict.keys():
    print "key exists"
else:
    print "key doesn't exist"