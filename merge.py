"""docstring"""
from typing import List


def merge(first_list: List[int], second_list: List[int]) -> List[int]:
    """merges two sorted lists"""
    merged = []
    # keep track of index in two lists
    i, j = 0, 0
    len_first, len_second = len(first_list), len(second_list)

    while i < len_first and j < len_second:
        if first_list[i] < second_list[j]:
            merged.append(first_list[i])
            i += 1
        else:
            merged.append(second_list[j])
            j += 1
    #  handle lists with different len
    if len_first - i > 0:
        merged.extend(first_list[i:])
    else:
        merged.extend(second_list[j:])
    return merged
