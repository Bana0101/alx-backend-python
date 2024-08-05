#!/usr/bin/env python3
"""
An asynchronous generator function
"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Asynchronous generator function that yields a random float between 0 and 10
    Returns:
        Generator: Asynchronous generator object that can be used in an
        awaitable context.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
