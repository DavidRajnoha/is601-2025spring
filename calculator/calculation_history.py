from typing import List

from calculator.calculation import Calculation
from calculator.history import History


class CalculationHistory:
    """
    Manages a history of calculations and provides methods for filtering and interaction.
    """

    def __init__(self):
        """Initializes the calculation history with an empty History of Calculation objects."""
        self.history = History[Calculation]()

    def add_calculation(self, calculation: Calculation):
        """Adds a calculation to the history."""
        self.history.add_item(calculation)

    def get_all_calculations(self) -> List[Calculation]:
        """Returns all calculations in the history."""
        return self.history.get_items()

    def filter_by_operation_name(self, operation_name: str) -> List[Calculation]:
        """
        Filters calculations by operation name.

        Args:
            operation_name (str): The name of the operation to filter by.

        Returns:
            List[Calculation]: A list of calculations that match the operation name.
        """
        return self.history.filter_item(lambda calc: calc.operation.__name__ == operation_name)

    def clear_history(self):
        """Clears all calculations from the history."""
        self.history.clear()