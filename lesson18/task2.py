class Vector:
    def __init__(self, x: float, y: float, z: float) -> None:
        self.x=x
        self.y=y
        self.z=z

    def __add__(self, other):
        return self.x + other.x, self.y + other.y, self.z + other.z
    
    def __sub__(self, other):
        return self.x - other.x, self.y - other.y, self.z - other.z
    
if __name__ == "__main__":
    v1 = Vector(1,2,3)
    v2 = Vector(4,5,6)

    result_add = v1 + v2
    result_sub = v1 - v2

    print(result_add)
    print(result_sub)