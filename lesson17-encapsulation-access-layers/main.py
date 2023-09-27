class Calculator:
    def __init__(self) -> None:
        self.__value = 0

    def add(self, num: float):
        return self.__value + num
    
    def substract(self, num: float):
        return self.__value - num
    
    def multiply(self, num: float):
        return self.__value / num
    
    def devide(self, num: float):
        return self.__value / num
    
    def getValue(self) -> float:
        return self.__value
    
PI = 3.14

class Circle:
    def __init__(self) -> None:
        self.__radius = 0
        self.__diametr = 0
        self.__length = 0
        self.__area = 0

    def setRadius(self, value: float):
        self.__radius = value
        self.__diametr = 2*value
        self.__length = 2*PI*value
        self.__area = PI*value*value

    def getRadius(self):
        return self.__radius
    
    def getDiametr(self):
        return self.__diametr
    
    def getLength(self):
        return self.__length
    
    def getarea(self):
        return self.__area
    
class Square:
    def __init__(self) -> None:
        self.__side = 0
        self.__perimetr = 0
        self.__area = 0

if "__main__" == __name__:
    