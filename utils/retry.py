import time
import functools

def retry(retries=3, delay=2, exceptions=(AssertionError,)):
    """
    Decorator to retry a function if specified exceptions occur.
    :param retries: Number of attempts
    :param delay: Delay between attempts in seconds
    :param exceptions: Tuple of exception types to catch and retry
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            last_exception = None
            for attempt in range(retries):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    last_exception = e
                    if attempt < retries - 1:
                        time.sleep(delay)
                    else:
                        raise last_exception
        return wrapper
    return decorator