from functools import lru_cache

import pytest

from fibonacci.naive import fibonacci_naive


@lru_cache(maxsize=256)
@pytest.mark.parametrize("n,expected", [(0, 0), (1, 1), (2, 1), (20, 6765)])
def test_naive(n: int, expected: int):
    res = fibonacci_naive(n=n)
    assert res == expected