"""
class parent:
    employees = 0
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
        self.total = name + ' salary : ' , salary
        parent.employees = parent.employees + 1

    def empcount(self):
        print " emp name : ",self.name
        print " emp salary : ",self.salary
        print " emp total: ", self.total
        print "employee count : ",parent.employees

class child(parent):
    def __init__(self,name,salary,city):
        parent.__init__(self,name,salary)
        self.city = city
        print "hi"

emp1 = parent('kiran',4000)
emp1.empcount()
emp2 = parent('aditya',2000)
emp2.empcount()
emp3 = child('abhi',3000,'hyd')
emp3.empcount()
"""
lis = [1,2,3,4,1,2,3,4]
lis
k = set(lis)
ki = list(k)
print ki