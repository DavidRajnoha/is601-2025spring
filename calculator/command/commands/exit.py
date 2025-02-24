"""This module contains the ExitCommand class."""
from calculator.command.command import Command, ExitException

class ExitCommand(Command):
    """A command that exits the application."""
    def execute(self):
        raise ExitException()