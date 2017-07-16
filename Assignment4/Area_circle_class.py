"""
Python class named Circle constructed by a radius and two
methods which will compute the area and the perimeter of a circle.
"""

class circle:
    def __init__(self,r):
        self.r = r

    def area(self):
        area = 3.14 * self.r * self.r
        print "Area of circle for given radius : " + str(area)

    def perimeter(self):
        perimeter = 2 * 3.14 * self.r
        print "Perimeter of circle for given radius : " + str(perimeter)


r = circle(int(input("Enter radius : ")))
r.area()
r.perimeter()