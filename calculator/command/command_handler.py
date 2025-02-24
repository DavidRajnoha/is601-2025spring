class CommandHandler:
    """
    CommandHandler class is responsible for handling commands.
    """
    def __init__(self):
        self._commands = {}

    def register(self, command_name, command):
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
