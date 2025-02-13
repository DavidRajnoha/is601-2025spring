from typing import Callable
from decimal import Decimal

class Calculation:
    """
    Represents a calculation that uses a binary operation on two numbers.

    Attributes:
        operation (Callable[[Decimal, Decimal], Decimal]): A function that takes two Decimals and returns a Decimal.
        a (Decimal): The first operand.
        b (Decimal): The second operand.
    """

    def __init__(self, operation: Callable[[Decimal, Decimal], Decimal], a: Decimal, b: Decimal):
        """
        Initializes the Calculation with a specific operation and two operands.

        Args:
            operation (Callable[[Decimal, Decimal], Decimal]): The operation to perform.
            a (Decimal): The first number.
            b (Decimal): The second number.
        """
        self.operation = operation
        self.a = a
        self.b = b

    def perform_operation(self):
        """
        Performs the calculation using the provided operation on the operands.

        Returns:
            Decimal: The result of applying the operation to a and b.

        Raises:
            Exception: Propagates any exception raised by the operation.
        """
        return self.operation(self.a, self.b)