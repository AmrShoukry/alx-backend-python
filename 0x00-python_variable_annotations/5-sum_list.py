#!/usr/bin/env python3
""" Complex Module """
from typing import List


def sum_list(input_list: List[float]) -> float:
    """ Sum function """
    total: float = 0
    for number in input_list:
        total += number
    return total
