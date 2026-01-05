import time
import tracemalloc
from functools import wraps

def performance(func):
    """
    Decorator that measures execution time and memory usage of functions
    and stores cumulative statistics.
    """
    # decorator attributes (shared across all wrapped calls)
    if not hasattr(performance, "counter"):
        performance.counter = 0
        performance.total_time = 0.0
        performance.total_mem = 0

    @wraps(func)
    def wrapper(*args, **kwargs):
        performance.counter += 1

        tracemalloc.start()
        start_time = time.perf_counter()

        result = func(*args, **kwargs)

        end_time = time.perf_counter()
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        performance.total_time += (end_time - start_time)
        performance.total_mem += peak  # bytes

        return result

    return wrapper
