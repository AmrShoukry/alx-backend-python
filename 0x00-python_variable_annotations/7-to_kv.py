#!/usr/bin/env python3
""" Complex Module """
from typing import Union, Tuple
import math


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ Sum function """
    return (k, math.pow(v, 2))
