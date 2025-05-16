import pytest
from calculator import add, subtract, multiply, divide

def test_add():
     assert add(2, 3) == 5
     assert add(-1, 1) == 0
     assert add(0, 0) == 0

def test_subtract():
     assert subtract(5, 3) == 2
     assert subtract(0, 5) == -5
     assert subtract(-1, -1) == 0

def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(-1, 5) == -5
    assert multiply(0, 10) == 0

def test_divide_normal():
    assert divide(6, 2) == 3
    assert divide(7, 2) == 3.5

def test_divide_by_zero():
     with pytest.raises(ValueError):
        divide(6, 0)
