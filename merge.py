"""
docstring
"""


def merge_(list_one, list_two):
    """

    :param list_one:
    :param list_two:
    :return:
    """
    index_left = index_right = 0
    full_merged_list = []
    full_len = len(list_one) + len(list_two)
    while len(full_merged_list) < full_len:
        if list_one[index_left] <= list_two[index_right]:
            full_merged_list.append(list_one[index_left])
            index_left += 1
        else:
            full_merged_list.append(list_two[index_right])
            index_right += 1
        if index_right == len(list_two):
            full_merged_list += list_one[index_left:]
            break
        elif index_left == len(list_one):
            full_merged_list += list_two[index_right:]
            break
    return full_merged_list
