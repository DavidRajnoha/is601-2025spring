# pylint: disable=redefined-outer-name
"""This module contains tests for the History class defined in calculator.history.
It verifies that items are correctly added, filtered, and cleared."""

import pytest
from calculator.history import History


@pytest.fixture
def int_history():
    """
    Fixture for a History instance that handles integers.
    """
    return History[int]()


@pytest.fixture
def str_history():
    """
    Fixture for a History instance that handles strings.
    """
    return History[str]()


def test_add_and_get_items(int_history):
    """Test adding integers and retrieving them."""
    int_history.add_item(1)
    int_history.add_item(2)
    int_history.add_item(3)
    assert int_history.get_items() == [1, 2, 3], ("Items were not added"
                                                  " correctly to the history.")


def test_filter_item(int_history):
    """Test filtering even numbers from the history."""
    for i in range(10):
        int_history.add_item(i)
    even_items = int_history.filter_item(lambda x: x % 2 == 0)
    expected = [0, 2, 4, 6, 8]
    assert even_items == expected, ("filter_item did not return the correct"
                                    " filtered list of even numbers.")


def test_filter_item_empty(int_history):
    """Test filtering on an empty history."""
    filtered = int_history.filter_item(lambda x: x % 2 == 0)
    assert filtered == [], "Filtering an empty history should return an empty list."


def test_clear(str_history):
    """Test clearing the history."""
    str_history.add_item("a")
    str_history.add_item("b")
    assert str_history.get_items() == ["a", "b"], ("Initial items do not match"
                                                   " expected list.")
    str_history.clear()
    assert str_history.get_items() == [], "Clear method did not empty the history."


def test_filter_item_with_custom_condition(str_history):
    """Test filtering strings that start with a specific letter."""
    items = ["apple", "banana", "apricot", "cherry"]
    for item in items:
        str_history.add_item(item)
    filtered = str_history.filter_item(lambda s: s.startswith("a"))
    expected = ["apple", "apricot"]
    assert filtered == expected, "filter_item did not correctly filter strings starting with 'a'."
