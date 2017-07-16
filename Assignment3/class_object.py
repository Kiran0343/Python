
class parent:
    employees = 0


    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
        self.email = name + "@gmail.com"
        parent.employees = parent.employees + 1


    def empcount(self):
        print " emp name : ",self.name
        print " emp salary : ",self.salary
        print " emp total: ", self.total
        print " emp email: ", self.email
        print "employee count : ",parent.employees




emp1 = parent('kiran',4000)
emp1.empcount()
emp2 = parent('aditya',2000)
emp2.empcount()

