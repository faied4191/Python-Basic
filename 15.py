class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        area = self.length * self.width
        print("Area:", area)

    def perimeter(self):
        perimeter = 2 * (self.length + self.width)
        print("Perimeter:", perimeter)

# Create an instance of Rectangle
ob = Rectangle(5, 3)