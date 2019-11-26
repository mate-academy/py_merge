"""Classic bubble sorting #2"""
from typing import List


def merge(arr1: List[int], arr2: List[int]) -> List[int]:
    """General func"""
    new_arr = arr1 + arr2
    arr_length = len(new_arr) - 1
    for i in range(arr_length):
        for j in range(arr_length - i):
            if new_arr[j] > new_arr[j + 1]:
                new_arr[j], new_arr[j + 1] = new_arr[j + 1], new_arr[j]
    return new_arr
