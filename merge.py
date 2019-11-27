"""Make a new sorted list combining two sorted lists"""
from typing import List


def merge(arr1: List[int], arr2: List[int]) -> List[int]:
    """General func"""
    new_arr = arr1 + arr2
    return quick_sort(new_arr)


def quick_sort(arr):
    """Quick sorting function"""
    if len(arr) < 2:
        return arr
    support = arr[0]
    less = [i for i in arr[1:] if i <= support]
    greater = [i for i in arr[1:] if i > support]
    return quick_sort(less) + [support] + quick_sort(greater)
