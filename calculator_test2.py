import pytest
from calculator import add, subtract, multiply, divide

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(0, 5) == -5

def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(-1, 4) == -4

def test_divide():
    assert divide(6, 2) == 3
    assert divide(7, 2) == 3.5


def test_divide_by_zero():
    with pytest.raises(ValueError, match="ділення на нуль"):
        divide(5, 0)

def test_large_numbers():
    assert add(1_000_000_000, 2_000_000_000) == 3_000_000_000

def test_calculate_whole_logic():
    assert add(10, 5) == 15
    assert subtract(20, 10) == 10
    assert multiply(4, 3) == 12
    assert divide(12, 4) == 3

@pytest.mark.parametrize("a,b", [("a", 2), (3, "b"), ("x", "y")])
def test_invalid_input_type(a, b):
    with pytest.raises(TypeError):
        add(a, b)
