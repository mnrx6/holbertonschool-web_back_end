#!/usr/bin/env python3
"""Create an asyncio task for a random delay."""
import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Schedule a random delay coroutine and return its task."""
    task_wait = asyncio.create_task(wait_random(max_delay))
    return task_wait
