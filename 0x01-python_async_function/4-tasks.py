#!/usr/bin/env python3
""" The basics of async """

from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """ random """
    runs: list = []
    for i in range(n):
        runs.append(await task_wait_random(max_delay))

    return sorted(runs)
