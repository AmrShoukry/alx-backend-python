#!/usr/bin/env python3
""" Complex Module """
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ Sum function """
    total: float = 0
    for number in mxd_lst:
        total += number
    return total
