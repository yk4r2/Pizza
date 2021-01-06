from typing import Callable
import time
import functools


def log(text_pattern: str) -> Callable:
    """Returns time of the function's processing."""
    def inner(func):
        @functools.wraps(func)
        def wrapper_timer(*args, **kwargs):
            start_time = time.perf_counter()
            value = func(*args, **kwargs)
            end_time = time.perf_counter()
            run_time = end_time - start_time
            print(text_pattern.replace('{}', '{0:.3f}'.format(run_time)))
            return value
        return wrapper_timer
    return inner
