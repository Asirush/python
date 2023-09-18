class Circle:
    def __init__(self, radius: int) -> None:
        self.Radius = radius

class Square:
    def __init__(self, side: int) -> None:
        self.sideSize = side

class CircleInSquare(Circle, Square):
    def __init__(self, radius: int) -> None:
        self.Radius = radius
        self.SquarePerimetr = 8*radius
        self.SquareArea = 4*radius*radius
        self.CircleArea = 3.14*radius*radius
        self.CircleLen = 2*3.14*radius

    def print(self):
        print(self.CircleArea)
        print(self.CircleLen)
        print(self.SquareArea)
        print(self.SquarePerimetr)