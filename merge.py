"""
New sorted list combining
"""

from typing import List


def merge(lst1: List[int], lst2: List[int]) -> List[int]:
    """Func sorted"""

    len_lst1 = len(lst1)
    len_lst2 = len(lst2)

    indx_lst1 = indx_lst2 = 0

    new_lst = []

    while indx_lst1 < len_lst1 and indx_lst2 < len_lst2:
        if lst1[indx_lst1] <= lst2[indx_lst2]:
            new_lst.append(lst1[indx_lst1])
            indx_lst1 += 1
        else:
            new_lst.append((lst2[indx_lst2]))
            indx_lst2 += 1
    if indx_lst1 < len_lst1:
        new_lst += lst1[indx_lst1:]
    if indx_lst2 < len_lst2:
        new_lst += lst2[indx_lst2:]
    return new_lst
