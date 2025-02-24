"""
This module contains the App class which is responsible for running the application.
"""
from calculator.command.command import ExitException
from calculator.command.command_handler import CommandHandler
import calculator.command.commands as commands_package



class App:
    """
    App class is responsible for running the application.
    """
    command_handler = CommandHandler()
    command_handler.load_commands(commands_package)

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