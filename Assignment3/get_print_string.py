"""
python script which has class having two below methods and access
those methods in another class:
"""

class parent():

    def __init__(self):
        print "hello from parent"

    def getString(self):
        self.word = str(raw_input("Enter string : "))

    def printString(self):
        print "string is : ", self.word

class child(parent):
    def __init__(self):
        print "hello from child"

c = child()
c.getString()
c.printString()