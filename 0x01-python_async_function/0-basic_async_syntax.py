#!/usr/bin/env python3
""" The basics of async """

import random


async def wait_random(max_delay=10):
    """ random """
    return random.uniform(0, max_delay)
