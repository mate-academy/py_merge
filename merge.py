"""Two list sort module"""
from typing import List


def merge(array1: List[int], array2: List[int]) -> List[int]:
    """
    Two list sort function
    :param array1: first list for sort
    :param array2: second list for sort
    :return: array1 + array2 sorted list
    """
    array1index = 0
    array2index = 0
    result = []

    while True:
        if array1index >= len(array1):
            result.extend(array2[array2index:])
            break
        if array2index >= len(array2):
            result.extend(array1[array1index:])
            break
        if array1[array1index] < array2[array2index]:
            result.append(array1[array1index])
            array1index += 1
        else:
            result.append(array2[array2index])
            array2index += 1
    return result
