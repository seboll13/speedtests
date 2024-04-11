from sys import argv
from time import time
from random import random
import numpy as np


# insertion sort of array
def insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i - 1
        nxt_element = arr[i]
        # Compare the current element with next one
        while (arr[j] > nxt_element) and (j >= 0):
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = nxt_element
    return arr


def _wait(n):
    for _ in range(n):
        pass


def main(size):
    # populate random arr of 10000 elements
    arr = np.array([int(1000 * random()) for _ in range(size)])

    # time
    #_wait(size)
    start = time()
    _sorted = insertion_sort(arr)
    end = time()
    print(f'Time taken: {(end - start):.5f} seconds.')


if __name__ == '__main__':
    size = int(argv[1])
    main(size)