"""
docsrting
"""
import random

import pytest

import merge


@pytest.mark.parametrize('x', range(10))
def test_merge(x):
    """

    :param x:
    :return:
    """
    for i in range(10):
        list_one = sorted(random.randint(1, 10) for _ in range(random.randint(1, 10)))
        list_two = sorted(random.randint(1, 10) for _ in range(random.randint(1, 10)))
        assert merge.merge_(list_one, list_two) == sorted(list_one + list_two)
