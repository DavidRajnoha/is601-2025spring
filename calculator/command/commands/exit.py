"""This module contains the ExitCommand class."""
from calculator.command.command import Command, ExitException
import logging

class ExitCommand(Command):
    """A command that exits the application."""
    def execute(self):
        logging.debug("Executing ExitCommand.")
        raise ExitException()