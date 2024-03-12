import pytest

from conftest import track_performance
from fibonacci.dynamic import fibonaci_dynamic_v2


@pytest.mark.performance
@track_performance
def test_performance():
    fibonaci_dynamic_v2(1000)
