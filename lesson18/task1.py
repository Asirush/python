class Shape:
    def area():
        return "Method is not created"
    
class Rectangle(Shape):
    def __init__(self, a: float, b: float) -> None:
        self.size_a = a
        self.size_b = b

    def area(self):
        return self.size_a * self.size_b
    
class Circle(Shape):
    radius = 0

    def __init__(self, r: float) -> None:
        self.radius = r

    def area(self):
        return 3.14 * self.radius * self.radius
    
if __name__ == "__main__":
    shape = Shape()
    print(shape.area())

    rectangle = Rectangle(4,5)
    print(rectangle.area())

    circle = Circle(3)
    print(circle.area())