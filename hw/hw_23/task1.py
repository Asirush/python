def main():
    # Получаем список чисел от пользователя
    nums = input("Введите числа через пробел: ").split()
    nums = list(map(int, nums))

    while True:
        # Показываем пользователю меню
        print("\nМеню:")
        print("1. Добавить новое число в список.")
        print("2. Удалить все вхождения числа из списка.")
        print("3. Показать содержимое списка.")
        print("4. Проверить есть ли значение в списке.")
        print("5. Заменить значение в списке.")
        print("6. Выход.")

        # Получаем выбор пользователя
        choice = int(input("\nВведите ваш выбор: "))

        if choice == 1:
            number = int(input("Введите число для добавления: "))
            if number in nums:
                print(f"Число {number} уже существует в списке.")
            else:
                nums.append(number)

        elif choice == 2:
            number = int(input("Введите число для удаления: "))
            while number in nums:
                nums.remove(number)

        elif choice == 3:
            order = input("Показать список с начала или с конца? (начало/конец): ")
            if order == "начало":
                print(nums)
            elif order == "конец":
                print(nums[::-1])

        elif choice == 4:
            number = int(input("Введите число для проверки: "))
            if number in nums:
                print(f"Число {number} есть в списке.")
            else:
                print(f"Числа {number} нет в списке.")

        elif choice == 5:
            old_num = int(input("Введите число, которое хотите заменить: "))
            new_num = int(input("Введите новое число: "))
            replace_all = input("Заменить все вхождения? (да/нет): ")

            if old_num in nums:
                if replace_all == "да":
                    for i in range(len(nums)):
                        if nums[i] == old_num:
                            nums[i] = new_num
                else:
                    idx = nums.index(old_num)
                    nums[idx] = new_num
            else:
                print(f"Числа {old_num} нет в списке.")

        elif choice == 6:
            print("До свидания!")
            break

        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()
