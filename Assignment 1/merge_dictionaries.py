'''
Python script to merge two Python dictionaries.
'''

dict1 = {'Name' : 'kiran','City' : 'Dallas'}
dict2 = {'course':'Python','Assignment_no' : 1}
for key,value in dict2.items():
    dict1[key] = value
dict3 = dict1
print dict3