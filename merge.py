"""
docstring
"""
from typing import List


def merge(list_one: List[int], list_two: List[int]) -> List[int]:
    """

    :param list_one:
    :param list_two:
    :return:
    """
    merged_list = list_one + list_two
    for i in range((len(merged_list))):
        for j in range(1, len(merged_list) - i):
            if merged_list[j - 1] > merged_list[j]:
                merged_list[j - 1], merged_list[j] = merged_list[j], merged_list[j - 1]
    return merged_list
