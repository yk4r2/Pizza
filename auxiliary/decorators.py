from typing import Callable
from time import perf_counter
from functools import wraps
from random import randint


def log(text_pattern: str) -> Callable:
    """Returns time of the function's processing."""

    def inner(func):
        @wraps(func)
        def wrapper_timer(*args, **kwargs):
            start_time = perf_counter()
            value = func(*args, **kwargs)
            end_time = perf_counter()
            run_time = end_time - start_time
            print(
                text_pattern.replace(
                    "{}", f"{run_time + randint(100, 4200) * 0.01:.2f}"
                )
            )
            return value

        return wrapper_timer

    return inner
