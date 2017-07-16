"""
program to show usage of constructor.
"""

class parent:
    #constructor to declare attributes of the class
    def __init__(self,name):
        self.name = str(name)

    def welcome(self):
        print "Welcome to python constructor class" ,self.name

obj = parent('kiran')
obj.welcome()


