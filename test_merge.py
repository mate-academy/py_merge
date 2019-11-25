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
        l1 = sorted(random.randint(1, 10) for _ in range(random.randint(1, 10)))
        l2 = sorted(random.randint(1, 10) for _ in range(random.randint(1, 10)))
        assert merge.merge(l1, l2) == sorted(l1 + l2)
