import sys
import os
import subprocess
import pytest

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
SCRIPT_PATH = os.path.join(PROJECT_ROOT, "main.py")


# List of test cases: each tuple contains a, b, operation, expected_output.
# Note: The expected messages exactly match what the main file prints.
TEST_CASES = [
    ("5", "3", "add", "The result of 5 add 3 is equal to 8"),
    ("10", "2", "subtract", "The result of 10 subtract 2 is equal to 8"),
    ("4", "5", "multiply", "The result of 4 multiply 5 is equal to 20"),
    ("20", "4", "divide", "The result of 20 divide 4 is equal to 5"),
    ("1", "0", "divide", "An error occurred: Cannot divide by zero."),
    ("9", "3", "unknown", "Unknown operation: unknown"),
    ("a", "3", "add", "Invalid number input: a or 3 is not a valid number."),
    ("5", "b", "subtract", "Invalid number input: 5 or b is not a valid number.")
]

@pytest.mark.parametrize("a, b, operation, expected_output", TEST_CASES)
def test_entrypoint(a, b, operation, expected_output):
    """
    Call the script via subprocess using the current Python interpreter.
    """
    result = subprocess.run([sys.executable, SCRIPT_PATH, a, b, operation],
                            capture_output=True, text=True)
    output = result.stdout.strip()
    assert output == expected_output, f"Got {output!r} instead of {expected_output!r}"
