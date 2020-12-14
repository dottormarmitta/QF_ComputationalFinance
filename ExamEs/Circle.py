# #
# I build the class:
# #

class Circle:

    # Constructur:
    def __init__(self, xc, yc, radius):
        self.radius = radius
        self.xc = xc
        self.yc = yc
        self.pi = 3.14159265358979323846264338327950288
    
    # Get the perimeter:
    def getPerimeter(self):
        return 2*self.pi*self.radius

    # Get area:
    def getArea(self):
        return self.pi*self.radius*self.radius
    
    # Move to:
    def moveTo(self, newX, newY):
        self.xc = newX
        self.yc = newY
    
    # For completeness, print cordinates values:
    def printCoordinates(self):
        print("x = " + str(self.xc) + " and y = " + str(self.yc))
    

# #
# Some testing:
# #
myFirstCircle = Circle(3,-2,4)
print("Area of first circle is: " + str(myFirstCircle.getArea()))
print("Perimeter of first circle is: " + str(myFirstCircle.getPerimeter()))
myFirstCircle.printCoordinates()
myFirstCircle.moveTo(3.29, 98.212)
myFirstCircle.printCoordinates()