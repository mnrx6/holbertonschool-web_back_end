#!/usr/bin/env python3
"""Run multiple asynchronous delays."""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Run random delays concurrently and return their results."""
    tasks = []
    delays = []
    for _ in range(n):
        task = asyncio.create_task(wait_random(max_delay))
        tasks.append(task)

    for task in asyncio.as_completed(tasks):
        results = await task
        delays.append(results)

    return delays
