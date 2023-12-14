import sys
from datetime import datetime
import time

original_write = sys.stdout.write


def my_write(string_text):
    curr_time = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]: ")
    original_write(curr_time + string_text + "\r")


if __name__ == "__main__":
    sys.stdout.write = my_write
    print("1, 2, 3")
    sys.stdout.write = original_write
