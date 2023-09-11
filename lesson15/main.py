def task1(input: str, filter: str, output: str):
    data = []
    blacklist = []
    with open(input, "r") as rf:
        data = rf.readlines
    with open(filter, "r") as rf:
        blacklist = rf.readlines
    with open(output, "w") as wf:
        for i in data:
            for j in blacklist:
                if i != j:
                    wf.writelines(i)


if "__main__" == __name__:
    task1("input.txt", "filter.txt", "output.txt")