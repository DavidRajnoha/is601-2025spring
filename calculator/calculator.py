from calculator.calculation import Calculation
from calculator.operations import add, subtract, multiply, divide
from calculator.calculation_history import CalculationHistory
from decimal import Decimal

import logging

class Calculator:
    _history = CalculationHistory

    @staticmethod
    def perform_operation(operation, a: Decimal, b: Decimal) -> Decimal:
        logging.debug(f"Performing operation: {operation.__name__}({a}, {b})")
        calculation = Calculation(operation, a, b)
        Calculator._history.add_calculation(calculation)
        return calculation.perform_operation()

    @staticmethod
    def add(a: Decimal, b: Decimal) -> Decimal:
        return Calculator.perform_operation(add, a, b)

    @staticmethod
    def subtract(a: Decimal, b: Decimal) -> Decimal:
        return Calculator.perform_operation(subtract, a, b)

    @staticmethod
    def multiply(a: Decimal, b: Decimal) -> Decimal:
        return Calculator.perform_operation(multiply, a, b)

    @staticmethod
    def divide(a: Decimal, b: Decimal) -> Decimal:
        """
        Divides a by b.

        Args:
            a (Decimal): Numerator.
            b (Decimal): Denominator.

        Returns:
            Decimal: The result of the division.

        Raises:
            ZeroDivisionError: If b is zero.
        """
        return Calculator.perform_operation(divide, a, b)
