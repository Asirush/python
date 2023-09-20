class ComplexNumber:
    def __init__(self, real: float, imaginary: float) -> None:
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other):
        result = []
        result.append(self.real + other.real)
        result.append(self.imaginary + other.imaginary)
        return ComplexNumber(result[0], result[1])
    
    def __sub__(self, other):
        result = []
        result.append(self.real - other.real)
        result.append(self.imaginary - other.imaginary)
        return ComplexNumber(result[0], result[1])
    
    def __str__(self) -> str:
        return f"{self.real} + {self.imaginary}i"
    
if __name__ == "__main__":
    c1 = ComplexNumber(1,2)
    c2 = ComplexNumber(3,4)

    result_add = c1 + c2
    result_sub = c1 - c2

    print(result_add)
    print(result_sub)