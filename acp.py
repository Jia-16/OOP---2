class Circle():
    def __init__(self, r):
        self.radius = r

    def circle_area(self):
        return 3.14*self.radius*self.radius
    
newCircle = Circle(14)
print("Dimension of Circle - Radius : %d"% (newCircle.radius))
print("Area of Circle :", newCircle.circle_area())