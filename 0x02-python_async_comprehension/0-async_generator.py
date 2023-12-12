#!/usr/bin/env python3
""" async """

import random
import asyncio
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[None, None]:
    """ Generator """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
