# pylint: disable=redefined-outer-name, invalid-name
# Fixtures; a, b parameters

"""Calculator Test"""


import pytest
from calculator.calculator import Calculator
from calculator.calculation_history import CalculationHistory

@pytest.fixture(autouse=True)
def clear_calc_history():
    """
    Fixture to clear the CalculationHistory before and after each test.
    """
    CalculationHistory.clear_history()
    yield
    CalculationHistory.clear_history()


def test_add(a, b, expected):
    """Test addition."""
    result = Calculator.add(a, b)
    assert result == expected, f"Addition: Expected {expected} but got {result}"


def test_subtract(a, b, expected):
    """Test subtraction."""
    result = Calculator.subtract(a, b)
    assert result == expected, f"Subtraction: Expected {expected} but got {result}"


def test_multiply(a, b, expected):
    """Test multiplication."""
    result = Calculator.multiply(a, b)
    assert result == expected, f"Multiplication: Expected {expected} but got {result}"


def test_divide(a, b, expected):
    """Test division."""
    result = Calculator.divide(a, b)
    assert result == expected, f"Division: Expected {expected} but got {result}"

def test_operation_stored_in_history():
    """
    Test that performing an operation (here addition) stores the calculation in the history.
    """
    Calculator.add(2, 2)
    history = CalculationHistory.get_all_calculations()
    assert len(history) >= 1, "Operation should be stored in the history."
    calc = history[-1]
    assert calc.operation.__name__ == "add", "The stored operation should be 'add'."
