"""
This module contains the App class which is responsible for running the application.
"""
from calculator.command.command import GreetCommand, ExitException, ExitCommand
from calculator.command.command_handler import CommandHandler


class App:
    """
    App class is responsible for running the application.
    """
    command_handler = CommandHandler()

    def __init__(self):
        """
        Initializes the application with default commands.
        """
        self.command_handler.register("greet", GreetCommand())
        self.command_handler.register("exit", ExitCommand())

    def run(self):
        """
        Runs the application loop.
        """
        while True:
            try:
                command = input("Enter a command: ")
                self.command_handler.handle(command)
            except (ExitException, EOFError):
                print("Exiting the application...")
                break