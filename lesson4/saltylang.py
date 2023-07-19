letters = "аяуюоеёэиы"
EXCEPTIONS = list(letters + letters.upper())
CHANGE_CHAR = "c"

def is_letter_val(letter) -> bool:
    if letter in EXCEPTIONS:
        return True
    else:
        return False
    
def salt_lang(lines) -> str:
    result = ""
    list_lines = list(lines.split(" "))
    
    for word in list_lines:
        for value in word:
            if(is_letter_val(value)):
                result += value + CHANGE_CHAR + value
            else:
                result += value
            result += ""
        return result

def salt_easy(sentence: str) -> str:
    for vowel in EXCEPTIONS:
        sentence = sentence.replace(vowel, vowel + CHANGE_CHAR + vowel.lower())
    return sentence

def main() -> None:
    while True:
        print("Write a word: ")
        word = str(input())
        print(salt_lang(word))
        print(salt_easy(word))
    
if __name__=="__main__":
    main()   