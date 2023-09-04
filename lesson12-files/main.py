# create file
def create_file(name: str):
    with open(name + ".txt", 'w') as f:
        f.close()

# task 1 
def task1(input: str, output: str):
    input = input + ".txt"
    arr = []

    with open(input, "r") as f:
        arr = f.readlines()
        for i in arr:
            if len(i) < 7:
                arr.remove(i)

    with open(output + ".txt", "w") as f:
        f.writelines(arr)
        
# task4
def task4(input: str, output: str):
    file_content = []
    result = ""
    valueexists = False
    with open(input, "r") as rf:
        file_content = rf.readlines()[::-1]
    for i in file_content:
        if i.__contains__(","):
            result = i
            valueexists=True
    if(valueexists==False):
        result = file_content[0]
    with open(output, "w") as wf:
        wf.write(result)
    
def task7(arr: list, file: str):
    with open(file, "w") as wf:
        while i in arr:
            wf.write(i)

if "__main__" == __name__:
    arr = [1,2,3]
    #task1("file1", "file2")
    #task4("file1.txt", "file2.txt")
    task7(arr, "file2.txt")