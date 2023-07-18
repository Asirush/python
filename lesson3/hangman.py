import random
import requests
import re


def downloads_russian_words() -> list:
    """
    Загружает файл, содержащий русские слова, с удаленного URL-адреса и
    возвращает содержимое в виде строки.

    Принимает:
        None

    Возвращает:
        str: содержимое файла в виде списка.
    """
    response = requests.get(
        "https://raw.githubusercontent.com/LussRus/Rus_words/master/UTF8/txt/raw/summary.txt"
    )
    text = response.content.decode("utf-8")

    return text


def choice_random_word(word_list: list) -> str:
    """
    Выбирает случайное слово из списка.

    Принимает:
        word_list (list): Список слов.

    Возвращает:
        str: Слово.
    """
    random_index = random.randint(0, len(word_list) - 1)

    return word_list[random_index]


def is_russian_char(guess: str) -> bool:
    """
    Проверяет, является ли буква из русского алфавита.

    Принимает:
        guess (str): Буква или знак '-'.

    Возвращает:
        bool: True, если буква русского алфавита, False в противном случае
    """
    if (
        (re.match("[а-я]", guess) is None)
        and (ord(guess[0]) != 1105)
        and (ord(guess[0]) != 45)
    ):
        return False
    return True

def request_a_letter(letter: chr, word: str) -> bool:
    if str.__contains__(letter):
        return True
    else:
        return False
    
def show_menu(known_word: str, attempts_count: int) -> None:
    if known_word == "":
        print(f"Count of attempts: {attempts_count}")
    else:
        print(f"Count of attempts: {attempts_count}")
        print(known_word)
        
def generate_hidden_word(word: str) -> str:
    result = ""
    c = 0
    while c < len(word):
        result += "_"
        c += 1
    return result

def check_if_letter_in_word(letter: chr, word: str) -> bool:
    if word.__contains__(letter):
        return True
    else:
        return False

def main() -> None:
    word = choice_random_word(downloads_russian_words().split("\n"))
    wrong_attempts = []
    knownWord = generate_hidden_word(word)
    attempt_count = 13 
    while attempt_count > 0:
        show_menu(knownWord, attempt_count)
        print("write a letter: ")
        tmp = input()
        if check_if_letter_in_word(tmp, knownWord):
            print("this letter is already tried!")
        elif check_if_letter_in_word(tmp, word):
            knownWord[word.find(tmp)] = tmp
            attempt_count -= 1
        else:
            wrong_attempts.append(tmp)
            attempt_count -= 1
                    
if __name__=="__main__":
    main()    