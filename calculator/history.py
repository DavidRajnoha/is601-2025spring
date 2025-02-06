from typing import Generic, TypeVar, List

T = TypeVar('T')

class History(Generic[T]):
    """
    Represents a history of items of type T.

    Attributes:
        items (List[T]): A list of items of type T.
    """

    def __init__(self):
        """Initializes an empty history."""
        self.items = []

    def add_item(self, item: T):
        """
        Adds an item to the history.

        Args:
            item (T): The item to add.
        """
        self.items.append(item)

    def get_items(self) -> List[T]:
        """
        Returns the list of items in the history.

        Returns:
            List[T]: A list of items of type T.
        """
        return self.items

    def filter_item(self, filter_func):
        """
        Returns a list of items that satisfy the filter function.

        Args:
            filter_func: A function that takes an item and returns a boolean.

        Returns:
            List[T]: A list of items that satisfy the filter function.
        """
        return [item for item in self.items if filter_func(item)]

    def clear(self):
        """Clears the history."""
        self.items = []