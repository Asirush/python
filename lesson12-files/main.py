# create file
def create_file(name: str):
    with open(name + ".txt", 'w') as f:
        f.close()

# task 1 
def task1(input: str, output: str):
    input = input + ".txt"
    arr = []

    with open(input, "r") as f:
        print(f.readlines())
        for i in input:
            if len(i) > 7:
                arr.append(i)

    with open(output + ".txt", "w", encoding='UTF-8') as f:
        for i in arr:
            f.writeline(i)
        

if "__main__" == __name__:
    task1("file1", "file2")