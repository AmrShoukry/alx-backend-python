#!/usr/bin/env python3
""" The basics of async """

from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ random """
    runs: list = []
    for i in range(n):
        runs.append(await wait_random(max_delay))

    return sorted(runs)
