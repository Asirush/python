import random
from sorts import *

def generate_arr(size: int) -> list:
    array = []
    for i in range(0,size):
        array.append(random.randint(1,10))
    return array
    
def show_before_sort(arr: list, arrsize: int):
    print("Before sorting")
    for i in range(0, arrsize):
        print(arr[i])
    return None

def show_after_sort(arr: list, arrsize: int):
    print("##########################")
    print("After sorting")
    for i in range(0, arrsize):
        print(arr[i])
    print("##########################")
    return None


if "__main__" == __name__:

    ARRSIZE = 5
    
    # Generate arrays
    arr1 = generate_arr(ARRSIZE)
    arr2 = generate_arr(ARRSIZE)
    arr3 = generate_arr(ARRSIZE)
    
    print("shell_sort")
    show_before_sort(arr1, ARRSIZE)
    shell_sort(arr1)
    show_after_sort(arr1, ARRSIZE)

    print("heap_sort")
    show_before_sort(arr2, ARRSIZE)
    heap_sort(arr2)
    show_after_sort(arr2, ARRSIZE)

    print("quick_sort")
    show_before_sort(arr3, ARRSIZE)
    answer = quick_sort(arr3)
    show_after_sort(answer, ARRSIZE)