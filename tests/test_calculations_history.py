# pylint: disable=redefined-outer-name, invalid-name
# Fixtures; a, b parameters
# pylint: disable=use-implicit-booleaness-not-comparison
# For better readability of tests
"""This module contains tests for the CalculationHistory class defined in
calculator.calculation_history. It verifies that calculations are properly
added, filtered by operation name, and that the history can be cleared."""

import pytest
from calculator.calculation import Calculation
from calculator.calculation_history import CalculationHistory

def mock_add(a, b):  # pragma: no cover
    """Mock add function."""
    return a + b

def mock_subtract(a, b):  # pragma: no cover
    """Mock subtract function."""
    return a - b

@pytest.fixture(autouse=True)
def clear_history_before_test():
    """
    Fixture that clears the CalculationHistory before each test.
    Since CalculationHistory stores its state in a class variable,
    we need to clear it to ensure tests remain independent.
    """
    CalculationHistory.clear_history()
    yield
    CalculationHistory.clear_history()

def test_add_and_get_all_calculations():
    """
    Test that calculations are correctly added to the history and can be retrieved.
    """
    calc1 = Calculation(mock_add, 2, 3)
    calc2 = Calculation(mock_subtract, 5, 3)
    CalculationHistory.add_calculation(calc1)
    CalculationHistory.add_calculation(calc2)

    all_calcs = CalculationHistory.get_all_calculations()
    assert all_calcs == [calc1, calc2], "The retrieved calculations do not match the added ones."

def test_filter_by_operation_name():
    """
    Test that filtering calculations by operation name returns the correct calculations.
    """
    calc1 = Calculation(mock_add, 1, 1)
    calc2 = Calculation(mock_add, 2, 3)
    calc3 = Calculation(mock_subtract, 5, 3)

    CalculationHistory.add_calculation(calc1)
    CalculationHistory.add_calculation(calc2)
    CalculationHistory.add_calculation(calc3)

    filtered_add = CalculationHistory.filter_by_operation_name("mock_add")
    filtered_subtract = CalculationHistory.filter_by_operation_name("mock_subtract")

    assert filtered_add == [calc1, calc2], (
        "Filtering by 'mock_add' did not return the expected calculations."
    )
    assert filtered_subtract == [calc3], (
        "Filtering by 'mock_subtract' did not return the expected calculation."
    )

def test_clear_history():
    """
    Test that clearing the history removes all stored calculations.
    """
    calc1 = Calculation(mock_add, 10, 20)
    calc2 = Calculation(mock_subtract, 50, 20)

    CalculationHistory.add_calculation(calc1)
    CalculationHistory.add_calculation(calc2)

    assert CalculationHistory.get_all_calculations() == [calc1, calc2], (
        "History should contain the added calculations."
    )

    CalculationHistory.clear_history()
    assert CalculationHistory.get_all_calculations() == [], "History was not cleared properly."

def test_empty_get_all_calculations():
    """
    Test that retrieving all calculations from an empty history returns an empty list.
    """
    all_calcs = CalculationHistory.get_all_calculations()
    assert all_calcs == [], (
        "Expected an empty list when retrieving calculations from an empty history."
    )

def test_filter_empty_history():
    """
    Test that filtering an empty history by operation name returns an empty list.
    """
    filtered_calcs = CalculationHistory.filter_by_operation_name("dummy_add")
    assert filtered_calcs == [], (
        "Expected an empty list when filtering an empty history."
    )
