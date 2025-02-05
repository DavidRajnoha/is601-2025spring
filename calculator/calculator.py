from calculator.operations import add, subtract, multiply, divide

class Calculator:
    @staticmethod
    def add(a: float, b: float) -> float:
        return add(a,b)

    @staticmethod
    def subtract(a: float, b: float) -> float:
        return subtract(a,b)

    @staticmethod
    def multiply(a: float, b: float) -> float:
        return multiply(a,b)

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
        return divide(a, b)
