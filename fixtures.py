from datetime import datetime

import pytest


@pytest.fixture
def time_tracker():
    tick = datetime.now()
    yield
    tock = datetime.now()
    diff = tick - tock
    print(f"\nruntime: {diff.total_seconds()}")
