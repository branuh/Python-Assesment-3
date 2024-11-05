from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius * self.radius

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

# Create instances of Circle and Square
circle = Circle(5)
square = Square(4)

# Calculate and print the area of each shape
print("Area of the circle:", circle.area())
print("Area of the square:", square.area())