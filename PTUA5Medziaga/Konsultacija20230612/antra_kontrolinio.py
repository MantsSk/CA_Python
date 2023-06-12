import math


class Shape:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        pass

    def calculate_perimeter(self):
        pass


class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__(length, width)

    def calculate_area(self):
        return self.length * self.width

    def calculate_perimeter(self):
        return 2 * (self.length + self.width)


class RightTriangle(Shape):
    def __init__(self, length, width):
        super().__init__(length, width)

    def calculate_area(self):
        return 0.5 * self.length * self.width

    def calculate_perimeter(self):
        hypotenuse = math.sqrt(self.length**2 + self.width**2)
        return self.length + self.width + hypotenuse


# Testing the classes
rectangle = Rectangle(5, 10)
triangle = RightTriangle(3, 4)

print("Rectangle Information:")
print("Area:", rectangle.calculate_area())
print("Perimeter:", rectangle.calculate_perimeter())
print()

print("Right Triangle Information:")
print("Area:", triangle.calculate_area())
print("Perimeter:", triangle.calculate_perimeter())
