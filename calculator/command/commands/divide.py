"""
DivideCommand class module.
"""
from calculator.calculator import Calculator
from calculator.command.command import Command
from calculator.command.commands.operation_executor import OperationExecutor


class DivideCommand(Command):
    """
    A command that performs division.
    """
    def __init__(self, executor=None):
        """
        Initializes the DivideCommand with an optional OperationExecutor.
        """
        self.executor = executor or OperationExecutor(Calculator.divide, "division")

    def execute(self):
        """
        Executes the command.
        """
        self.executor.execute()