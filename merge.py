"""Merge module."""
from typing import List


def merge(first_list: List[int], second_list: List[int]) -> List[int]:
    """Merge two lists into one and return it sorted."""
    fst_lst_length = len(first_list)
    snd_lst_length = len(second_list)
    new_list = []

    i, j = 0, 0
    while i < fst_lst_length and j < snd_lst_length:
        if first_list[i] < second_list[j]:
            new_list.append(first_list[i])
            i += 1
        else:
            new_list.append(second_list[j])
            j += 1
    return new_list + first_list[i:] + second_list[j:]
