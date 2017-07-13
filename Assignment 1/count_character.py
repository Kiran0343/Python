'''
program to count the occurence of given character in list.
'''
#creating a list to store elements
list = ['kiran','reddy','kancharla']
#creating empty string
kiran = ''
#using for loop to concatinate all the elements of the list into the string kiran
for i in list:
    kiran = kiran + i
#using count() method to calculate count of character in the string
print(kiran.count('an'))
