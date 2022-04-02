import functools
from datetime import datetime


class RateLimiter:

    __LAST_CALL = 0
    __CYCLE = 0

    def __init__(self, number=10, seconds=1):
        RateLimiter.__CYCLE = seconds / number
        RateLimiter.__LAST_CALL = datetime.now()

    def __call__(self, func):
        @functools.wraps(func)
        def inner(*args, **kwargs):
            while True:
                time_passed = (datetime.now() - RateLimiter.__LAST_CALL).total_seconds()
                if time_passed >= RateLimiter.__CYCLE:
                    RateLimiter.__LAST_CALL = datetime.now()
                    break
            return func(*args, **kwargs)
        return inner


if __name__ == '__main__':

    @RateLimiter(1, 1)
    def print_call(message: str):
        print(message)

    for _ in range(10):
        print_call("Hello world")
