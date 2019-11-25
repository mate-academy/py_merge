"""module docstring"""
# from typing import List


def merge(first_list, second_list):
    """docstring"""
    unsorted = first_list + second_list
    sorted_list = []
    list_length = len(unsorted)
    i = 0
    while i < list_length:
        sorted_list.append(min(unsorted))
        unsorted.remove(min(unsorted))
        i += 1
    return sorted_list
