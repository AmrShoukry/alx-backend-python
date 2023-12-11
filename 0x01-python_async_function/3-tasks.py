#!/usr/bin/env python3
""" The basics of async """

import asyncio
from typing import Coroutine

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> Coroutine[None, None, float]:
    """ random """

    task = asyncio.create_task(wait_random(max_delay))
    return task
