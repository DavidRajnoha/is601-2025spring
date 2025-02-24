"""
SubtractCommand class module.
"""
from calculator.calculator import Calculator
from calculator.command.command import Command
from calculator.command.commands.operation_executor import OperationExecutor


class SubtractCommand(Command):
    """
    A command that performs subtraction.
    """
    def __init__(self, executor=None):
        """
        Initializes the SubtractCommand with an optional OperationExecutor.
        """
        self.executor = executor or OperationExecutor(Calculator.subtract, "Subtraction")

    def execute(self):
        """
        Executes the command.
        """
        self.executor.execute()