#!/usr/bin/env python3
"""Run multiple asyncio tasks concurrently."""

import asyncio
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Run multiple tasks and return their delays."""
    tasks = []
    delays = []
    for _ in range(n):
        task = task_wait_random(max_delay)
        tasks.append(task)

    for task in asyncio.as_completed(tasks):
        results = await task
        delays.append(results)

    return delays
