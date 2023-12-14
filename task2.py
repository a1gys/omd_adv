import sys
import time
from typing import Callable


def timed_output(function: Callable):
    original_write = sys.stdout.write

    def my_write(string_text):
        curr_time = time.strftime("[%Y-%m-%d %H:%M:%S]: ")
        original_write(curr_time + string_text + "\r")

    def wrapper(*args, **kwargs):
        sys.stdout.write = my_write
        try:
            function(*args, **kwargs)
        finally:
            sys.stdout.write = original_write
    return wrapper


@timed_output
def print_greeting(name: str):
    print(f"Hello, {name}!")


if __name__ == "__main__":
    print_greeting("Nikita")
