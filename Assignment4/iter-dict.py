"""
Python program to iterate over dictionaries using for loops.
"""

dict = {'name':'kiran','id':1,'city':'hyd'}
for key,value in dict.iteritems():
    print "key :" + str(key) + "\t\t" + "value :" +str(value)