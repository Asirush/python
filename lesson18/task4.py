class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def info(self):
        return f'"{self.name}", {self.age}'

class Student(Person):
    def __init__(self, name: str, age: int, id: str) -> None:
        self.name = name
        self.age = age
        self.id = id
    
    def info(self):
        return f'"{self.name}", {self.age}, "{self.id}"'

class Teacher(Person):
    def __init__(self, name: str, age: int, lesson: str) -> None:
        super().__init__(name, age)
        self.lesson = lesson

    def info(self):
        return f'"{self.name}", {self.age}, "{self.lesson}"'
        
if __name__ == "__main__":
    person = Person("Alice", 30)
    student = Student("Bob", 25, "12345")
    teacher = Teacher("Charlie", 35, "Math")

    print(person.info())
    print(student.info())
    print(teacher.info())