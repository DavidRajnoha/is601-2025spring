from abc import ABC, abstractmethod


class Command(ABC):
    """
    Command interface declares a method for executing a command.
    """
    @abstractmethod
    def execute(self):
        pass


class GreetCommand(Command):
    """
    GreetCommand class is a concrete command that prints a greeting.
    """
    def execute(self):
        print("Hello, World!")


class ExitException(Exception):
    pass


class ExitCommand(Command):
    """
    ExitCommand class is a concrete command that exits the application.
    """
    def execute(self):
        raise ExitException()