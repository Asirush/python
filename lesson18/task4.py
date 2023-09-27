class Lesson:
    def __init__(self, name: str) -> None:
        self.name = name

    def __str__(self):
        return self.name

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

    def __init__(self, name: str, age: int, id: str, lesson: Lesson) -> None:
        self.name = name
        self.age = age
        self.id = id
        self.lessons.append(lesson)

    def addLesson(self, lesson: Lesson):
        self.lessons.append(lesson)
    
    def info(self):
        result = f'"{self.name}", {self.age}, "{self.id}", {self.lessons}'

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