from calculator.calculation import Calculation
from calculator.operations import add, subtract, multiply, divide

class Calculator:
    @staticmethod
    def perform_operation(operation, a: float, b: float) -> float:
        calculation = Calculation(operation, a, b)
        return calculation.perform_operation()

    @staticmethod
    def add(a: float, b: float) -> float:
        return Calculator.perform_operation(add, a, b)

    @staticmethod
    def subtract(a: float, b: float) -> float:
        return Calculator.perform_operation(subtract, a, b)

    @staticmethod
    def multiply(a: float, b: float) -> float:
        return Calculator.perform_operation(multiply, a, b)

    @staticmethod
    def divide(a: float, b: float) -> float:
        """
        Divides a by b.

        Args:
            a (float): Numerator.
            b (float): Denominator.

        Returns:
            float: The result of the division.

        Raises:
            ZeroDivisionError: If b is zero.
        """
        return Calculator.perform_operation(divide, a, b)
