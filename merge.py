""" docstring module"""
from typing import List


def merge(list_item1: List[int], list_item2: List[int]) -> List[int]:
    """merge two sorted list"""
    result = []
    i = 0
    j = 0
    while i < len(list_item1) and j < len(list_item2):
        if list_item1[i] < list_item2[j]:
            result.append(list_item1[i])
            i = i + 1
        else:
            result.append(list_item2[j])
            j = j + 1
    for k in list_item2[j:]:
        result.append(k)
    for k in list_item1[i:]:
        result.append(k)
    return result
