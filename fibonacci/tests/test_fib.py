from typing import Callable

import pytest

from fibonacci.naive import fibonacci_naive
from fixtures import time_tracker


@pytest.mark.parametrize("n,expected", [(0, 0), (1, 1), (2, 1), (20, 6765)])
@pytest.mark.parametrize("fib_func", [fibonacci_naive])
def test_naive(
    time_tracker,
    fib_func: Callable[[int], int],
    n: int,
    expected: int,
):
    res = fib_func(n)
    assert res == expected
