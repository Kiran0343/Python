'''
program to insert elements in list.
'''

list = []
size = input("Enter size of the list : ")
for i in range(0,size):
    k = input("Enter the index " + str(i) +" element : ")
    list.append(k)
print "List after inserting the lements : " + str(list)