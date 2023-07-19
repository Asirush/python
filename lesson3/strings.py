def qotation_marks() -> None:
    print('string') # одинарные ковычки
    print("string") # двойные ковычки
    print("""string""") # тройные ковычки

    print('book "war and peace"') # экранитрование ковычек
    print("book 'war and peace'") # экранитрование ковычек
    
    return None

def string_max_size() -> int:
    import sys
    return sys.maxsize

def line_breaks() -> None:
    text = "one\ntwo\nthree"
    print(text)
    return None

def concationation() -> None:
    s1 = "Hello" + " world"
    s2 = " world"
    print(s1+s2)
    
    name = "John"
    age = 30
    print("Name: " + name + ", age: " + str(age))
    return None

def string_compare() -> None:
    s1 = "1a"
    s2 = "aa"
    s3 = "Aa"
    s4 = "ba"
    
    print("aa < Aa: " + str("aa" < "Aa"))
    print("aa > ba: " + str("aa" > "ba"))
    print("aa < az: " + str("aa" < "az"))
    print(s1 > s2)
    print(s3 == s4)
    
    s1 = "Intel"
    s2 = "intel"
    print(s1==s2)
    
def remove_string() -> None:
    s = "test"
    print(s, s.replace("test",""))
    
    s = "test"
    s = ""
    print(s)
    return None

def index_string() -> None:
    s = "abcdef"
    print(s[0]) # first letter
    print(s[1]) # second
    print(s[2]) # third
    print(s[-1]) # last one
    return None

def custom_format_string() -> None:
    name = "Alex"
    print("Hello, %s" % name)
    
    print("%d %s, %d %s" % (6, "bananas", 10, "lemons"))
    
    print("{}".format(100))
    
    print("{0}, {1}, {2}".format("one", "two", "three"))
    
    print(f"Hello, {name}!")
    
    a=5
    b=10
    print(f"Five plus ten is {a+b} and not {2*(a+b)}.")

def string_methods() -> None:
    text = ("Wikipedia is a python libruary that makes"
            "its easy to access and parse data from Wikipedia")
    print(text.find("Wikipedia"))
    print(text.rfind("Wikipedia"))
    print(text.count("Wikipedia"))
    
    print(
        text.replace("from Wikipedia", "from https://wikipedia.org/")
    )
    print(text.split(" "))
    
    split_text = text.split(" ")
    print(split_text)
    print("_".join(split_text))
    
    text = "  test  "
    print(text.strip()) # remove spaces
    print(text.lstrip()) # remove spaces at the start
    print(text.rstrip()) # remove space at the end
    
    text = "Python is a product of a Python Software Foundation"
    print(text.lower()) # lowercase
    print(text.upper()) # uppercase
    
    text = "python is a product of a python software foundation"
    print(text.capitalize()) # first letter uppercase
    
    return None

def string_to_types() -> None:
    import json
    from datetime import datetime
    
    print(int("10"))
    print(int("0x12F", base=16))
    
    print("one two three four".split())
    
    print("one, two, three, four".split(","))
    
    print("Bytes".encode("utf-8"))
    
    print(datetime.strptime("Jan 1 2020 1:33PM", "%b %d %Y %I:%M%p"))
    
    print(float("1.5"))
    
    print(
        json.loads('{"Russia": "Moscow", "France": "Paris"}')
    )
    
    print(json.dumps("hello"))
    return None
    
def best_practices() -> None:
    import re
    
    text = "django"
    
    print(list(text))
    print([c for c in "text"])
    
    for c in text:
        print(c)
        
    str = "h3110 23 cat 444.4 rabbit 11 2 dog"
    print([int(s) for s in str.split() if s.isdigit()])
    print(re.findall(r"\d+", str))
    
    print("test"[::-1])
    print("".join(reversed("test")))
    
    print("Some text1"[:-1])
    
    print("  Some text2  ".strip())
    print("  So me t e x t". replace(" ", ""))
    
    return None



def main() -> None:
    qotation_marks()
#    string_max_size()
#    line_breaks()
#    concationation()
#    string_compare()
#    remove_string()
#    index_string()
#    custom_format_string()
#    string_methods()
#    string_to_types()
#    best_practices()
    
if __name__=="__main__":
    main()    