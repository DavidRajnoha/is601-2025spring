"""
AddCommand class module.
"""
from calculator.calculator import Calculator
from calculator.command.command import Command
from calculator.command.commands.operation_executor import OperationExecutor


class AddCommand(Command):
    """
    A command that performs addition.
    """
    def __init__(self, executor=None):
        """
        Initializes the AddCommand with an optional OperationExecutor.
        """
        self.executor = executor or OperationExecutor(Calculator.add, "Addition")

    def execute(self):
        """
        Executes the command.
        """
        self.executor.execute()