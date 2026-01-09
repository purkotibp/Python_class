

# # #------- task 1  on polymorphysim 
# # create  a class called "shape" with a method 
# #called "area" that returns the area of the shape 
# ------- task 1 on polymorphism
# create a class called "Shape" with a method called "area"

class Shape:
    def area(self):
        pass 

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        self.pi = 3.14

    def area(self):
        return self.pi * self.radius * self.radius
    
class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length * self.length

class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

circle= Circle(7)
square= Square(10)
def area_of_shape(shape):
    return shape.area()

rectangle = Rectangle(10, 20)

print(area_of_shape(circle))
print(area_of_shape(square))
print(area_of_shape(rectangle))

