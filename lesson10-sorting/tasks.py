import random
from sorts import *

TOWERSIZE = 4
MINSIZE = 2
MAXSIZE = 6

def rotate_array(array: list, start: int, end: int):
    array[start:end:-1]
    return None

def oladiy(tower: list) -> list:
    result = list(quick_sort(tower))
    return result
        
def generate_arr(size: int, minsize: int, maxsize: int) -> list:
    array = []
    for i in range(0,size):
        array.append(random.randint(minsize,maxsize))
    return array

def print_tower(arr: list):
    for i in TOWERSIZE:
        print(arr[i])
    return None

if "__main__" == __name__:
    tower = generate_arr(TOWERSIZE, MINSIZE, MAXSIZE)
    print(tower)
    print_tower(oladiy(tower))

