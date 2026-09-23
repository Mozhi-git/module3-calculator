import pytest

from app.operations import Operations

def test_addition():
    assert Operations.addition(5, 3) == 8

def test_subtraction():
    assert Operations.subtraction(10, 4) == 6

def test_multiplication():
    assert Operations.multiplication(4, 3) == 12

def test_division():
    assert Operations.division(10, 2) == 5.0

def test_division_by_zero():
    with pytest.raises(ValueError):
        Operations.division(10, 0)


@pytest.mark.parametrize(
        "a,b,expected",
        [
            (5, 3, 8),
            (10, 4, 14),
            (-2, 5, 3),
        ],
)
def test_addition_parametrized(a, b, expected):
    assert Operations.addition(a, b) == expected