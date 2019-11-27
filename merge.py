"""Sorting of two merged list without using any built-in functions."""

from typing import List


def merge(first_list: List[int], second_list: List[int]) -> List[int]:
    """Sorting of two lists"""
    sorted_list = []
    first_arr_copy, second_arr_copy = first_list.copy(), second_list.copy()
    while first_arr_copy and second_arr_copy:
        if first_arr_copy[0] <= second_arr_copy[0]:
            item = first_arr_copy.pop(0)
            sorted_list.append(item)
        else:
            item = second_arr_copy.pop(0)
            sorted_list.append(item)
    sorted_list.extend(first_arr_copy if first_arr_copy else second_arr_copy)
    return sorted_list
