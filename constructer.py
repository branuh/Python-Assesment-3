class Rectangle:
    def __init__(self, side1=0, side2=0):
        if side2 == 0:
            self.length = side1
            self.width = side1
        else:
            self.length = side1
            self.width = side2

    def area(self):
        return self.length * self.width

# Create a square
square = Rectangle(5)
print("Area of the square:", square.area())

# Create a rectangle
rectangle = Rectangle(4, 6)
print("Area of the rectangle:", rectangle.area())