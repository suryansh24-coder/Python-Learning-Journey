class Circle:
    def __init__(self,radius):
        self.radius = radius
    
    def Area(self):
        return 3.14 * self.radius**2
    
    def perimeter(self):
        return 3.14*2* self.radius
    
c1 = Circle(21)    
print(c1.radius())
print(c1.Area()) 
print(c1.perimeter())   