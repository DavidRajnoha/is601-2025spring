import importlib
import inspect
import pkgutil
from difflib import get_close_matches
from calculator.command.command import Command


class CommandHandler:
    """
    CommandHandler class is responsible for handling commands.
    """
    def __init__(self):
        self._commands = {"help": HelpCommand(self)}

    def load_commands(self, package):
        self._load_commands(package)

    def _load_commands(self, package):
        """Dynamically discover and register all commands in the 'calculator.command' package."""
        for _, module_name, _ in pkgutil.iter_modules(package.__path__, package.__name__ + "."):
            module = importlib.import_module(module_name)
            for _, obj in inspect.getmembers(module, inspect.isclass):
                if issubclass(obj, Command) and obj is not Command:
                    command_name = module_name.split(".")[-1]  # Extract file name as command name
                    self._register(command_name, obj())

    def _register(self, command_name, command):
        """
        Registers a command with the handler.
        """
        self._commands[command_name] = command

    def handle(self, command_name):
        """
        Handles a command by executing it.
        """
        command = self._commands.get(command_name, None)
        try:
            command.execute()
        except AttributeError:
            self.handle_invalid_command(command_name)

    def handle_invalid_command(self, command_name):
        """
        Handles an invalid command by suggesting a similar command.
        """
        try:
            suggested_command = self._suggest_command(command_name)
            print(f'Command "{command_name}" not found. Did you mean "{suggested_command}"?')
        except SuggestionFailed:
            print(f'Command "{command_name}" not found')
            self._commands["help"].execute()

    def get_commands(self):
        """
        Returns a list of available commands.
        """
        return sorted(self._commands.keys())

    def _suggest_command(self, invalid_command):
        """
        Returns a suggested command name if one is similar enough to the invalid_command.
        """
        available = self.get_commands()
        # get_close_matches returns a list; we pick the best match if available.
        matches = get_close_matches(invalid_command, available, n=1, cutoff=0.6)
        try:
            return matches[0]
        except IndexError:
            raise SuggestionFailed


class SuggestionFailed(Exception):
    """
    Raised when a command suggestion fails.
    """

class HelpCommand(Command):
    """
    HelpCommand presents usage information by listing all available commands.
    """
    def __init__(self, command_handler):
        self.command_handler = command_handler

    def execute(self):
        print("Available commands:")
        for command_name in sorted(self.command_handler.get_commands()):
            print(f"  {command_name}")
