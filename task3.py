import sys
from typing import Callable


class file_output_redirecter:

    def __init__(self, path: str):
        self.path = path
        self.original_stdout = sys.stdout
        self.file = None

    def __enter__(self):
        self.file = open(self.path, "w")
        sys.stdout = self.file
        return self

    def __exit__(self, ex_type, ex_value, traceback):
        if self.file:
            self.file.close()
        sys.stdout = self.original_stdout


def redirect_output(filepath: str):
    def decorator(func: Callable):
        def wrapper(*args, **kwargs):
            with file_output_redirecter(path=filepath):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator


@redirect_output("./function_output.txt")
def calculate():
    for power in range(1, 5):
        for num in range(1, 20):
            print(num ** power, end=" ")
        print()


if __name__ == "__main__":
    calculate()
