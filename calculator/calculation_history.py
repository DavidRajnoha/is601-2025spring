import logging
from typing import List
from calculator.calculation import Calculation
from calculator.history import History


class CalculationHistory:
    """
    Manages a shared history of calculations and provides static methods for filtering and interaction.
    """
    _history: History[Calculation] = History[Calculation]()

    @staticmethod
    def add_calculation(calculation: Calculation) -> None:
        """
        Adds a calculation to the history.
        """
        logging.debug(f"Adding calculation to history: {calculation}")
        CalculationHistory._history.add_item(calculation)

    @staticmethod
    def get_all_calculations() -> List[Calculation]:
        """
        Returns all calculations in the history.
        """
        logging.debug("Getting all calculations from history")
        return CalculationHistory._history.get_items()

    @staticmethod
    def filter_by_operation_name(operation_name: str) -> List[Calculation]:
        """
        Filters calculations by operation name.
        """
        logging.debug(f"Filtering calculations by operation name: {operation_name}")
        return CalculationHistory._history.filter_item(
            lambda calc: calc.operation.__name__ == operation_name
        )

    @staticmethod
    def get_last() -> Calculation:
        """
        Returns the last calculation in the history.
        """
        logging.debug("Getting last calculation from history")
        return CalculationHistory._history.get_items()[-1]

    @staticmethod
    def clear_history() -> None:
        """
        Clears all calculations from the history.
        """
        logging.info("Clearing calculation history")
        CalculationHistory._history.clear()
