from typing import List

def sort(array: List) -> List: 
    n = len(array)
    for i in range(1, n):
        current = i 
        while current > 0 and array[current] < array[current - 1]:
            array[current], array[current - 1] = array[current - 1], array[current]
            current -= 1
    return array    



if __name__ == "__main__":
    import random
    array = [random.randint(0, 1000) for _ in range(1000)]
    print(sort(array))