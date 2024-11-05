import pytest
from server import add, subtract, multiply, divide


def test_add():
    assert add(1, 2) == {"result": 3}
    assert add(3, 4) == {"result": 7}

def test_subtract():
    assert subtract(1, 2) == {"result": -1}
    assert subtract(3, 4) == {"result": -1}

def test_multiply():
    assert multiply(1, 2) == {"result": 2}
    assert multiply(3, 4) == {"result": 12}

def test_approx_multiply():
    assert multiply(0.11231092, 0.212409124)["result"] == pytest.approx(0.02, abs=4e-3)

def test_divide():
    assert divide(1, 2) == {"result": 0.5}
    assert divide(3, 4) == {"result": 0.75}

@pytest.mark.xfail(raises=ZeroDivisionError)
def test_divide_by_zero():
    divide(1, 0)