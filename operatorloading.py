class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

# Create two Vector objects
v1 = Vector(2, 3)
v2 = Vector(1, 4)

# Add the vectors using the overloaded + operator
result = v1 + v2

print(result)  # Output: Vector(3, 7)