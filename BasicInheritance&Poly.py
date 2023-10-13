class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

class Square(Shape):
    def __init__(self, side_length):
        self.side_length = side_length

    def area(self):
        return self.side_length * self.side_length

# Function to calculate and print the area of a shape
def print_area(shape):
    print(f"Area: {shape.area()}")

# Create instances of Circle and Square
circle = Circle(5)
square = Square(4)

# Using polymorphism to calculate and print areas
print_area(circle)  # Area: 78.5
print_area(square)  # Area: 16
