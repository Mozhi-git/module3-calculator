import pytest

from app.calculator import Calculator

def test_calculator_addition():
    assert Calculator.calculate(5, 3, "add") == 8

def test_calculator_subtraction():
    assert Calculator.calculate(10, 4, "subtract") == 6

def test_calculator_multiplication():
    assert Calculator.calculate(4, 3, "multiply") == 12

def test_calculator_division():
    assert Calculator.calculate(10, 2, "divide") == 5.0

def test_invalid_operation():
    with pytest.raises(ValueError):
        Calculator.calculate(5, 3, "power")