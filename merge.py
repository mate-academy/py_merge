"""
New sorted list combining
"""

from typing import List


def merge(lst1: List[int], lst2: List[int]) -> List[int]:
    """Func sorted"""
    new_lst = lst1 + lst2
    len_lst = len(new_lst)
    for i in range(len_lst):
        lowest_index = i
        for j in range(i+1, len(new_lst)):
            if new_lst[j] < new_lst[lowest_index]:
                lowest_index = j
        new_lst[i], new_lst[lowest_index] = new_lst[lowest_index], new_lst[i]
    return new_lst
