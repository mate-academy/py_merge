"""
module combine two sorted lists
"""
from typing import List


def merge(frst_lst: List[int], sec_lst: List[int]) -> List[int]:
    """
    Merge two sorted lists.
    :param frst_lst: List[int]
    :param sec_lst: List[int]
    :return: List[int]
    """
    i, j = 0, 0
    result_lst = []
    frst_lst_size, sec_lst_size = len(frst_lst), len(sec_lst)

    while i < frst_lst_size and j < sec_lst_size:
        if frst_lst[i] < sec_lst[j]:
            result_lst.append(frst_lst[i])
            i += 1
        else:
            result_lst.append(sec_lst[j])
            j += 1
    return result_lst + frst_lst[i:] + sec_lst[j:]
