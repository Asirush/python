class StringStack:
    def __init__(self, size):
        self.size = size
        self.stack = []
    
    def push(self, item):
        if len(self.stack) < self.size:
            self.stack.append(item)
        else:
            print("Стек переполнен!")
    
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            print("Стек пуст!")
            return None
    
    def count(self):
        return len(self.stack)
    
    def is_empty(self):
        return len(self.stack) == 0
    
    def is_full(self):
        return len(self.stack) == self.size
    
    def clear(self):
        self.stack = []
    
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            print("Стек пуст!")
            return None

def main():
    size = int(input("Введите размер стека: "))
    stack = StringStack(size)

    while True:
        print("\nМеню:")
        print("1. Поместить строку в стек.")
        print("2. Вытолкнуть строку из стека.")
        print("3. Подсчет количества строк в стеке.")
        print("4. Проверить пустой ли стек.")
        print("5. Проверить полный ли стек.")
        print("6. Очистить стек.")
        print("7. Получить значение верхней строки без выталкивания.")
        print("8. Выход.")
        
        choice = int(input("\nВыберите операцию: "))

        if choice == 1:
            string = input("Введите строку для добавления в стек: ")
            stack.push(string)
        elif choice == 2:
            print(f"Вытолкнутая строка: {stack.pop()}")
        elif choice == 3:
            print(f"Количество строк в стеке: {stack.count()}")
        elif choice == 4:
            if stack.is_empty():
                print("Стек пуст.")
            else:
                print("Стек не пуст.")
        elif choice == 5:
            if stack.is_full():
                print("Стек полон.")
            else:
                print("Стек не полон.")
        elif choice == 6:
            stack.clear()
            print("Стек очищен.")
        elif choice == 7:
            print(f"Верхняя строка стека: {stack.peek()}")
        elif choice == 8:
            print("До свидания!")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()
