class parent:
    employees = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        self.email = name + "@gmail.com"
        parent.employees = parent.employees + 1

    def empcount(self):
        print " emp name : ", self.name
        print " emp salary : ", self.salary
        print " emp email: ", self.email
        print "employee count : ", parent.employees


class child(parent):
    child_employees = 0
    def __init__(self, name, salary, city):
        parent.__init__(self, name, salary)
        self.city = city
        child.child_employees = child.child_employees + 1

    def childcount(self):
        print "child employees count :" , child.employees



emp1 = parent('kiran', 4000)
emp1.empcount()
emp2 = parent('aditya', 2000)
emp2.empcount()
emp3 = child('abhi', 3000, 'hyd')
emp3.childcount()
emp3.empcount()