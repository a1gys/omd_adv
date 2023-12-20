from typing import Sequence, TypeVar, Callable, List


T = TypeVar("T")


class Seq:

    def __init__(self, sequence: Sequence[T]):
        self.sequence = sequence

    def map(self, func: Callable) -> "Seq":
        if not callable(func):
            raise TypeError("mapping function must be callable")
        return Seq(func(element) for element in self.sequence)

    def filter(self, func: Callable) -> "Seq":
        if not callable(func):
            raise TypeError("filtering function must be callable")
        return Seq(element for element in self.sequence if func(element))

    def take(self, num: int) -> List[T]:
        if not isinstance(num, int) or num < 0:
            raise ValueError("num must be non-negative integer")
        return list(self.sequence)[:num]


if __name__ == '__main__':
    numbers = [1, 2, 3, 4, 5]
    seq = Seq(numbers)
    res = seq.filter(lambda n: n % 2 == 0).map(lambda n: n + 10).take(3)
    assert res == [12, 14]
