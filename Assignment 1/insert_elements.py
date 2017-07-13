'''
program to insert elements in list.
'''


#creating an empty list
list = []
#asking the user, how many elements to be loaded
size = input("Enter size of the list : ")
#appending the list through length of the list using for loop
for i in range(0,size):
    k = input("Enter the index " + str(i) +" element : ")
    list.append(k)
#prinitng the list after appending all the elements
print "List after inserting the lements : " + str(list)