import yamath
import pytest


def test_add():
    ans = yamath.add(1.0, 2.0, lambda x: 2 * x)
    sol = 6.0

    assert ans == sol


def test_error():
    with pytest.raises(TypeError):
        yamath.add(1.0, 2.0, None)
