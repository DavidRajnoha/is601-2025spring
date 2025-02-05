from typing import Callable

class Calculation:
    """
    Represents a calculation that uses a binary operation on two numbers.

    Attributes:
        operation (Callable[[float, float], float]): A function that takes two floats and returns a float.
        a (float): The first operand.
        b (float): The second operand.
    """

    def __init__(self, operation: Callable[[float, float], float], a: float, b: float):
        """
        Initializes the Calculation with a specific operation and two operands.

        Args:
            operation (Callable[[float, float], float]): The operation to perform.
            a (float): The first number.
            b (float): The second number.
        """
        self.operation = operation
        self.a = a
        self.b = b

    def perform_operation(self):
        """
        Performs the calculation using the provided operation on the operands.

        Returns:
            float: The result of applying the operation to a and b.

        Raises:
            Exception: Propagates any exception raised by the operation.
        """
        return self.operation(self.a, self.b)