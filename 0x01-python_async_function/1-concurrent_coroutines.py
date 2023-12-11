#!/usr/bin/env python3
""" The basics of async """

from typing import List
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """ random """
    start = time()
    
    wait_n(n, max_delay)
    
    end = time()

    return end - start
