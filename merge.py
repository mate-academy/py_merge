'''
Module
'''
from typing import List


def merge(first_list: List[int], second_list: List[int]) -> List[int]:
    """

    :param first_list:
    :param second_list:
    :return:
    """
    result_list = []
    len_first_list, len_second_list = len(first_list), len(second_list)
    i, j = 0, 0
    while i < len_first_list and j < len_second_list:
        if first_list[i] <= second_list[j]:
            result_list.append(first_list[i])
            i += 1
        else:
            result_list.append(second_list[j])
            j += 1
    if len_first_list - i > 0:
        result_list.extend(first_list[i:])
    elif len_second_list - j > 0:
        result_list.extend(second_list[j:])
    return result_list
