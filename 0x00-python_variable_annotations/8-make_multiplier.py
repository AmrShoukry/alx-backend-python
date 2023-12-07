#!/usr/bin/env python3
""" Callable Module """
from typing import Callable
import math


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ multiplier function """
    def helper(x: float) -> float:
        return x * multiplier
    return helper
