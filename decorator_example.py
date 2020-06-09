# Good Decorator Example
from time import time

# Using the wrapper to take what-ever arguments we want with *args and **kwargs
# Start the time before the action
# Do action
# Take time after action
# Print the difference between the times

# This can be used to test the run speed of any function


def performance_checker(fn):
    def wrapper(*args, **kwargs):
        start = time()
        result = fn(*args, **kwargs)
        end = time()
        print(f"Took {end - start} seconds")
        return result

    return wrapper


@performance_checker
def long_time():
    for i in range(100000000):
        i * 5


long_time()
