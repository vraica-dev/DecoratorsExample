"""
idea - create a decorator that logs the time spent by the function it decorates
"""
from time import sleep


class LogTime:
    """
    decorator logging the time spent by an function to run
    """
    def __init__(self, fnc):
        self.fnc = fnc

    def __call__(self, *args, **kwargs):
        import time

        start_t = time.perf_counter()
        output = self.fnc(*args, **kwargs)
        end_t = time.perf_counter()

        print(f'Function  < {self.fnc.__name__} >  took {round(end_t - start_t, 5)} secs.')
        return output


@LogTime
def my_calc(n):
    """
    example random function
    """
    total = 0
    for i in range(n):
        total = total * 0.5 + 11 / 2 + 22 * 0.2
        sleep(0.5)
    return total


print(my_calc(10))  # Function  < mycounter >  took 5.10201 secs.  ; #  total = 19.799999999999997
