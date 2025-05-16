import pytest
from triangle import triangle_area

def test_valid_triangle():
    assert round(triangle_area(3, 4, 5), 2) == 6.0

def test_invalid_triangle():
    with pytest.raises(ValueError, match="Неможливі сторони"):
        triangle_area(1, 2, 3)

def test_equilateral_triangle():
    assert round(triangle_area(6, 6, 6), 2) == 15.59

def test_zero_side():
    with pytest.raises(ValueError, match="додатніми числами"):
        triangle_area(0, 5, 5)

def test_negative_side():
    with pytest.raises(ValueError, match="додатніми числами"):
        triangle_area(-3, 4, 5)
