"""Sorting of two merged list without using any built-in functions."""

from typing import List


def bubble_sorting(array):
    """Realization of bubble sort"""
    for i in range(len(array) - 1):
        for j in range(len(array) - 1 - i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array


def merge(first_list: List[int], second_list: List[int]) -> List[int]:
    """Sorting of two lists"""
    return bubble_sorting(first_list + second_list)
