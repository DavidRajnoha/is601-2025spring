"""Tests for the Calculation class."""
import pytest
from calculator.calculation import Calculation
from calculator.operations import add, multiply, divide, subtract

def test_addition():
    """Test that addition returns the correct sum."""
    calc = Calculation(add, 3.0, 4.0)
    result = calc.perform_operation()
    assert result == 7.0, f"Expected 7.0, got {result}"

def test_multiplication():
    """Test that multiplication returns the correct product."""
    calc = Calculation(multiply, 3.0, 4.0)
    result = calc.perform_operation()
    assert result == 12.0, f"Expected 12.0, got {result}"

def test_subtraction():
    """Test that subtraction returns the correct difference."""
    calc = Calculation(subtract, 3.0, 4.0)
    result = calc.perform_operation()
    assert result == -1.0, f"Expected -1.0, got {result}"

def test_division():
    """Test that division returns the correct quotient."""
    calc = Calculation(divide, 10.0, 2.0)
    result = calc.perform_operation()
    assert result == 5.0, f"Expected 5.0, got {result}"

def test_division_by_zero():
    """Test that division by zero raises ZeroDivisionError."""
    calc = Calculation(divide, 10.0, 0.0)
    with pytest.raises(ZeroDivisionError):
        calc.perform_operation()
