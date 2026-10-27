#!/usr/bin/env python3
"""Measure the execution time of asynchronous coroutines."""
import asyncio
import time


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Measure the average execution time of wait_n."""
    time_start = time.time()
    asyncio.run(wait_n(n, max_delay))
    time_end = time.time() - time_start
    return time_end / n
