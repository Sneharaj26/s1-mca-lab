class Rectangle:
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def get_length(self):
        return self.__length

    def get_width(self):
        return self.__width

    def area(self):
        return self.__length * self.__width

    def __lt__(self, other):
        return self.area() < other.area()


rectangle1 = Rectangle(5, 10)
rectangle2 = Rectangle(3, 8)

if rectangle1 < rectangle2:
    print("Area of rectangle1 is smaller than the area of rectangle2.")
else:
    print("Area of rectangle1 is not smaller than the area of rectangle2.")
