"""Tests for the Calculation class."""
from decimal import Decimal

# pylint: disable=redefined-outer-name, invalid-name
# Fixtures; a, b parameters

import pytest
from calculator.calculation import Calculation
from calculator.operations import divide


def test_calculation(a, b, operation, expected):
    """Test that Calculation performs the correct operation."""
    calc = Calculation(operation, a, b)
    result = calc.perform_operation()
    assert result == expected, f"Expected {expected}, got {result}"


def test_division_by_zero():
    """Test that division by zero raises ZeroDivisionError."""
    calc = Calculation(divide, Decimal("10.0"), Decimal("0.0"))
    with pytest.raises(ZeroDivisionError):
        calc.perform_operation()
