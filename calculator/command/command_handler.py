import importlib
import inspect
import pkgutil

from calculator.command.command import Command


class CommandHandler:
    """
    CommandHandler class is responsible for handling commands.
    """
    def __init__(self):
        self._commands = {}

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
        command = self._commands.get(command_name)
        try:
            command.execute()
        except AttributeError:
            print(f'Command "{command_name}" not found')
