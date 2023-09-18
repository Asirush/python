class Employeer:
    def __init__(self, id: int, name: str, position: str) -> None:
        self.id = id
        self.name = name
        self.position = position
    
    def __str__(self) -> str:
        return self.name

    def print(self):
        print(self.id + ": " + self.name + " - " + self.position)

class Manager(Employeer):
    def __init__(self, id: int, name: str, position: str) -> None:
        super().__init__(id, name, position)
    
    def __str__(self) -> str:
        return super().__str__()

    def print(self):
        return super().print()

class Worker(Employeer):
    def __init__(self, id: int, name: str, position: str) -> None:
        super().__init__(id, name, position)
    
    def print(self):
        return super().print()
    
class President(Employeer):
    def __init__(self, id: int, name: str, position: str) -> None:
        super().__init__(id, name, position)
    
    def print(self):
        return super().print()