"""
This module contains the fixtures for the calculator operations.
"""

# pylint: disable=comparison-with-callable

from decimal import Decimal

from faker import Faker
from calculator.operations import add, subtract, multiply, divide


fake = Faker()


class InvalidStateException(Exception):
    """
    Custom exception for invalid state.
    """


def generate_test_data(num_records: int) -> list:
    """
    Generate test data for calculator operations.
    """
    operation_mappings = {
        "add": add,
        "subtract": subtract,
        "multiply": multiply,
        "divide": divide,
    }

    for i in range(num_records):
        a = Decimal(fake.random_number(digits=2))
        b = Decimal(fake.random_number(digits=2)) if i % 4 != 3 else\
            Decimal(fake.random_number(digits=1))
        operation_name = fake.random_element(elements=(list(operation_mappings.keys())))
        operation = operation_mappings[operation_name]

        b = Decimal('1') if operation == divide and b == 0 else b

        try:
            expected = operation(a, b)
        except ZeroDivisionError as exc:
            raise InvalidStateException("This statement should not"
                                        " be reached, b is set to 1 if it is"
                                        " 0 for division operation") from exc

        yield a, b, operation_name, operation, expected


def pytest_addoption(parser):
    """
    Add option to generate test data.
    """
    parser.addoption("--num-records", action="store", default=50,
                     help="Number of records to generate")

def pytest_generate_tests(metafunc):
    """
    Inject test data into the test functions.
    """
    if ({"a", "b", "expected"}.intersection(set(metafunc.fixturenames))
            and "operation" in metafunc.fixturenames):
        num_records = metafunc.config.getoption("num_records")
        parameters = list(generate_test_data(num_records))
        modified_parameters = [(a, b, op_name if 'operation_name' in metafunc.fixturenames
        else op_func, expected) for a, b, op_name, op_func, expected in parameters]
        metafunc.parametrize("a,b,operation,expected", modified_parameters)
    elif ({"a", "b", "expected"}.intersection(set(metafunc.fixturenames))
          and "operation" not in metafunc.fixturenames):
        metafunc_name = metafunc.function.__name__
        num_records = metafunc.config.getoption("num_records")
        parameters = list(generate_test_data(num_records))
        filtered_parameters = [param for param in parameters if param[2] in metafunc_name]
        modified_parameters = [(a, b, expected) for a, b, _, _, expected in filtered_parameters]
        metafunc.parametrize("a,b,expected", modified_parameters)
