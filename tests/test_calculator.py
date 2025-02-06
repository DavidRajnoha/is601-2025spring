"""Test Calculator with an Injected Mock CalculationHistory"""

from calculator.calculator import Calculator
from calculator.calculation import Calculation


class MockCalculationHistory:
    """
    A simple mock for CalculationHistory that records calculations.
    """
    # pylint: disable=missing-function-docstring
    def __init__(self):
        self.calculations = []

    def add_calculation(self, calculation: Calculation):
        self.calculations.append(calculation)

    def get_all_calculations(self):
        return self.calculations


def test_calculator_with_injected_mock_history():
    """
    Test that Calculator uses the injected mock CalculationHistory.

    This test replaces the Calculator's history with a mock instance,
    performs an addition, and verifies that the history received the calculation.
    """
    # pylint: disable=protected-access
    original_history = Calculator._history
    mock_history = MockCalculationHistory()

    try:
        Calculator._history = mock_history
        Calculator.add(10, 5)

        stored_calcs = mock_history.get_all_calculations()
        assert len(stored_calcs) == 1, "Mock history should have one calculation."
    finally:
        # Restore the original history to avoid side effects on other tests.
        Calculator.history = original_history
