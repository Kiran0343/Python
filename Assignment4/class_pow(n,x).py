"""
Python class to implement pow(x, n).
"""

class power:
    def __init__(self,x,n):
        self.n = n
        self.x = x

    def power(self):
        value = self.x ** self.n
        print "power of (" +str(self.x) + "," + str(self.n) + ") : " +str(value)

n = int(raw_input("enter n value : "))
x = int(raw_input("enter x value : "))
obj1 = power(x,n)
obj1.power()