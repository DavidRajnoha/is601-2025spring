"""
MultiplyCommand class module.
"""
from calculator.calculator import Calculator
from calculator.command.command import Command
from calculator.command.commands.operation_executor import OperationExecutor


class MultiplyCommand(Command):
    """
    A command that performs multiplication.
    """
    def __init__(self, executor=None):
        """
        Initializes the MultiplyCommand with an optional OperationExecutor.
        """
        self.executor = executor or OperationExecutor(Calculator.multiply, "Multiplication")

    def execute(self):
        """
        Executes the command.
        """
        self.executor.execute()