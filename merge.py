"""Make a new sorted list combining two sorted lists"""
from typing import List

def merge(arr1: List[int], arr2: List[int]) -> List[int]:
    """General func"""
    length_arr1 = len(arr1)
    length_arr2 = len(arr2)
    new_arr = []
    i, j = 0, 0
    while i < length_arr1 and j < length_arr2:
        if arr1[i] < arr2[j]:
            new_arr.append(arr1[i])
            i += 1
        else:
            new_arr.append(arr2[j])
            j += 1
    new_arr = new_arr + arr1[i:] + arr2[j:]
    return new_arr
