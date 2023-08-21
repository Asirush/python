import random

def buble_sort(array):
    for i in range(len(array)):
        for j in range(len(array)):
            if array[i] < array[j]:
                temp = array[i]
                array[i] = array[j]
                array[j] = temp
    return array

def desc_buble_sort(array):
    for i in range(len(array)):
        for j in range(len(array)):
            if array[i] > array[j]:
                temp = array[i]
                array[i] = array[j]
                array[j] = temp
    return array

def simple_print(array):
    return array

def triple_sort(array):
    # using self-made functions
    a = buble_sort(array[:len(array)//3])
    b = buble_sort(array[len(array)//3:(len(array)//3)*2])
    c = simple_print(array[(len(array)//3)*2:])

    # using sort functions
    a = sorted(array[:len(array)//3])
    b = sorted(array[len(array)//3:(len(array)//3)*2], reverse=True)
    c = simple_print(array[(len(array)//3)*2:])

if "__main__" == __name__:
    array = []
    for i in range(0,10):
        array.append(random.randint(1,10))
    
    buble_sort(array)
    print(array)

    desc_buble_sort(array)
    print(array)

    triple_sort(array)
    print(array)