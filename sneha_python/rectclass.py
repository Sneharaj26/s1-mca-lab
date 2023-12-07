class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2 * (self.length + self.breadth)

    def compare_area(self, other_rectangle):
        area1 = self.area()
        area2 = other_rectangle.area()

        if area1 > area2:
            return "Rectangle 1 has a larger area."
        elif area1 < area2:
            return "Rectangle 2 has a larger area."
        else:
            return "Both rectangles have the same area."


rectangle1 = Rectangle(5, 10)
rectangle2 = Rectangle(8, 6)

print("Area of Rectangle 1:", rectangle1.area())
print("Perimeter of Rectangle 1:", rectangle1.perimeter())

print("Area of Rectangle 2:", rectangle2.area())
print("Perimeter of Rectangle 2:", rectangle2.perimeter())

comparison_result = rectangle1.compare_area(rectangle2)
print(comparison_result)

