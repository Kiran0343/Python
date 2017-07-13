'''
Python program to remove duplicates from a list.
'''
list = [2,3,4,5,6,7,3,5,7]
list2 = []
for i in list:
    if i not in list2:
        list2.append(i)
print list2