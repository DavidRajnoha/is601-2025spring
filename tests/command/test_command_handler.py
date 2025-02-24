"""
Test the CommandHandler class.
"""
# pylint: disable=protected-access
# Used for testing purposes only.
from calculator.command.command_handler import CommandHandler
from calculator.command.command import Command


class MockCommand(Command):
    """
    A mock command for testing purposes.
    """
    def __init__(self):
        self.executed = False

    def execute(self):
        self.executed = True


def test_register_command():
    """
    Test that a command is correctly registered.
    """
    handler = CommandHandler()
    command = MockCommand()
    handler.register("test", command)

    assert "test" in handler._commands
    assert handler._commands["test"] is command


def test_execute_registered_command():
    """
    Test that a registered command executes properly.
    """
    handler = CommandHandler()
    command = MockCommand()
    handler.register("test", command)

    handler.handle("test")
    assert command.executed is True


def test_execute_unregistered_command(capfd):
    """
    Test that handling an unregistered command prints an error.
    """
    handler = CommandHandler()

    handler.handle("nonexistent")

    captured = capfd.readouterr()
    assert 'Command "nonexistent" not found' in captured.out
