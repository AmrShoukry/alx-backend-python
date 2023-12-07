#!/usr/bin/env python3
""" Complex Module """


def sum_list(input_list: list[float]) -> float:
    """ Sum function """
    total: float = 0
    for number in input_list:
        total += number
    return total
